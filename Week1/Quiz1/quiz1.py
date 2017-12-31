import numpy as np
import matplotlib.pyplot as plt
import __future__
import pickle


#1.Which matrix corresponds to the following code?

A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
print(f'\n A = {A}')

#2. Given the 2D array (i.e., matrix) A=[[1,2,3,4],[2,3,4,5],[3,4,5,6]],
# which of the following expressions generates B=[[2,3,4], [4,5,6]]

A = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])

B = A[[0,2],1:]
print(f'\nB = {B}')

# 3. Suppose you have a script that contains the line
 #    A = np.array([1, 2, 3])
# but when you run it, the following error occurs:

'''
    Traceback (most recent call last):
      File "&lt;stdin&gt;", line 1, in &lt;module&gt;
    NameError: name 'np' is not defined
'''

    #How do you correct it

'''
    Answer: Insert the following at the start of your script:
        import numpy as np 
 '''

# 4. Given that numpy is imported as np, and that you have
# defined the one-dimensional array a=[1234],  which of the following commands
# will not raise an error? Check all that apply.
a= np.array([1,2,3,4])

b = np.ones(5, )
print(b)

# Gives error
#b = np.ones(5,5)

#Gives error
#b = a[:2, :2]

b = a[4:]

#Gives error
#b = a[4]

b = a[:5]

b = np.ones((5,5))
print(b)

b= b[:2]
print(b)

# 5. Which piece of code generates an array x of 100 random numbers between 0
# and 1?

x = np.random.rand(100)
print(x[1:10])

# 6. Suppose x is an array of 100 random numbers between 0 and 1.
# Which piece of code sets to 1 all elements of x that are greater than 0.5?

x[x > 0.5] = 1
print(x[1:10])

# 7. Which piece of code returns the numerical indices of the first three elements
# of the one-dimensional array x that are greater than 1?

#see: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.nonzero.html
x = (x > 1).nonzero()[0][:3]
print(f'7 x = {x}')

# 8. What piece of code loads the file 'data.pickle', which contains a dict
# object, into the variable "data"? You can assume that the directory containing
#  'data.pickle' is in your path (i.e., is accessible).

# *The end result should be that the variable data is a dict object.

#Basic example:
# create dictionary containing all your data
data = {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}

# save data in pickle format
with open('my_data.pickle', 'wb') as f:
    pickle.dump(data, f)

# open data from file
with open('my_data.pickle', 'rb') as f:
    new_data_variable = pickle.load(f)

print(new_data_variable)
# now new_data_variable is equal to the dict:
# {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}

'''
Answer: 
....
pickle.load(f)
...
'''

# 9. Suppose the dict called "data" has been set to {'a': 3, 'c': 9, 'b': 5}.
# How do you set the value corresponding to the key 'b' to 100?

data = {'a': 3, 'c': 9, 'b': 5}
print(data['b'])
data['b'] = 100
print(data['b'])

# 10. Which plot results when you run the following script?


x = np.arange(0, 5, step=0.05)
y = np.sin(x**2)
plt.plot(x,y)
plt.show()

# 11. Given the array x = np.array([1,2,3,4,5]), how do you create an array y that contains the cubes of
#  all the elements of x?

x = np.array([1,2,3,4,5])
y= x**3
print(y)

# 12. What is the mathematical representation of x after this sequence
# of commands?

x = np.array([[1, 2, 3], [2, 3, 4]])
x *= 5
x -= 1
x[x > 10] = 0
x = x.T
print(x)

# 14. Which of the following pieces of code sets the value of y to True
# if the value of x is either 2, 5, or 9, and to False otherwise?
# Check all that apply.

x= 5

#Option 1:
y = x in [2, 5, 9]

#Option 2:
y = False
if x in [2, 5, 9]:
    y = True

#Option 3:
if x in [2, 5, 9]:
    y = True
else:
    y = False


# 14. What does the statement

# import pdb; pdb.set_trace()

#do when placed inside a Python script?

#E.g.,

x = np.arange(5)
y = -np.arange(5)
x[y < -2] = 0
#import pdb; pdb.set_trace()
x *= 9
print(x)

#Enter the debugger at the calling stack frame.
# This is useful to hard-code a breakpoint at a given point in a program,
# even # if the code is not otherwise being debugged
# (e.g. when an assertion fails).

#see: https://docs.python.org/2/library/pdb.html


np.ones((5,5))