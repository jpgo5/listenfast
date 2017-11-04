import random
import time
import os

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']
both = list(set().union(letters, numbers))

# seqDomain=numbers
# seqDomain=letters
seqDomain=both
    
seqLength=4
tempo=0

def listenfast():
    playAgain=True
    print('Hello and welcome to the ListenFast game!')
    print('This will help you to listen and process faster.')
    print('sequence length is {}'.format(seqLength))
    raw_input('press enter to begin')
    print('')
    while(playAgain):
        #determineSequence
        sequence = determineSequence(seqDomain, seqLength)
        playSequence(sequence)
        responseStr = raw_input("what did you hear?: ")
        response = list(responseStr)
        response=cleanResponse(sequence, response)
        
        analyzeResponse(sequence, response)

        again= raw_input("Play again(y/n)?: ")
        if(not(again == '' or again == 'y')):
            playAgain=False


def cleanResponse(seq, res):
    if (len(seq) > len(res)):
        for i in range(len(res), len(seq)):
            res.append('*')
    return res
            
def analyzeResponse(s, r):
    incorrectIndices=[]
    for i in range(len(s)):
        if (s[i] != r[i]):
            incorrectIndices.append(i)
    if(len(incorrectIndices) == 0):
        print("correct!")
    else:
        incorrectRes=[]
        x=0
        for i in range(len(s)):
            if (r[i] != s[i]):
                incorrectRes.append(r[incorrectIndices[x]])
                x += 1
            else:
                incorrectRes.append(' ')
        correct=' '.join(s)
        incorrect=' '.join(incorrectRes)
        print('correct:   ' + correct)
        print('incorrect: ' + incorrect)

            
def determineSequence(domain, length):
    sequence=[]
    for i in range(length):
        sequence.append(domain[random.randint(0, len(domain)-1)])
    return sequence

def playSequence(sequence):
    time.sleep(.3)#so it don't speak as I hit the keyboard
    for i in range(len(sequence)):
        os.system("espeak '{}' 2> /dev/null".format(sequence[i]))
        time.sleep(tempo)
    
listenfast()

