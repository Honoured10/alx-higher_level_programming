#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Convert the arguments to integers
    arguments = [int(arg) for arg in sys.argv[1:]]

    # Print the sum of the arguments
    print(f"Sum of arguments: {sum(arguments)}")
