import json.decoder
import unittest
from unittest.mock import patch, mock_open
from exercises.exercise_2.exercise_2 import DependencyGraph, return_dep_graph, PackageNotDefinedError


class TestDependencyGraph(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='{"pkg1": ["pkg2", "pkg3"],"pkg2": ["pkg3"],"pkg3": []}')
    def test__read_valid_json(self, mock_read):
        d = DependencyGraph('path/to/file')
        self.assertEqual(d.dependencies_dict, {"pkg1": ["pkg2", "pkg3"], "pkg2": ["pkg3"], "pkg3": []})

    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    def test__read_invalid_json(self, mock_read):
        with self.assertRaises(json.decoder.JSONDecodeError) as e:
            DependencyGraph('path/to/file')
        self.assertEqual(str(e.exception), "Expecting value: line 1 column 1 (char 0)")

    def test_indent_lines_one_tab(self):
        self.assertEqual(DependencyGraph.indent_lines("- pkg1\n  - pkg2", 1), "  - pkg1\n    - pkg2")

    def test_indent_lines_no_tabs(self):
        self.assertEqual(DependencyGraph.indent_lines("- pkg1\n  - pkg2", 0), "- pkg1\n  - pkg2")

    def test_indent_lines_empty_string(self):
        self.assertEqual(DependencyGraph.indent_lines(""), "")

    @patch('builtins.open', new_callable=mock_open, read_data='{"pkg1": []}')
    def test_repr_single_package_no_dependencies(self, mock_read):
        d = DependencyGraph('path/to/file')
        self.assertEqual(d.package_repr("pkg1"), "- pkg1")

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3"], "pkg2": [], "pkg3": []}')
    def test_repr_multiple_packages_nonrecursive_dependencies(self, mock_read):
        d = DependencyGraph('path/to/file')
        self.assertEqual(d.package_repr("pkg1"), "- pkg1\n  - pkg2\n  - pkg3")

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3"], "pkg2": ["pkg3"], "pkg3": []}')
    def test_repr_multiple_packages_recursive_dependencies(self, mock_read):
        d = DependencyGraph('path/to/file')
        self.assertEqual(d.package_repr("pkg1"), "- pkg1\n  - pkg2\n    - pkg3\n  - pkg3")

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3"], "pkg2": ["pkg3"], "pkg3": []}')
    def test_repr_nonexistent_package(self, mock_read):
        d = DependencyGraph('path/to/file')
        with self.assertRaises(PackageNotDefinedError) as e:
            d.package_repr("pkg4")
        self.assertEqual(str(e.exception), "Package pkg4 does not exist!")

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3", "pkg4"], "pkg2": ["pkg3"], "pkg3": []}')
    def test_repr_nonexistent_package_as_dependency(self, mock_read):
        d = DependencyGraph('path/to/file')
        with self.assertRaises(PackageNotDefinedError) as e:
            d.package_repr("pkg1")
        self.assertEqual(str(e.exception), "Package pkg4 does not exist!")

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3", "pkg4"], "pkg2": ["pkg3"], "pkg3": []}')
    def test__str__invalid_graph(self, mock_read):
        d = DependencyGraph('path/to/file')
        with self.assertRaises(PackageNotDefinedError) as e:
            str(d)
        self.assertEqual(str(e.exception), "Package pkg4 does not exist!")

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3", "pkg4"],"pkg2": ["pkg3", "pkg5"],"pkg3": ["pkg6"],"pkg4": ["pkg7"],'
                     '"pkg5": ["pkg7", "pkg8"],"pkg6": ["pkg9"],"pkg7": [],"pkg8": ["pkg10"],"pkg9": [],'
                     '"pkg10": ["pkg11", "pkg12"],"pkg11": [],"pkg12": []}')
    def test__str__of_dependency_graph(self, mock_read):
        d = DependencyGraph('path/to/file')
        expected_result = (
            "- pkg1\n"
            "  - pkg2\n"
            "    - pkg3\n"
            "      - pkg6\n"
            "        - pkg9\n"
            "    - pkg5\n"
            "      - pkg7\n"
            "      - pkg8\n"
            "        - pkg10\n"
            "          - pkg11\n"
            "          - pkg12\n"
            "  - pkg3\n"
            "    - pkg6\n"
            "      - pkg9\n"
            "  - pkg4\n"
            "    - pkg7\n"
            "- pkg2\n"
            "  - pkg3\n"
            "    - pkg6\n"
            "      - pkg9\n"
            "  - pkg5\n"
            "    - pkg7\n"
            "    - pkg8\n"
            "      - pkg10\n"
            "        - pkg11\n"
            "        - pkg12\n"
            "- pkg3\n"
            "  - pkg6\n"
            "    - pkg9\n"
            "- pkg4\n"
            "  - pkg7\n"
            "- pkg5\n"
            "  - pkg7\n"
            "  - pkg8\n"
            "    - pkg10\n"
            "      - pkg11\n"
            "      - pkg12\n"
            "- pkg6\n"
            "  - pkg9\n"
            "- pkg7\n"
            "- pkg8\n"
            "  - pkg10\n"
            "    - pkg11\n"
            "    - pkg12\n"
            "- pkg9\n"
            "- pkg10\n"
            "  - pkg11\n"
            "  - pkg12\n"
            "- pkg11\n"
            "- pkg12\n"
        )
        actual_result = str(d)
        self.assertEqual(actual_result, expected_result)

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"pkg1": ["pkg2", "pkg3"], "pkg2": [], "pkg3": []}')
    def test_return_dep_graph(self, mock_read):
        self.assertEqual(return_dep_graph(), "- pkg1\n  - pkg2\n  - pkg3\n- pkg2\n- pkg3\n")


if __name__ == "__main__":
    unittest.main()
