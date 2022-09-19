"""
    Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

    A group of duplicate files consists of at least two files that have the same content.

    A single directory info string in the input list has the following format:

    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
    It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

    The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

    "directory_path/file_name.txt"
    
    Example 1:
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    
    Example 2:
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Solution:
    Split each path into the root, filenames, and contents. Use contents as keys and add each filepath (root + filename) into a dictionary. Return all groups of filepaths that contain at least 2 filepaths. 

    Follow up:
    1. Imagine you are given a real file system, how will you search files? DFS or BFS? 
    Ans: For a real file system, we will traverse it using DFS.

    2. If the file content is very large (GB level), how will you modify your solution?
    Ans: If the file content is very large, we should hash the file content before using it as a key for the dictionary. MD5 is a good hash algorithm for such purpose (DO NOT USE MD5 FOR CRYPTOGRAPHIC PURPOSE).

    3. If you can only read the file by 1kb each time, how will you modify your solution?
    Ans: If we are only able to read file 1kb each time, we should read file asynchronously as a stream. 

    4. What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
    Ans: Running time of the modified alogrithm is O(kmn) where k is the number of files, m is longest path in the directory tree, and n is cost of reading and hashing each file content. Since hashcodes has a fix size, accessing dictionary should still be constant time. The most consuming part of the modified algorithm is most likely reading and hashing file contents. 

    5. How to make sure the duplicated files you find are not false positive? 
    Ans: The chance of two different files generating the same hashcode are very rare. 


Complexity:
    Time: O(kmn) where 
        k is the number of paths, 
        m is the number of file, 
        n is th length of the longest path (cost of string splitting)
    Space: O(kn)
"""

from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:

        # Dictionary to store filepaths using content as the key
        group = defaultdict(list)

        # Iterate through all paths
        for path in paths:

            # Split the current path into the root and files
            p = path.split(" ")

            root = p[0]

            # For each files,
            for f in p[1:]:

                # Split the current file into a filename and a content
                fName, content = f.split("(")

                # Add filepath to the dictionary
                group[content[:-1]].append(f"{root}/{fName}")

        # Return groups of filespaths that contain at least 2 filepaths
        return [value for value in group.values() if len(value) > 1]
