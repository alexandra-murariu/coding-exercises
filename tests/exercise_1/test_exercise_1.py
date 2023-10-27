import unittest
from exercises.exercise_1.exercise_1 import get_duplicates


class TestExercise1(unittest.TestCase):
    def test_get_duplicates_different_objects_list(self):
        lst = [1, 2]
        self.assertEqual(get_duplicates(["b", 1, 2, "a", 3, (1, 2), lst, "b", (1, 2), lst, 3.0, 4.0, 3, "a"]),
                         ['b', (1, 2), [1, 2], 3, 'a'])

    def test_get_duplicates_copy_of_list(self):
        self.assertEqual(get_duplicates(["b", 1, 2, "a", 3, (1, 2), [1, 2], "b", (1, 2), [1, 2], 3.0, 4.0, 3, "a"]),
                         ['b', (1, 2), 3, 'a'])

    def test_get_duplicates_empty_list(self):
        self.assertEqual(get_duplicates([]), [])

    def test_get_duplicates_no_duplicates(self):
        self.assertEqual(get_duplicates(["b", 1, 2, "a", 3, (1, 2)]), [])

    def test_get_duplicates_only_duplicates(self):
        self.assertEqual(get_duplicates(["b", 1, 2, "a", 3, (1, 2), "b", 1, 2, "a", 3, (1, 2)]),
                         ["b", 1, 2, "a", 3, (1, 2)])


if __name__ == "__main__":
    unittest.main()
