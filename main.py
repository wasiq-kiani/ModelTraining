# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("I am writing this for the first time")
    print("hi,",name)
    print(np.__version__)
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
#   Reshapeing the array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr = arr.reshape(3,4)
print(arr.shape)
print(arr)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

arr1 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
print(arr1.shape)
print(arr1)