#!/usr/bin/python3
"""Module for minOperations(n)
"""

def minOperations(n):    
    """Determines the minimum number of operations required
    to transform a text file with one character to a text
    file with n characters.
    Only two operations can be carried out,
    copy all, which copies the text in the file to clipboard
    paste, which pastes text from the clipboard to the textfile

    args: n
    returns: int

    ex: minOperations(9) -> 6
    """
    # If n is a string, try to parse into int
    if isinstance(n, str):
        try:
            n = int(n)
        except:
            return 0

    # If n is a float, try to convert into int
    if isinstance(n, float):
        if int(n) == n:
            n = int(n)
        else:
            return 0

    # If n is int, proceed with the algorithm
    if isinstance(n, int):
        n_operations = 0
        text_file = "H"
        clipboard = ""

        # Function to simulate copying from text file to clipboard
        def copy_all():
            nonlocal clipboard
            clipboard = text_file

        # Function to simulate pasting from clipboard to file
        def paste():
            nonlocal text_file
            text_file += clipboard

        # Function to determine if we should copy and paste or just paste
        def should_copy_all():

            # Spaces that need filling
            remaining_spaces = n - len(text_file)

            # Length of clipboard after copying
            clipboard_len_after_copy = len(text_file)

            # Spaces that need filling divided by length of clipboard after copy
            ratio = remaining_spaces / clipboard_len_after_copy

            # If the ratio is a whole number, we can copy, so function returns true
            return int(ratio) == ratio

        while len(text_file) < n:
            if should_copy_all():
                copy_all()
                n_operations += 1

            paste()
            n_operations += 1

        return n_operations
    else:
        return 0
