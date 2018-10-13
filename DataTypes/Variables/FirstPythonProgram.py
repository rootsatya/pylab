#!/bin/usr/python

#In this program we will learn about Shebang Value, Comments, Variables, Print  and functions

#Comments Section
#Comments can be created with #Sometext,'Sometext','''Sometext''',"""Sometext"""
print("Variables and Printing")

#1st Comments Section
"This is a 1st comment"
FirstName="Guido"
MiddleName="Van"
LastName="Rossum"
Title="Python Creator"

#Accessing Variables
print(FirstName)
print(MiddleName)
print(LastName)
print ("is")
print(Title)

#2nd Python Program
print('2nd Program')
firstname='Guido'
middlename="Van"
lastname='Rossum'
title="Python Creator"

#Accessing Variables
print('')
print(firstname)
print(middlename)
print(lastname)
print('is')
print(title)
print('')


#3rd Program
Country='India'
State="Karnataka"
City='''Bangalore'''
Area= 'Whitefield'
Pincode="""560066"""

#Accessing Veriables
print('Country : ',Country)
print('State : ',State)
print("City : ",City)
print("Area : ",Area)
print('Pincode : ',Pincode)
#Printing all variables in single line with single print function
print(Country,type(Country),id(Country), State,type(State),id(State),City,type(City),id(City),Area,type(Area),id(Area),Pincode,type(Pincode),id(Pincode))

#4th Program
Movie='AntMan'
Director = '''Peyton Reed'''
Producer = "Joe Cornish"
Story = """Edgar Wright"""
Music="""Chris Beck"""

#Accessing Variables
print(Movie,Director,Producer,Story,Music)

#5th Program
print("5th Program")
"""This is multi line comment for 5th program and next line
starts for the sake of multiline"""
Language = 'Python 3.6'
OS = '''Windows 7 Ent'''
Text_Editor = "Sublime"
IDLE = """PyCharm"""

print(IDLE,Text_Editor,OS,Language)
print(id(OS),id(Language),id(Text_Editor),id(IDLE))
print(type(OS),type(Language),type(Text_Editor),type(IDLE))

'''End of the Program'''
