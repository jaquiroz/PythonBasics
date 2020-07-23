# Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. 
# Only the first letter of each word should be used, each letter in the acronym should be a capital letter, 
# and there should be nothing to separate the letters of the acronym. 
# Words that should not be included in the acronym are stored in the list stopwords. 
# For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
aux=org.split()
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
    x=x+w[0]
  
acro=x.upper()

print(acro)
