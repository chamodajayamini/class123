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
print(studet_name)
print(type(studet_name))
# for i in studet_name:
#     print(i)
#Call indexes seperately 
print(studet_name[0])
print(studet_name[1])
print(studet_name[2])
print(studet_name[3])
print(studet_name[-1])
print(len(studet_name))   #Actual number of elements
new_list = studet_name[1:4]
print(new_list)
#Exercise 01
new_list_2 = studet_name[3:5]
print(new_list_2)
#Exercise 02
new_list_3 = studet_name[:3] # 0,1,2 
print(new_list_3)
#Exercise 03
new_list_4 = studet_name[2:] #2,3,4,5
print(new_list_4)
# Change Element in the array
studet_name[1:3] =["Kalani","Vithushan"]
print(studet_name)
#Exersise
studet_name[3:] =[200,300,400]
print(studet_name)
#Add element
# studet_name.append("Sanjaya")
# print(studet_name)
#Add element location we want(Arbitary location)
# studet_name.insert(2,"Sanjaya")
# print(studet_name)

studet_name.insert(0,"Sanjaya")
print(studet_name)
