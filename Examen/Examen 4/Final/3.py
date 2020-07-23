# Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. 
# The first two letters of each word should be used, each letter in the acronym should be a capital letter, 
# and each element of the acronym should be separated by a “. ” (dot and space). 
# Words that should not be included in the acronym are stored in the list stopwords. 
# For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
#sent="height and ewok wonder"
aux=sent.split()
aux2=[]
aux3=[]
n=len(aux)
i=0
acro=""
x=""
for i in range(n):
    if aux[i] in stopwords:
       print(aux[i]) 
    else:
        aux2.append(aux[i])

i=0
for w in aux2:
    x=x+w[0]+w[1]+'. '
  
acro=x.upper()

print(acro)
