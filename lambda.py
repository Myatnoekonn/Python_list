# Normal function to add 10 to a number
num = 5

#1. function definition
def add_ten():
    result = num + 10
    print("Result ", result)


#2.function call
add_ten()

#function with a parameter(argument)
def add_ten(num):
    result = num + 10
    print("Result ", result)

add_ten(15)

#lambda function 
# lambda arguments: expression
result = lambda num: num + 10

print("Result ",result(20))