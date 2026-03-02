# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    names = set()

    f1 = open(file1, "r")
    for line in f1:
        names.add(line.strip())
    f1.close()

    f2 = open(file2, "r")
    for line in f2:
        names.add(line.strip())
    f2.close()
    sorted_names = sorted(names)

    out = open(output_file, "w")
    for i in sorted_names:
        out.write(name + "\n")
    out.close()

    return len(sorted_names)
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    pass


# Test your code here
result = merge_lists("data/list1.txt", "data/list2.txt", "data/merged.txt")
print(f"Unique names: {result}")
