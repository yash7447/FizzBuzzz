#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fizzbuzz(n):
# Define the strings to use for replacement
    fizz_replace = "Dog"
    buzz_replace = "Shelter"

    """
    Print the numbers from 1 to n, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    """
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(fizz_replace + buzz_replace)
        elif i % 3 == 0:
            print(fizz_replace)
        elif i % 5 == 0:
            print(buzz_replace)
        else:
            print(i)


# In[3]:


fizzbuzz(100)

