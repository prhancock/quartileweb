#file -- quartiles.py --

import sys
import enchant
import itertools
import random
import time
import threading

d = enchant.Dict("en_US")

stringList = ['con','gre','ss','men',
              'che','ck','poi','nt',
              'bal','der','da','sh',
              'mys','te','ri','ous',
              'uns','uper','vi','sed']
#random.shuffle(stringList)


def permutations(iterable, r=None):
    #print("in permutations")
    #print(iterable)
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in itertools.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def containsVowel(word):
    vowels = {"a", "e", "i", "o", "u", "y"}
    if any(char in vowels for char in word.lower()):
        return True
    else:
        return False

def concatinateTuple(tuple):
    segment = ''
    for element in tuple:
        segment = segment + element
    return segment


def runningDots():
    count = 0
    while not done:
        if count < 5:
            print(".",end='',flush=True)
            count += 1
        else:
            print("\r     \r",end='',flush=True)
            count=0
        time.sleep(1)
    print("\r    \r",end='', flush=True)



#done=False
#t = threading.Thread(target=runningDots)
#t.start()

def getWords(gridList):
   count = 0
   wordList = []
   for length in [1,2,3,4]:
       mylist = list(permutations(gridList,length))
       for element in mylist:
          potentialWord = concatinateTuple(element)
          if d.check(potentialWord) and containsVowel(potentialWord):
             wordList.append(potentialWord)

   wordList.sort()
   #done=True
   #t.join()

   return wordList

   #for word in wordList:
   #   print(word)

if __name__ == "__main__":
    words = getWords(["eph","eme","ral","ly","cha","rc","ute","rie","ext","in","gui","sh","bat","tle","fie","ld","co","nspi","ra","cy"])
    print(words)
