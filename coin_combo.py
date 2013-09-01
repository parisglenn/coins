import random
import string
import time

#aidin
#paul
#isaac



Coins = {1:2,5:3,10:1,25:2}

"""
The easiest way to think about solving this problem is to take the nickels, dimes and quarters and find the largest sum you can make (75)
Then realize that you can create every sum divisible by 5 between 5 and 75 (15)
Then you can create three variants of each on of those sums by adding either 0, 1 or 2 pennies (15x3)
Then account for your ability to create the sum of 1 cent and two cents ((15x3)+2)
47
"""

#if i already have [1,5],[1,10], and [1,25], how do I avoid building [5,1], [10,1], and [25,1]


def find_sums(coins, limit=None): 
        start = time.time()
        coinsAsList = dictToList(coins)
        if limit == None:
                limit = len(coinsAsList)
        assert limit <= len(coinsAsList), "limit can not exceed elements in combination"        
        sums, i, ew, ews = [],-1,[], []
        while len(ew) < limit: 
                tempEW = ew[:]      #this list allows you to keep track of which coins you have already tried to add to the new combo
                tempcoinsdict = coins.copy() #creates temperary dictionary in order to use keys to keep track of letters used
                i2 = 0
                while i2 < len(coinsAsList): #iterates through hand to add letters that have not yet been added to the existing word
                        if coinsAsList[i2] not in tempEW: #if letter hasn't been used it's full number of times in the word yet, then it's added to the word
                                adding_ew = ew[:] #not having this line gave me lots of trouble... understandably 
                                adding_ew.append(coinsAsList[i2]) #adding new coin to ew as opposed to adding_ew gave me lots of trouble                               new_sum = add_list(adding_ew)
                                new_sum = add_list(adding_ew)
                                if new_sum not in sums:
                                        ews.append(adding_ew)
                                        sums.append(new_sum)
                                i2 += tempcoinsdict[coinsAsList[i2]] # iterate to the next letter, no matter how high the frequency is for the current letter in the existing word, otherwise we build the same word twice
                        else: #we check to see if the current letter has a high enough frequency to add it to the existing word again
                                tempEW.remove(coinsAsList[i2]) #this is being removed so that when we check to see if the letter to be added is already in the existing word, we can add it on the second pass as the logic in this claus' if statement
                                #we are keeping count (by removal) of how many times we have left to use this coin type in this combination. The if statement would never work in a case of double letters if we didn't remove it from the hand when we see it already exists
                                num = tempcoinsdict[coinsAsList[i2]] - 1
                                tempcoinsdict[coinsAsList[i2]] = num
                                i2 += 1
                                #if the letter is already in the word, we remove one instance of the letter from the existing word (as a list)
                                    #then subtract the frequency of that word occuring in the dict, so when it's skipped over, it doesn't jump to far in the list       
                i += 1 #iterate to the next existing word to create the next new word
                ew = ews[i][:]
        end = time.time()
        dur = end-start    
        print str(len(sums)), "possible combinations for ", str(coins), "took ", str(dur), "seconds to calculate"
        return sums

def add_list(combo):
        new_sum = 0
        for i in combo:
                new_sum += i
        return new_sum
"""    
def list_to_dict(hand):
        # freqs: dictionary (element_type -> int)
        freq = {}
        for x in sequence:
                freq[x] = freq.get(x,0) + 1
        return freq
"""
def dictToList(hand1):
        newlist = []
        items = hand1.items()
        for i in items:
                for i2 in xrange(i[1]):
                        newlist.append(i[0])
        return newlist
    
def test_dedup(coins):
        no_d = find_sums_dedup(coins, dedup=False)
        with_d = find_sums_dedup(coins, dedup=True)
        assert len(no_d) is len(with_d), "the two methods did not yeild equal results"

"""
def find_sums_dedup(coins, dedup=False): 
        start = time.time()
    coinsAsList = dictToList(coins)
    sums, i, ew, ews = [],-1,[], []
    while len(ew) < len(coinsAsList): 
        tempEW = ew[:]      #this list allows you to keep track of which coins you have already tried to add to the new combo
        tempcoinsdict = coins.copy() #creates temperary dictionary in order to use keys to keep track of letters used
        i2 = 0
        while i2 < len(coinsAsList): #iterates through hand to add letters that have not yet been added to the existing word
            if coinsAsList[i2] not in tempEW: #if letter hasn't been used it's full number of times in the word yet, then it's added to the word
                adding_ew = ew[:] #not having this line gave me lots of trouble... understandably 
                adding_ew.append(coinsAsList[i2]) #adding new coin to ew as opposed to adding_ew gave me lots of trouble
                new_sum = add_list(adding_ew)
                if dedup == True:
                    ews.append(adding_ew)
                    sums.append(new_sum)
                elif new_sum not in sums and dedup == False:
                    ews.append(adding_ew)
                    sums.append(new_sum)
                i2 += tempcoinsdict[coinsAsList[i2]] # iterate to the next letter, no matter how high the frequency is for the current letter in the existing word, otherwise we build the same word twice
            else: #we check to see if the current letter has a high enough frequency to add it to the existing word again
                tempEW.remove(coinsAsList[i2]) #this is being removed so that when we check to see if the letter to be added is already in the existing word, we can add it on the second pass as the logic in this claus' if statement
                #we are keeping count (by removal) of how many times we have left to use this coin type in this combination. The if statement would never work in a case of double letters if we didn't remove it from the hand when we see it already exists
                num = tempcoinsdict[coinsAsList[i2]] - 1
                tempcoinsdict[coinsAsList[i2]] = num
                i2 += 1
                #if the letter is already in the word, we remove one instance of the letter from the existing word (as a list)
                    #then subtract the frequency of that word occuring in the dict, so when it's skipped over, it doesn't jump to far in the list       
        i += 1 #iterate to the next existing word to create the next new word
        ew = ews[i][:]
    if dedup == True:
        sums = set(sums) #dedups the list
    end = time.time()
    dur = end-start    
    print str(len(sums)), "possible combinations for ", str(coins), "took ", str(dur), "seconds to calculate"
    return sums    
"""    
if __name__ == '__main__':
    pass
