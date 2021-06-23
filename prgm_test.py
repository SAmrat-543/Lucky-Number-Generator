#from sys import stdout
import time
from random import randint
print(" LUCKY NUMBER GENERATOR ".center(120, "*"))
a = input("Enter Your Age = ")
a = int(a)
print(" Please Wait ".center(120, '.'))
x = int(1)
print(" Calculating ".center(120, '-'))
for x in range(101):
    time.sleep(randint(5, 10) / 101)
    print("\r", "{} %".center(118, ' ').format(x), flush=True, end="")
print("\n", " Completed ".center(120, " "))
print(" Your Lucky Number is {} ".format(a % randint(1, a-1)).center(120, "#"))
print("\nTimestamp :\n{}".format(time.asctime(time.localtime(time.time()))))
print("\n", "Press Enter to Exit".center(120, " "))
input()
