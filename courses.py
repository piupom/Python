"""
Implement a Python module "courses" that provides the following facilities for handling course data:

    A class Course with attributes code, name, minCredits and maxCredits. The class needs to have:
        An initialization function that receives initialization values for these attributes (in the same order as they were mentioned here).
            The attributes code and name are strings. The attributes minCredits and maxCredits are integers.
        A string conversion function that returns a string of form "code name minCredits ECTS" or "code name minCredits-maxCredits ECTS", depending on whether minCredits == maxCredits or not.
        An equality comparison function __eq__(self, other) that compares Course-objects bases on their names (this is similar to what was done in a lecture example regarding __lt__).
        A function __hash__(self) that returns the value self.name.__hash__().
            Without going into details, having both the __eq__ and the __hash__-function enables us to use Course-objects as dictionary keys or set values. In this question we will not really create an own implementation but just reuse the __hash__-function of the attribute name. The end result is that in terms of dictionary keys or set values, two Course-objects are deeed to be identical if their names are identical.
    A function readCourses(filename) that reads course information from the file specified by the parameter filename and creates and returns a list of Course-objects that describe all courses in the file (in the order they appeared).
        Inspect the file courses.txt to see how the course information is structured. You need to do some suitable string matching operations in order to pick out the essential course information.
        You do not need to worry about duplicates (whether or not the same course appears more than once).

"""

import sys
from courses import Course, readCourses

# Read the course list
courseList = readCourses(sys.argv[1])

# Try to add one more course
courseList.append(Course("TIETA19", "Practical Programming in Python", 5, 5))

# Print out all types present in the courseList (should be only Course)
print(set(map(type, courseList)), end="\n\n")

# Print out all occurrences of course descriptions in the input (+ 1 added)
print("All course occurrences:")
for course in courseList:
  print(course)

# Print out only unique occurrences (based on course name)
print("\nUnique course occurrences:")
for course in sorted(set(courseList), key=str):
	print(course)