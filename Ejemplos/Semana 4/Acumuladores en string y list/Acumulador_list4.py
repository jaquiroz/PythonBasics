# Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.

numbs = [5, 10, 15, 20, 25]
n=len(numbs)
for i in range(n):
    numbs[i]+=5

print(numbs)