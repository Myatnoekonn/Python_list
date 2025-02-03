# Filter out even numbers and then square them

result1 = list(map( lambda e: e**2  , filter( lambda num: num%2==0, [1, 2, 3,4,5, 6,7,8,9,10]) )   )
print(result1)

# square all numbers and filter out even
result2 = list(filter( lambda num: num%2==0 , map( lambda num: num**2 ,  [1, 2, 3,4,5, 6,7,8,9,10]  ) )   )
print(result2)