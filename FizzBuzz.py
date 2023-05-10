#!/usr/bin/env python
# coding: utf-8

# In[2]:

class MyFizzBuzz:
    def __init__(self, n):
        self.n = n

    def fizzbuzz(self):
# Define the strings to use for replacement
        fizz_replace = "Dog"
        buzz_replace = "Shelter"

        """
    Print the numbers from 1 to n, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                print(fizz_replace + buzz_replace)
            elif i % 3 == 0:
                print(fizz_replace)
            elif i % 5 == 0:
                print(buzz_replace)
            else:
                print(i)

    def fizzbuzzseven(self):
            fizz_replace = "Dog"
            buzz_replace = "Shelter"

            """
        Print the numbers from 1 to n, replacing multiples of 5 with "Dog",
        multiples of 7 with "Shelter", and multiples of both with "DogShelter".
            """
            for i in range(1, self.n+1):
                if i % 5 == 0 and i % 7 == 0:
                    print(fizz_replace + buzz_replace)
                elif i % 5 == 0:
                    print(fizz_replace)
                elif i % 7 == 0:
                    print(buzz_replace)
                else:
                    print(i)
# In[3]:

fb = MyFizzBuzz(100)
fb.fizzbuzzseven()


# %%
