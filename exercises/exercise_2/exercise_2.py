import json
import sys

tab = "  "
package_delimiter = "-"
dependency_delimiter = "\n"
space = " "


class PackageNotDefinedError(Exception):
    """
    Custom Error class created for the case when an operation on an undefined package (e.g. from a JSON file) is tried.
    """

    def __init__(self, message):
        super().__init__(message)


class DependencyGraph:
    """
    Class that defines a Dependency Graph: a graph of packages with their dependencies. This class can read the JSON
    configuration of this graph from a file, and can represent both the whole graph as a string, or the dependencies
    of a single package given as argument.
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.dependencies_dict = {}
        self.pkg_cache_repr = {}
        self._read()

    def _read(self):
        """
        Function that reads the JSON dependencies graph into the dependencies_dict.
        """
        with open(self.filename, 'r') as f:
            self.dependencies_dict = json.load(f)

    @staticmethod
    def indent_lines(lines: str = "", nr_of_tabs: int = 0) -> str:
        """
        Function that puts a given number of tabs (:param nr_of_tabs) at the beginning of each new line, in order to be
        able to construct the dependency graph at any depth level.
        :param lines: the string that represents the dependencies of a package, as lines
        :type lines: str
        :param nr_of_tabs: the number of tabs that must be inserted to the beginning of each line
        :type nr_of_tabs: int
        :return: the transformed string
        :rtype: str
        """
        lines = lines.replace(package_delimiter, tab * nr_of_tabs + package_delimiter)
        return lines

    def repr(self, package: str, nr_of_tabs: int = 0) -> str:
        """
        Function that returns the graph representation of the dependencies of a given package (:param package), at a
        given depth level (:param nr_of_tabs)
        :param package: the package to be represented
        :type package: str
        :param nr_of_tabs: the depth level (number of tabs to be added at the beginning of each line from the string
        representation of the output)
        :type nr_of_tabs: int
        :return: the string representation of the dependencies of the given package
        :rtype: str
        """
        if package not in self.dependencies_dict.keys():
            raise PackageNotDefinedError(f"Package {package} does not exist!")
        repr_for_package = tab * nr_of_tabs + package_delimiter + space + package
        for dep in self.dependencies_dict[package]:
            if dep not in self.pkg_cache_repr.keys():
                self.pkg_cache_repr[dep] = self.repr(dep, 0)
            repr_for_package += dependency_delimiter + DependencyGraph.indent_lines(self.pkg_cache_repr[dep],
                                                                                    nr_of_tabs + 1)
        return repr_for_package

    def __str__(self):
        """
        Function that overrides the str functionality, into the string representation of the JSON graph.
        :return: str
        """
        result = ""
        for package in self.dependencies_dict:
            result += self.repr(package, 0) + "\n"
        return result


def return_dep_graph(path: str = '/tmp/deps.json') -> str:
    """
    Function that returns the string representation of an entire graph that is read from the given path (:param path)
    :param path: the path where the JSON representation of the graph is found
    :type path: str
    :return: the string representation of the dependencies graph
    :rtype: str
    """
    return str(DependencyGraph(path))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(return_dep_graph(sys.argv[1]))
    else:
        print(return_dep_graph())
