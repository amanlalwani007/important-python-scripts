from profanity import profanity
from threading import Thread


def check(k):
        file=open(r"withoutabusewords.txt","a")
        custom_words=['fuck','bullshit','punkass','shit','pervert']
        profanity.load_words(custom_words)
        censor=profanity.censor(k)
        print(censor,end=' ')
        file.write(censor)
        file.write(" ")
def inputs():
    for i in range(10000):
        k=input()
        Thread(target=check(k)).start()


Thread(target=inputs).start()



