# Coding exercises

These exercises were solved as part of an assessment.

## Description

There are two exercises in this repository. They are present in the [exercises](exercises) folder, in separate
subfolders. The unit tests are present inside the [tests](tests) directory.

The [exercises](exercises) and the [tests](tests) folders have the same internal structure, apart from the fact that
each test file is prefixed with "test_". For example, the tests for [exercise_1.py](exercises/exercise_1/exercise_1.py)
are located inside [test_exercise_1.py](tests/exercise_1/test_exercise_1.py) file.

The [.github](.github) folder is the place where the Github CI pipeline is configured.

The [conf.py](conf.py) and [index.rst](index.rst) are necessary for auto-documenting the code using
the [Sphinx](https://www.sphinx-doc.org/en/master/) package.

## Solutions

### First exercise

For the first exercise, I created two solutions. The problem does not specify if all objects are of the same type, or if
they are hashable types. So, I considered two scenarios:

* **random objects:** For the case in which the input list can contain both hashable and non-hashable objects, the
  solution is present in [exercise_1.py](exercises/exercise_1/exercise_1.py). I created a function that gets as
  parameters the list and also a comparator function. This defines the "duplicate" state, based on the equality function
  that is checked among objects. As there are more possibilities, such as overridable "==", but also "is", I considered
  best to let the user choose what he would like duplicates to mean.
    * Example: For the input ["b", 1, 2, "a", 3, (1, 2), [1, 2], "b", (1, 2), [1, 2], 3.0, 4.0, 3, "a"], there are
      different solutions based on the comparator function that is being used:
        * "**==**": ['b', (1, 2), [1, 2], 3, 'a']
        * "**is**": ['b', (1, 2), 3, 'a']
        * This is because when lists are compared with the "==" operator, they are equal if they have equal items at the
          same positions. But if they are checked with the "is" operator, they need to be exactly the same object,
          defined at the same place in memory. In the solution, the algorithm iterates through the input list and keeps
          track of seen
          items. Then, if the item was a new unseen one, it adds it to the list of seen items. If not, it also checks
          that the item is not already part of the result, and if not, it adds it to the result.

* **hashable objects:** For the case in which all elements from the input list are hashable, a more effective solution
  is possible. The algorithm iterates through all elements from the input, and then adds them as keys in a dictionary
  with frequency of each element - the value is incremented at each new occurence in the input list of that specific
  key. In the end, only
  elements that appeared as key with at least 2 occurences in the dictionary are added to the result list, meaning they
  are duplicated. The solution for this case is presented
  in [exercise_1_hashable_objects.py](exercises/exercise_1/exercise_1_hashable_objects.py). It is
  more efficient because all objects (keys) are put in a dictionary, which provides a hashmap for all the keys, so the
  lookup operation is only O(1) on average time complexity.

### Second exercise

The solution for the second exercise is located here: [exercise_2.py](exercises/exercise_2/exercise_2.py).

In the solution, I created a DependencyGraph class. In the constructor, it is given the path to the JSON representation
of the dependencies graph. It also reads the input from the file and saves it in a dictionary attribute.

Through the overriden __str__ function, a string representation of the graph is returned. This function iterates through
all packages from the dependencies dictionary, and calls the **repr** method from the class, giving the package name as
argument. The **repr** method returns the string representation of the dependencies of a given package, recursively.
Meaning that if pkg1 has a dependency on pkg2, then the string representation of the dependencies of pkg1 will also
contain repr(pkg2, nr_of_tabs+1). The second argument specifies the depth of the dependency, which comes with more tabs
in the output representation.

The string representations of packages are being _cached_ with a tab size of zero, so that
if another package has a dependency on an already cached package, the recursion shouldn't be done again - instead, the
string representation for the dependency package is retrieved from the cache dictionary of the DependencyGraph object,
and indented according to the depth of the dependency.

I also created a separate function that receives the path to the JSON file as argument (default='/tmp/deps.json'), and
returns the string representation of that graph.

#### Executing program

There are two options for running [exercise_2.py](exercises/exercise_2/exercise_2.py):

* ```
  python -m exercise_2
  ```
* ```
  python -m exercise_2 helpers/c.json
  ```

The first option will read the JSON representation of the graph from the default location: "/tmp/deps.json", while the
second option can receive as argument the path to the JSON file to be read.

## CI pipeline

The pipeline executes the following steps at each commit:

1. dependencies installation (e.g. flake8, sphinx, coverage).
2. lint with flake8
    * this stops the build if there are any syntax errors or undefined names in the code
    * it checks for PEP8 standards
3. custom bash script that verifies that there are unit test files for each module inside the [exercises](exercises)
   directory
4. run all unit tests, calculate and display coverage, and also write an HTML coverage report, that also contains
   information about the lines that weren't covered by unit tests
5. generate HTML documentation using the Sphinx library with autodoc, based on docstrings from the code in the
   repository
6. deploy generated documentation to https://alexandra-murariu.github.io/coding-exercises/
7. upload coverage report as artifact
8. upload documentation as artifact

## Author

[Alexandra Murariu](murariu.alexandra2002@gmail.com)

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details
