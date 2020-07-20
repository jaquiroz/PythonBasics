# Create an empty list called resps. Using the list percent_rain, for each percent, 
# if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, 
# add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, 
# add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. 
# Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
n=len(percent_rain)
resps=[None]*(n)
for i in range(n):
    if percent_rain[i]>90:
        resps[i] = "Bring an umbrella."
    elif percent_rain[i]>80:
        resps[i] = "Good for the flowers?"
    elif percent_rain[i] >50:
        resps[i]= "Watch out for clouds!"
    else:
        resps[i] = "Nice day!"

print(resps)
