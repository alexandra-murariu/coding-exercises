import unittest
from exercises.exercise_1.exercise_1_hashable_objects import get_duplicates


class TestExercise1HashableObjects(unittest.TestCase):
    def test_get_duplicates_hashable_objects_list(self):
        self.assertEqual(
            get_duplicates(["a", "apple", "@", "B", "!", "9", "car", "apple", "X", "&", "a", "1", "B", "z", "9"]),
            ['a', 'apple', 'B', '9'])

    def test_get_duplicates_non_hashable_objects(self):
        with self.assertRaises(TypeError) as e:
            get_duplicates(["b", 1, 2, "a", 3, (1, 2), [1, 2], "b", (1, 2), [1, 2], 3.0, 4.0, 3, "a"])
        self.assertEqual(str(e.exception), "unhashable type: 'list'")

    def test_get_duplicates_empty_list(self):
        self.assertEqual(get_duplicates([]), [])

    def test_get_duplicates_no_duplicates(self):
        self.assertEqual(get_duplicates(["b", 1, 2, "a", 3, (1, 2)]), [])

    def test_get_duplicates_only_duplicates(self):
        self.assertEqual(get_duplicates(["b", 1, 2, "a", 3, (1, 2), "b", 1, 2, "a", 3, (1, 2)]),
                         ["b", 1, 2, "a", 3, (1, 2)])


if __name__ == "__main__":
    unittest.main()
