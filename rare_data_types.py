#Complex
#Complex Computations
cmplx = complex(1j)
print(cmplx)
print(type(cmplx))
print("**********************************************")

#List
#Mutable, Changeable, Ordered Sequence, Multiple Items in a single Variable
fruits_list = list(("dare", "funmi", "neeya", "funmi"))
print(fruits_list)
print(type(fruits_list))
print("**********************************************")

#Tuple
#Collection of Objects which are ordered and immutable
fruits = tuple(("dare", "funmi", "neeya", "funmi"))
print(fruits)
print(type(fruits))
print("**********************************************")

#Range
#A sequence of numbers starting from 0 and ends just before the specified number, increasing by 1 by default
rng = range(6)
print(rng)
print(type(rng))
print("**********************************************")

#Set
#Unordered Collection of unique data that are iterable and mutable 
my_set = {"abdul", "toyeeeb", "fadio", "fadio"}
print(my_set)
print(type(my_set))
print("**********************************************")

#Frozen Set
#Immutable version of sets, cant change values, iterable
my_frzn_st = frozenset({"dsa", "cybersecurity", "blockchain"})
print(my_frzn_st)
print(type(my_frzn_st))
print("**********************************************")

#Boolean
#True or false in python, any value other than 0 will give true
my_bool = bool(9)
print(my_bool)
print(type(my_bool))
print("**********************************************")

#Byte
#Converting to an immutable byte representation of a given data
my_byte = b"Hack"
print(my_byte)
print(type(my_byte))
print("**********************************************")

#Byte Array
#A mutable byte object
my_byte_array = bytearray(7)
print(my_byte_array)
print(type(my_byte_array))
print("**********************************************")

#Memory View
#To show the internal data of an object. Supports buffer protocol. Yield large performance gains
my_mem_view = memoryview(bytes(8))
print(my_mem_view)
print(type(my_mem_view))
print("**********************************************")
