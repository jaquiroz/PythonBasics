# Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. 
# Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
i=len(words)
past_tense=[None]*i
j=0
for j in range(i):
    n=len(words[j])
    a=words[j]
    spl=a[(n-1):]
    #past_tense[j]=spl

    if spl=='e':
        past_tense[j]=words[j]+'d'
    else:
        past_tense[j]=words[j]+'ed'

print(past_tense)
        

    