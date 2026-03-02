# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):

    f1 = open(file1, "r")
    list1 = f1.readlines()
    f1.close()

    f2 = open(file2, "r")
    list2 = f2.readlines()
    f2.close()
    sorted_names = sorted(names)

    names = []
    for name in list1:
        names.append(name.strip())
        
    for name in list2 :
        names.append(name.strip())

    unique_names =sorted(set(names))
    
    f3 = open(output_file, "w")
    for name in unique_names:
        f3.write(name + "\n")
    f3.close()

    return len(unique_names)
    
   
# Test your code here
result = merge_lists("data/list1.txt", "data/list2.txt", "data/merged.txt")
print(f"Unique names: {result}")
