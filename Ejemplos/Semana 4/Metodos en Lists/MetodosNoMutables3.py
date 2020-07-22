scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    #El metodo format sustituye los valores de los corchetes con los valores asociados respectivamente
    print("Hello {}. Your score is {}.".format(name, score))
