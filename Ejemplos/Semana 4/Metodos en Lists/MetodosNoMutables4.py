#There can be multiple substitutions, with data of any type. Next we use floats. Try original price $2.50 with a 7% discount:

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
#calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice) #.2f permite utilizar dos decimales

print(calculation)


