#Karthik Jagadeesan 72796420 and Hieu Dao-Tran 24353293.  ICS 31 Lab sec 5.  Lab asst 8.
def bandb(doc: str):
    infile = open(doc, 'r')
    sample = infile.read()
    inputlist = sample.split('\n')
    finalrooms = []
    exlist = []
    newlist = []
    for string in inputlist:
        exlist.append(string.strip(' '))
    for letters in exlist:
        newlist.append(letters[:2].upper() + letters[2:])
    for word in newlist:
        if word[:2] == 'PL':
            print(word[3:])
        elif word[:2] == 'LB':
            print('Number of rooms in serivce:', len(finalrooms))
            print('---------------------------------------------')
            for num in finalrooms:
                print(num)
        elif word[:2] == 'NB':
            finalrooms.append(int(word[2:].strip(' ')))
bandb('inputsample.txt')
