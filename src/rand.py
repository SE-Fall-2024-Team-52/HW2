"""
This module provides a function to generate a random array using shell commands.
"""
import subprocess


def random_array(arr):
    """
    Fills an array with random integers generated using the `shuf` shell command.

    Parameters:
    input_arr (list): The list to be populated with random integers.

    Returns:
    list: The list populated with random integers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
