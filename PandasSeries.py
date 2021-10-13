import pandas as pd

grades = pd.Series([87,100,94])


grades2 = pd.Series(98.6, range(3))

#print(grades2)

#print(grades[0])

#print(grades.describe()) #this prints avg, std dev, min, max, lots of different things w the describe method

#custom indexing for our values, we can use string indexing here which is something we can't do in numpy 
grades = pd.Series([87,100,94], index = ['Wally','Eva','Sam'])
#Series is case sensitive, must use uppercase 'S'
#print(grades)

grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam':94})

#print(grades)
#when you make it a dictionary, the keys become the index values and the values of the array, Wally, Eva and Sam became the
#corresponding indexes in our series

#print(grades['Eva'])
# can aslo use dot notation. The indexes become attributes of the object which is why we can do this
#print(grades.Wally)

#tells us the data type of grades
#print(grades.dtype)
#using type helps us to see that it's not a list, it's a numpy array
#print(type(grades.values))

hardware = pd.Series(['Hammer','Saw','Wrench'])

#boolean that shows whether the contains is true or false
print(hardware.str.contains('a'))

# changes it to upper case
print(hardware.str.upper())

