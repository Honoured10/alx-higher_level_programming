# Import the hidden_4 module
import hidden_4

if __name__ == "__main__":
    # Get the names defined by the module
    names = dir(hidden_4)

    # Filter out names that start with __
    names = [name for name in names if not name.startswith("__")]

    # Sort the names alphabetically
    names.sort()

    # Print the names
    for name in names:
        print(name)
