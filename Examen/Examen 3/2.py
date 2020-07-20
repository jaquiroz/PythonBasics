# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, 
# including one-letter words. Store the result in the variable same_letter_count.

#Hard-coded answers will receive no credit.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
x = sentence.split(' ')
n=len(x)
same_letter_count=0
i=0
for i in range(n):
    aux=len(x[i])
    a=x[i]
    spl_1=a[:1]
    spl_2=a[(aux-1):]
    if spl_1 == spl_2:
        same_letter_count+=1
#print(spl_1)
#print(spl_2)
print(same_letter_count)