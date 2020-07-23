# A palindrome is a phrase that, if reversed, would read the exact same. 
# Write code that checks if p_phrase is a palindrome by reversing it and then 
# checking if the reversed version is equal to the original. Assign the reversed version of p_phrase 
# to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
n=len(p_phrase)
print(n)
r_phrase=""
i=0
j=n-1
for i in range(n):
    a=p_phrase[j]
    r_phrase=r_phrase+a
    j=j-1

print(r_phrase)
  




