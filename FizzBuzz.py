#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fizzbuzz(n):
    """
    Print the numbers from 1 to n, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    """
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# In[3]:


fizzbuzz(100)

