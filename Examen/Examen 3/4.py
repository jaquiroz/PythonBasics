# Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
#Note 1: be sure to not double-count words that contain both an a and an e.
#HINT 1: Use the in operator.
#HINT 2: You can either use or or elif.

#Hard-coded answers will receive no credit.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
x = sentence.split(' ')
n= len(x)
num_a_or_e=0
i=0
for i in range(n):
    if 'a' in x[i]:
        num_a_or_e+=1
    elif 'e' in x[i]:
        num_a_or_e+=1

print(num_a_or_e)

