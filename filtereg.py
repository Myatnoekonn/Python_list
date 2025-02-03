numbers = [1,2,3,4,5,6,7,8,10]

# even_numbers = []
# #Normal function
# def even_number(numbers):
#     for i in numbers:
#         if(i % 2 == 0):
#             even_numbers.append(i)

# print(even_numbers(numbers))

#filter function =>[]

even_numbers = list(filter(  lambda i: i%2==0, numbers ))
print(even_numbers)