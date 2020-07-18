#Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").

n=7
lett=" "
aux=""
for s in range(n):
    aux=aux+"b"
lett=aux
print(lett)
