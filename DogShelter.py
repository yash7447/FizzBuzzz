class MyFizzBuzz:
    def __init__(self, n):
        self.n = n
        
    def fizzbuzz(self):
        fizz_replace = "Fizz"
        buzz_replace = "Buzz"

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
				
				
class MyNewFizzBuzz(MyFizzBuzz):
    def fizzbuzz(self):
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


my_new_fizzbuzz = MyNewFizzBuzz(100)
# Call the fizzbuzz method on the my_new_fizzbuzz object
my_new_fizzbuzz.fizzbuzz()          

                   

