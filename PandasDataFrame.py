import pandas as pd

# whenever you make a data frame from a dictionary, the keys become the columns (/column indexes) 
# and the values become the rows 

grades_dict = { 'Wally': [87,96,70],
                'Eva': [100, 87,90],
                'Sam': [94,77,90],
                'Katie': [100,81,82],
                'Bob': [83,65,85]}

# kind of like an excel spreadsheet

grades = pd.DataFrame(grades_dict)

# this will label the index so that way it doesn't just print the index number, instead it will have the Test #

grades.index = ['Test1','Test2','Test3']

print(grades)
#this will transpose(T) the view to make the student's names rows and the test scores as columns
#print(grades.T)
# each column from this data set is a series, called a "panda series"

#print(grades['Eva'])
#print(grades.Sam)

# using the loc and iloc methods
# can print from the calling the index that we made previously, upperbound INCLUDED
print(grades.loc['Test2'])

#iloc means integer lock, upperbound NOT INCLUDED
print(grades.iloc[1])

# for consecutive rows
print(grades.loc['Test1':'Test3'])
print(grades.iloc[0:3])

# for non - consecutive rows
print(grades.loc[['Test1','Test3']])
print(grades.iloc[[0,2]])

# view only Eva's and Katie's grades for Test1 and Test2
print(grades.loc['Test1':'Test2',['Eva','Katie']])

#view only Sam's THRU Bob's grades for Test1 and Test3
print(grades.loc[['Test1','Test3'],'Sam':'Bob'])

#NaN means Not a Number
# select everyone with an A grade
grades_A = grades[grades>=90]

print(grades_A)

#create a dataframe for everyone with a B grade
#to use an 'and' in a data frame, use '&'
grades_B = [(grades>=80) & (grades<90)]

print(grades_B)

# when using ands and ors we get back the ones that pass and don't pass

# create a dataframe for everyone with an A or B grade
# | this key creates an 'or'

grades_A_or_B = [(grades>=90) | (grades>=80)]

print(grades_A_or_B)

pd.set_option('precision',2)
print(grades.T.describe())

#sort_index, everything will change based on this order
print(grades.sort_index(ascending=False))

#for alphabetical order
print(grades.sort_index(axis=1, ascending=False))

#want to sort by Test1 by columns in descending order, in case of a tie, does it alphabetically
print(grades.sort_values(by='Test1',axis=1,ascending=False))
#flip the chart so the students are listed in descending order
print(grades.T.sort_values(by='Test1', ascending=False))

# to only see Test1 and not 2 and 3

print(grades.loc['Test1'].sort_values(ascending=False))