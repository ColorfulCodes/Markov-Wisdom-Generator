import random
import tweepy
import time
from secret import *
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)  
from itertools import zip_longest

#Tweepy Magic
# -*- coding: utf-8 -*-

# Create empty list to add words after split
holdWords = []

def read_file():
    # read files from three texts: Proverbs, Tao Te Ching, Dharmasala, and Islam wise sayings

    with open('/home/codegem/code/Markov-Wisdom-Generator/Texts/prov.txt', 'r') as f, open('/home/codegem/code/Markov-Wisdom-Generator/Texts/taotc.txt', 'r') as f2, open('/home/codegem/code/Markov-Wisdom-Generator/Texts/dhammapada.txt') as f3, open('/home/codegem/code/Markov-Wisdom-Generator/Texts/Proverbs.txt') as f4:

        # for loop through each file.
        for x, y, z, p in zip_longest(f, f2, f3, f4, fillvalue=''):
            # separate period from word
            
            x = x.replace(".", " .").replace('\x00', '')
            y = y.replace(".", " .")
            z = z.replace(".", " .")
            p = p.replace(".", " .")
            for word in x.lower().strip().split():

                holdWords.append(word)
            for word in y.lower().strip().split():
                holdWords.append(word)
            for word in z.lower().strip().split():
                holdWords.append(word)
            for word in p.lower().strip().split():
                holdWords.append(word)
        return holdWords
read_file()

#multiply longest file divided by file currently in
# max(log(a), log(b))/log(a) (lines of file is a
# or max(a,b)/a

master_dict = {}
total = 0
# iterate through  list of words
for i in range(len(holdWords)-1):
    # keep j one word ahead
    j = i + 1
    current_word = holdWords[i]
    next_word = holdWords[j]

    if current_word not in master_dict:
        # add current_word to dictionary
        # and give current_word a dictionary
        # '_total' as its value
        master_dict[current_word] = {'_total':0}

    copy_dict = master_dict[current_word]

    if next_word not in copy_dict:
        # if next_word not in dictionary
        # add it and set value to 0
        copy_dict[next_word] = 0

    if next_word in  copy_dict:
        # if it is in the dict, increment
        # it's value by 1
        copy_dict[next_word] += 1
        # increment total in entire dict by 1
        copy_dict['_total'] += 1


for i in master_dict:
    #print k
    #print master_dict[i]['total']
    # for key, value pair in dictionary
    for k,v in master_dict[i].items():
        if k != '_total':
            # divide value/count by dictionary word total
            fraction = float(v)/float(master_dict[i]['_total'])
            value = master_dict[i]
            # change value to fraction
            value[k] = fraction
            #print k, fraction

#print master_dict

def weighted_choice(choices):
   # total equals sum of all values in choices dictionary
   total = sum(word for c, word in choices.items() if c != '_total')
    # r equals generated number between 0 and total
   r = random.uniform(0, total)
   #print choices
   upto = 0
    # for key value pair in choices
   for c, word in choices.items():
      # Ignore _total
      if c == '_total':
        continue
        #if 0 + value of current word is >= r

      if upto + word >= r:
         #return current word
         return c
      #else add value of word to upto(which is originally 0)
      upto += word
   assert False, "Shouldn't get here"

def generate_sentence():
    #w = random.choice(master_dict.keys())
    word = weighted_choice(master_dict['.'])
    #creates string to add to
    string = ''

    while True:

        if word in ['.','!','?',',', ";"]:
            string += word
            break
        #add space to string
        string+=(' ')
        # add returned word to string
        string+= (word)
        # set word with a call to weighted_choice, with the value just used
        word = weighted_choice(master_dict[word])
    # cut off empty space in beginning of word and capitalize the first word
    return string[1:].capitalize()



def run():
    stop = True
    # holds value given from generate_sentence() function
    hold = generate_sentence()
    
    while stop:
        print(hold)
        # the tweet maximum is 160 char
        if len(hold) <= 160:
            api.update_status(hold)
            # time.sleep(900)
            # Tweet every 15 minutes
            if len(hold) <= 152:
                return hold + " #wisdom"
            else:
                return hold
        else:
            hold = generate_sentence()

run()


#  To make smarter have word frequency prefer nouns that follow other thingys. Have a larger data set.
