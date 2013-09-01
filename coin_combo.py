import time

Coins = {1:2,5:3,10:1,25:2}

"""
The easiest way to think about solving this problem is to take the nickels, dimes and quarters and find the largest sum you can make (75)
Then realize that you can create every sum divisible by 5 between 5 and 75 (15)
Then you can create three variants of each on of those sums by adding either 0, 1 or 2 pennies (15x3)
Then account for your ability to create the sum of 1 cent and two cents ((15x3)+2)
47
"""


def find_sums(coins, limit=None): 
        start = time.time()
        coinsAsList = dict_to_list(coins)
        if limit == None:
                limit = len(coinsAsList)
        assert limit <= len(coinsAsList), "limit can not exceed elements in combination"        
        sums, i, ew, ews = [],-1,[], []
        while len(ew) < limit: 
                tempEW = ew[:]      #this list allows you to keep track of which coins you have already tried to add to the new combo
                tempcoinsdict = coins.copy() #creates temperary dictionary in order to use keys to keep track of coins used
                i2 = 0
                while i2 < len(coinsAsList): #iterates through hand to add coins that have not yet been added to the existing combo
                        if coinsAsList[i2] not in tempEW: #if coin hasn't been used it's full number of times in the combo yet, then it's added to the combo
                                adding_ew = ew[:] #not having this line gave me lots of trouble... understandably 
                                adding_ew.append(coinsAsList[i2]) #adding new coin to ew as opposed to adding_ew gave me lots of trouble                               new_sum = add_list(adding_ew)
                                new_sum = add_list(adding_ew)
                                if new_sum not in sums:
                                        ews.append(adding_ew)
                                        sums.append(new_sum)
                                i2 += tempcoinsdict[coinsAsList[i2]] # iterate to the next coin, no matter how high the frequency is for the current coin in the existing combo, otherwise we build the same combo twice
                        else: #we check to see if the current coin has a high enough frequency to add it to the existing combo again
                                tempEW.remove(coinsAsList[i2]) #this is being removed so that when we check to see if the coin to be added is already in the existing combo, we can add it on the second pass as the logic in this claus' if statement
                                #we are keeping count (by removal) of how many times we have left to use this coin type in this combination. The if statement would never work in a case of double coins if we didn't remove it from the hand when we see it already exists
                                num = tempcoinsdict[coinsAsList[i2]] - 1
                                tempcoinsdict[coinsAsList[i2]] = num
                                i2 += 1
                                #if the coin is already in the combo, we remove one instance of the coin from the existing combo (as a list)
                                    #then subtract the frequency of that combo occuring in the dict, so when it's skipped over, it doesn't jump to far in the list       
                i += 1 #iterate to the next existing combo to create the next new combo
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

#this method is not currently being used
def list_to_dict(hand):
        # freqs: dictionary (element_type -> int)
        freq = {}
        for x in sequence:
                freq[x] = freq.get(x,0) + 1
        return freq

def dict_to_list(hand1):
        newlist = []
        items = hand1.items()
        for i in items:
                for i2 in xrange(i[1]):
                        newlist.append(i[0])
        return newlist
    
if __name__ == '__main__':
    coins(Coins)
