#Python Collections (SIMILAR TO ARRAY)
# LIST, TUPLE, SET, DICTIONARY
#python Lists
#Lists are used to store the multiple data in a single variable
#use square brackets
#Python lists are ordereed
# Lists are allow duplicates
# list can store different different data types
studet_name_1= ["Samatha",100,True, "Chamoda","Isini","Rishi"]
studet_name_2= ["Rishi","Sandun"]
print(studet_name_1)
print(type(studet_name_1))
# for i in studet_name:
#     print(i)
#Call indexes seperately 
print(studet_name_1[0])
print(studet_name_1[1])
print(studet_name_1[2])
print(studet_name_1[3])
print(studet_name_1[-1])
print(len(studet_name_1))   #Actual number of elements
new_list = studet_name_1[1:4]
print(new_list)
#Exercise 01
new_list_2 = studet_name_1[3:5]
print(new_list_2)
#Exercise 02
new_list_3 = studet_name_1[:3] # 0,1,2 
print(new_list_3)
#Exercise 03
new_list_4 = studet_name_1[2:] #2,3,4,5
print(new_list_4)
# Change Element in the array
studet_name_1[1:3] =["Kalani","Vithushan"]
print(studet_name_1)
#Exersise
studet_name_1[3:] =[200,300,400]
print(studet_name_1)
#Add element
# studet_name.append("Sanjaya")
# print(studet_name)
#Add element location we want(Arbitary location)
# studet_name.insert(2,"Sanjaya")
# print(studet_name)

studet_name_1.insert(0,"Sanjaya")
print(studet_name_1)

#Add two arrays

#samantha, chamoda,ishini, rishi ,sandun

#remove 
studet_name_1.remove("Kalani")
print(studet_name_1)

#Another mETHOD
del studet_name_1[2]
print(studet_name_1)

# clear command output []
#delete command delete whole array

studet_name_1.clear()

#Sort List
#alphabetical order(acending order)
my_list = ["banana","apple","carrot", "orange"]
# my_list_2 = [100,"banana","apple",99,78] -# error we cant sort different type datatypes
my_list_3 =["1carrot", "banana", "2apple"]
my_list.sort()
my_list_3.sort()
# my_list_2.sort() #decending order
# print(my_list_2)
print(my_list_3)

my_list_4 =["dog", "cat", "Lion","Rat","fish"]

my_list_4.sort(key=str.lower) #ignore the whether it is capital or not
print(my_list_4)
my_list_5 =["dog", "cat", "lion"]
my_list_6 =[]
my_list_6 = my_list_5
# my_list_6 = my_list_5.copy() # make a exact copy of the list
my_list_5.append("deer")
my_list_6.append("monkey")
print(my_list_5)
print(my_list_6)

