"""
Problem:
    Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:



    Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.

    In text form, it looks like this (with ⟶ representing the tab character):

    dir
    ⟶ subdir1
    ⟶ ⟶ file1.ext
    ⟶ ⟶ subsubdir1
    ⟶ subdir2
    ⟶ ⟶ subsubdir2
    ⟶ ⟶ ⟶ file2.ext
    If we were to write this representation in code, it will look like this: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". Note that the '\n' and '\t' are the new-line and tab characters.

    Every file and directory has a unique absolute path in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by '/'s. Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of letters, digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits, and/or spaces.

    Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

    Note that the testcases are generated such that the file system is valid and no file or directory name has length 0.

    

    Example 1:


    Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    Output: 20
    Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
    Example 2:


    Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    Output: 32
    Explanation: We have two files:
    "dir/subdir1/file1.ext" of length 21
    "dir/subdir2/subsubdir2/file2.ext" of length 32.
    We return 32 since it is the longest absolute path to a file.
    Example 3:

    Input: input = "a"
    Output: 0
    Explanation: We do not have any files, just a single directory named "a".

Solution:
    Use stack to represent structure of a directory where the root of a directory is at index 0. Directory level can be infer from the number of tabs. ie "" is level 0, "\n" is level 1 and so on.

    Start by splitting input based on nextline. For each path, find the number of tabs and name of the folder/file. Then, while there exists a folder/file at lower level than the current path, pop it. Next, add the folder/file onto the stack. As you adding and popping folder/file from the stack, keep track of the length of stack. Lastly, once we reach a folder, update the result

Complexity:
    Time: O(n) where n is the number of folder/file in the input
    Space: O(n)
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:

        # Split input based on next
        names = input.split("\n")

        # Initialize the current stack length and the max stack length
        curL, maxL = 0, 0

        # Initialize the stack
        stack = []

        # For each name
        for name in names:

            # Split the current name by the tab
            name = name.split("\t")

            # Find the number of tab and the current folder/file name
            tabs, name = len(name) - 1, name[-1]

            # While there exisits a folder/file at the lower level than the current folder/file
            while len(stack) > tabs:

                # Pop them and update the curent length of the stack
                curL -= len(stack.pop())

            # Add the current folder/file onto the stack
            curL += len(name)
            stack.append(name)

            # If the current name if a file name, update the max length
            # Add len(stack) -1 to the current stack length to account for foward slash between each folder/file name
            if "." in stack[-1]:
                maxL = max(maxL, curL + len(stack) - 1)

        return maxL

