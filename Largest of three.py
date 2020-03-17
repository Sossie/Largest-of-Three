# Python program to find the largest 
# number among the three numbers 
  
def maximum(a, b, c): 
  
    if (a >= b) and (a >= b): 
        largest = a 
  
    elif (b >= a) and (b >= a): 
        largest = b 
    else: 
        largest = c 
          
    return largest 
a = input("Input value of a ") 
b = input("Input value of b ") 
c = input("Input value of c ")

print(maximum(a, b, c))