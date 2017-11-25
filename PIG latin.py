#piglatin
import random
from string import ascii_lowercase

allletters=list(ascii_lowercase)
consonants=allletters
vowels=['a','e','i','o',"u"]
vowelchoose=["way" , "yay","ay"]
newword=[]
wordlist=[]
for i in consonants:
    for j in vowels:
        if i == j:
            consonants.remove(i)
while True:
    while True:

        word=input("enter the word you want to convert to pig latin")
        if word.isalpha():
            wordlistvowels = list(word)
            wordlist=list(word)
            if wordlistvowels[0] in vowels:
                choose=random.choice(vowelchoose)
                print(word+choose)
            else:
                for m in wordlistvowels:
                    if m in vowels:
                        break
                    elif m in consonants:
                        newword.append(m)
                        wordlist.remove(m)
                        continue
                    else:
                        pass
                wordlist.extend(newword)
                new = "".join(wordlist)
                print(new+"ay")
            break
        else:
            print("enter the one word correctly:")
            continue
    value=input("do you want to enter more letter. if yes press y else n:").lower()

    if  value=="y":
        continue
    else:
        print("goodbye")
        exit()