#imports
from random import randint
from time import time
import numpy as np


#definitions
answeredlist = []
starttime = time()
scorelist = np.array(())

#core
filename = input("File name (without a .txt extension): ")
file = open(filename + ".txt", "r")
questions = file.readlines()
indexes = list(range(len(questions)))

while (len(indexes)):
    rint = randint(0, len(indexes)-1)
    print(f"Question {indexes[rint] + 1}: {questions[indexes[rint]]}")
    anscond = input("Did you know the answer (1/0): ")
    try:
        if anscond == "answered":
            print(answeredlist)
        else:
            anscondint = int(anscond)
    except:
        anscondint = 0

    scorelist = np.append(scorelist, anscondint)
    if anscondint:
        print("You answered the question correctly.")
        answered = indexes.pop(rint)
        answeredlist.append(answered + 1)
        answeredlist.sort()
    else:
        print("You answered the question wrong.")
    print(f"\nCurrent time of studying: {(time() - starttime)/60:.2f} minutes.")
    print(f"Current score: {np.average(scorelist)*100:.2f} %")
    print("----------------------------------------------------")


#session results
print("\n\n\n\n\nYour study session results")
print(f"Overall time: {(time() - starttime)/60:.2f} minutes.")
print(f"Overall score: {np.average(scorelist)*100:.2f} %\n\n\n\n\n")
print("----------------------------------------------------")