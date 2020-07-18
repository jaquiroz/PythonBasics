# Write code to create a list of word lengths for the words in original_str using the accumulation pattern 
# and assign the answer to a variable num_words_list. (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"
aux=original_str.split(' ')
n=len(aux)
print(n)
num_words_list=[None]*(n)

for s in range (n):
    num_words_list[s]=len(aux[s])
   
print(num_words_list)