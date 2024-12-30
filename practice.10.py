"""import pyttsx3

engine=pyttsx3.init()
n=input("Enter anything:")
engine.say(n)
engine.runAndWait()"""


"""st="Hey! Ayesha you are amazing."

f=open("mytextfile.txt","w")
f.write(st)
f.close()"""


"""f=open("mytextfile.txt")
lines=f.readlines()
f.close()
print(lines,type(lines))"""

#You don't have to close the file


"""with open("mytextfile.txt") as f:
    print(f.read())"""


"""f=open("peom.txt","w")
f.write("Twinkle twinkle little star!")
f.close()"""


"""f=open("peom.txt")
content=f.read()
if("twinkle" in content):
    print("yes")
else:
    print("no")

f.close()"""

"""import random
def game():
       score=random.randint(1,100)
       with open("score.txt") as f:
               highscore=f.read()
               if(highscore!=""):
                   highscorescore=int(highscorescore)
               else:
                    highscore=0
       print("Your score",score)
       if(score>highscore):
           with open("score.txt","w") as f:
                f.write(str(score))
           
       return score
    

game()"""


"""def gen_table(n):
    table=""
    for i in range(1,11):
        table+=f"{n} * {i} = {n*i}\n"
    with open(f"tables/table{n}","w") as f:
        f.write(table)
for i in range(2,21):
    gen_table(i)"""

"""f=open("log.txt")
con=f.read()

if "python" in con:
    print("Yes")
else:
    print("No")"""


'''f=open("log.txt")
lines=f.readlines()
lineno=1
for line in lines:
    if "python" in line:
       print(f"line no:{lineno}")
       break
    lineno+=1

else:
    print("No")'''





















       



    

