# addition_str is a string with a list of numbers separated by the + sign. 
# Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns
#  it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

addition_str = "2+5+10+20"
sum_val=0
aux=addition_str.split('+')
for sm in aux:
    i=int(sm)
    sum_val=sum_val+i
    
print(sum_val)