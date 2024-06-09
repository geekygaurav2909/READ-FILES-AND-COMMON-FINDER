with open("file1.txt", "r") as file1:
    file1_list = [int(num) for num in file1]

with open("file2.txt", "r") as file2:
    file2_list = [int(num) for num in file2]

    
print(file1_list)
print(file2_list)

result = [num for num in file1_list if num in file2_list]
print(result)