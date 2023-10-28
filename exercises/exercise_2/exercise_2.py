import json


class Tree:
    def __init__(self, filename='/tmp/deps.json'):
        self.filename = filename
        self.dependencies_dict = {}
        self.pkg_cache_repr = {}
        self._read()

    def _read(self):
        with open(self.filename, 'r') as f:
            self.dependencies_dict = json.load(f)

    @staticmethod
    def indent_lines(lines="", nr_of_tabs=0):
        lines = lines.replace("-", "  " * nr_of_tabs + "-")
        return lines

    def repr(self, package: str, nr_of_tabs=0):
        repr_for_package = "  " * nr_of_tabs + "- " + package
        for dep in self.dependencies_dict[package]:
            if dep not in self.pkg_cache_repr.keys():
                self.pkg_cache_repr[dep] = self.repr(dep, 0)
            repr_for_package += "\n" + Tree.indent_lines(self.pkg_cache_repr[dep], nr_of_tabs+1)
        return repr_for_package

    def __str__(self):
        result = ""
        for package in self.dependencies_dict:
            result += self.repr(package, 0) + "\n"
        return result


if __name__ == "__main__":
    t = Tree(r"helpers/c.json")
    print(t)
    # print(t.repr("pkg1"))
