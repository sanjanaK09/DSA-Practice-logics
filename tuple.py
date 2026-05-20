# mytuple = ("prashant", "Ashish","Rahul","Sandeep","komal","ankush","rajesh", 23,3.15,77, "sandeep")

# print(mytuple)
# print(type(mytuple))

# # mytuple[2]="sunil" #immutable
# # print(mytuple)


# init_tuple = ()
# print(init_tuple.__len__())
##OUTPUT--->0 as there is no value inserted ,the brackets are empty ,it is by default 0

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a ==init_tuple_b)
##values can be given inside parenthises or can also be given without parenthises


# init_tuple_a='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a + init_tuple_b)
## will simply add both the elements

# l=[1,2,3]
# init_tuple = ('Python',) * (l.__len__()- l[::-1][0])
# print(init_tuple)



# init_tuple = ('Python') * 3. ###('Python', --->class tuple) ('Python'--->class str)
# print(type(init_tuple))



# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)
# ##TypeError: 'tuple' object does not support item assignment



# init_tuple = ((1,2),)*7
# print(init_tuple)
# ###((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))
# print(len(init_tuple[3:8]))
# ###4