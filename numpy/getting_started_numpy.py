# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# #numpy
# #NUMERICAL PYTHON
# this is a pyhton library for working with arrays 
# it has functions for working with linear algebra ,fourier transfformation and martrices 
# 

# %%
import numpy
arr=numpy.array([1,2,3,4,5])#syntax for an array
print(arr)


# %%
#you can import it with an alias name '
import numpy as np
arr=np.array([1,2,3,4])
print(arr)


# %%
#checking for the version
import numpy as n
print("ths is version",n.__version__)


# %%
'''
the array object in numpy is called ndarray
the ndarray can be created using the array()->function
-to create an ndarray we can pass in a tuple ,list or array like object
'''
import numpy as n 
arr_list=n.array([1,2,3,4,5])
arr_tuple=n.array((1,2,3,4,5))
print(arr_list)
print(arr_tuple)
print(type(arr))

# %% [markdown]
# 
# %% [markdown]
# DIMENISONS 
#     A dimension array is one level of array depth 
#     nested array are array that have arrays in there elements 
#     

# %%
#0-Darrays
import numpy as np
arr=np.array(42)
print(arr)


# %%
#1-Darrays
#2-Darray
#3-Darray
import numpy as np
arr=np.array([1,2,3,4])
arr_2=np.array([[1,2,3],[4,5,6]])
arr_3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
#checking for the dimensions
#use the ndim attribute that returns an int that tells as how many dimensions we are working with
print(arr.ndim)
print(arr_2.ndim)
print(arr_3.ndim)
#Higher dimension arrays 
#an array can have any number of dimensions 
#wecan create an array of 5 dimensions 
import numpy as np
arr_higher=np.array([1,2,3,4,5],ndmin=5)
#just initilize ndim with a value which is your dimension
#difine the number if dimensions with ndmin argument 
print(arr)


# %%
#acccessing array elements 
'''
the values in the array can be accessed using indexing 
access the value by reffering to  its index 
the index in nupy start with index zero

'''
arr=np.array([1,2,3,4])
print(arr[0],arr[1],arr[2],arr[3])#one dim arrays 
arr_2=np.array([[1,2,3],[4,5,6]])
print(arr_2[0],arr_2[1],arr_2[0,0],arr_2[0,1],arr_2[0,2],arr_2[1,0],arr_2[1,1],arr_2[1,2])#two dim array 
arr_3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr_3[0],arr_3[1],arr_3[0,0,2])


# %%
#SLICING
'''SLICING IN PYTHON MEANS TAKING AN ELEMENT 
    FORM ONE GIVEN INDEX TO ANOTHER GIVEN INDEX 
    [START:STOP] OR [START:STOP:STEP]

'''
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[1:5])#gets values from  index one to 5
print(arr[1:])#form index 1 to the end of the list
print(arr[4:])
print(arr[:4])#form the start of the list to the end 
#negative slicing 
print(arr[-3:-1])
#step
print(arr[::2])
print(arr[2::2])


# %%
#SLICING 2D ARRAYS
'''
syntax{
    arr[element,start:stop:step]
            or
    arr[start:stop:step , start:stop:step]        
}
'''
import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
print(arr[0,1:4])
print(arr[1,0:])
print(arr[0:2 ,0:2])


# %%
'''
datatypes in python
strings -text data 
integers ->int nmbers 
float->real numbers 
booloean->true false
complex ->complex numbers 
i integer
b boolean
u unsigned integer
f float
c comlex float 
m timedelta 
M datetime
O object 
S string
U unicode string 
V fixed chunk of memeory for other type void 


'''
import numpy as np 
arr=np.array([1,2,3,4] ,dtype="int32")
#dtype can be sued to specify the type of int 
arr_two=np.array(["banan","mango"])
print(arr_two.dtype)
print(arr.dtype)


# %%



