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

print("----------------------------------------------------")

while (len(indexes)):
    starttime = time()
    rint = randint(0, len(indexes)-1)
    print("\n")
    print(f"Question {indexes[rint] + 1}: {questions[indexes[rint]]}")
    anscond = input("Did you know the answer (1/0)?: ")
    try:
        if anscond == "answered":
            print(answeredlist)
        else:
            anscondint = int(anscond)
    except:
        anscondint = 0

    if anscondint:
        anscondint = 1
    else:
        anscondint = 0

    scorelist = np.append(scorelist, anscondint)

    if anscondint:
        print("You answered the question correctly.")
        answered = indexes.pop(rint)
        answeredlist.append(answered + 1)
        answeredlist.sort()
    else:
        print("You answered the question wrong.")
    endtime = time()
    print(f"\nSpent time on current question: {(endtime-starttime)/60:.2f} minutes.")
    print(f"Current time of studying: {(time() - starttime)/60:.2f} minutes.")
    print(f"Current progress: {len(answeredlist)}/{len(questions)} ({(len(answeredlist)/len(questions))*100:.2f} %).")
    print(f"Current score: {np.average(scorelist)*100:.2f} %.")
    print("\n")
    print("----------------------------------------------------")


#session results
print("\n\n\n\n\nYour study session results")
print(f"Overall time: {(time() - starttime)/60:.2f} minutes.")
print(f"Overall score: {np.average(scorelist)*100:.2f} %")
print(f"Questions answered: {len(answeredlist)}\n\n\n\n\n")
print("----------------------------------------------------")

#waits until enter is pressed
input("Press enter to exit...")