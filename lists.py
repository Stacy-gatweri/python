# 1. Create an empty list
my_list = []

#2.Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#3. Insert 15 at the second position 
my_list.insert(1, 15)
# print(my_list)

#4. Extend the list with another list[50, 60, 70]
my_otherlist = [50, 60, 70]
my_list.extend (my_otherlist)
# print(my_list)

# 5.Remove the last element
my_list.pop()
#print(my_list)

# 6.Sort the list in ascending order
my_list.sort()
#print(my_list)

# 7.Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

