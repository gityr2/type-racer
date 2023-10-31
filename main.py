import time
import os
import sys
from rgbprint import Color
import random
print(Color.white)
print("Welcome to the keyboard test. This is where you will test how fast u are")

a = input("wanna begin")
if a.lower().startswith("y"):
    print("3")
    time.sleep(1)
    print('2')
    time.sleep(1)
    print("1")
    time.sleep(1)
    
    print("GO!!!!!")
    with open("ranWord.dat", "r") as DataWord:
        DataWord = DataWord.readlines()
        RandomWords = []
        RandomWordNum = list(DataWord[random.randint(0, len(DataWord)-1)] for i in range(0,20))
        
        RandomWords = RandomWordNum
                
    the_word = f"{' '.join(RandomWords)}\n"
    
    print(the_word)
    asd = input(
    ">"
    ).strip()
    before = time.time()
    if asd != "":
        os.system("clear")
        jh = the_word.split()
        asds = asd.split()
        
        word_print = ""
        
        for i,v in zip(jh, asds):
            if i == v:
                word_print += i + " "
            else:
                word_print += f"{Color.red}{v}{Color.white} "
        print(word_print.strip())
        correct_characters = sum(a == b for a, b in zip(jh, asds))
        total_characters = len(the_word)
        acc = (correct_characters / total_characters) * 100
        print(f"accuracy: {round(acc, 2)} WPM: {round(len(the_word)/(time.time()-before), 2)}")
        print(time.time())
        print(before)
