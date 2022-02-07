i = 1
sum = 0
while i <= 10:
   if i%2 == 0:
      sum = sum + i
   i = i+1

print(sum)

# breakdown of the above code

'''sum = sum + i
    0  =  0  + 1 --> here if condition false 
    0  =  0  + 2 --> here if condition true sum become 2
    2  =  2  + 3 --> here if condition false
    2  =  2  + 4 --> here if condition true sum become 6
    6  =  6  + 5 --> here if condition false
    6  =  6  + 6 --> here if condition true sum become 12
    12 =  12 + 7 --> here if condition false
    12 =  12 + 8 --> here if condition true sum become 20
    20 =  20 + 9 --> here if condition false
    20 =  20 + 10--> here if condition true sum become 30
    30 ---------->''' # this will be the final output of the above code
   
''''best way to understand any code and to accelerate your logical building  
skill is to sub divide the code'''