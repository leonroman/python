# This code demonstrates the use of indentation in Python.
# Indentation is crucial in Python as it defines the blocks of code.
# Here we have an output loop that prints "Hello" and the value of i 2 times.
print ("First loop starts now")
for i in range(2):
    print ("Hello")
    print("Value of i is:", i)

print ("Second loop starts now")
# Here we have another loop that prints "Hi" 2 times and only once the last value of i (the last iteration).
for i in range(2):
    print ("Hi")
print("Value of i is:", i)



# $ python day1/indentation.py 
# First loop starts now
# Hello
# Value of i is: 0
# Hello
# Value of i is: 1
# Second loop starts now
# Hi
# Hi
# Value of i is: 1