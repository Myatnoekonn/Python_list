# Square all numbers  
# 8 num => 8 square  => 8**2 
# square_list = list()
# #Normal function
# def square_num(numbers):
#     for i in numbers:
#        pow = i**2
#        square_list.append(pow)
#     return square_list
       
# sq = square_num([ 3, 5, 7, 10, 12])
# print(sq)

#lambda function
sq = list(map(    lambda i: i**2      ,   [3, 5, 7, 10, 12]   ))
print(sq)