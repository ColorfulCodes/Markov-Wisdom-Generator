import random
from itertools import izip

#Tweepy Magic
# -*- coding: utf-8 -*-

# Creat empty list to add words after split
tao = []

def read_file():
    # read files from three texts: Proverbs, Tao Te Ching, Dharmasala
    with open('/home/user/markov/prov.txt', 'r') as f, open('/home/user/markov/taotc.txt', 'r') as f2, open('/home/user/markov/dh.txt') as f3:

        #file2string = "".join([x for x in f2])
        """
        for x in f:
            x = x.replace(".", " .")
            for word in x.lower().strip().split():
                tao.append(word)

"""
        for x, y, z in izip(f, f2, f3):
            x = x.replace(".", " .")
            y = y.replace(".", " .")
            z = z.replace(".", " .")
            for word in x.lower().strip().split():
            #empty.append(line.split())
                tao.append(word)
            for word in y.lower().strip().split():
                tao.append(word)
            for word in z.lower().strip().split():
                tao.append(word)
        #print tao

read_file()

master_dict = {}
total = 0
for i in range(len(tao)-1):
    j = i + 1
    t_w = tao[i]
    j_w = tao[j]
    if t_w not in master_dict:
        master_dict[t_w] = {'_total':0}
    w_d = master_dict[t_w]

    if j_w not in w_d:
       w_d[j_w] = 0
    if j_w in w_d:
        w_d[j_w] += 1
        w_d['_total'] += 1

#print master_dict

for i in master_dict:
    #print k
    #print master_dict[i]['total']
    for k,v in master_dict[i].iteritems():
        if k != '_total':
            fraction = float(v)/float(master_dict[i]['_total'])
            value = master_dict[i]
            value[k] = fraction
            #print k, fraction

#print master_dict

def weighted_choice(choices):
   total = sum(w for c, w in choices.iteritems() if c != '_total')
   r = random.uniform(0, total)
   #print choices
   #print r
   upto = 0
   for c, w in choices.iteritems():
      if c == '_total':
        continue
      if upto + w >= r:
         #print c
         return c
      upto += w
   assert False, "Shouldn't get here"

# [ a a a b b c c c c c ]

# { 1: a, 4: b, 6: c }

# [ a * * b * c * * * * ]

"""
for i in range(20):
   weighted_choice(master_dict['compassion'])
"""

def generate_sentence():
    #w = random.choice(master_dict.keys())
    w = weighted_choice(master_dict['.'])
    string = ''
    #for i in range(9):
        #string+= (w)

    while True:
        if w  in ['.','!','?',',']:
            string += w
            break
        string+=(' ')
        string+= (w)
        w = weighted_choice(master_dict[w])
    return string[1:].capitalize()

stop = True
#for i in range(3):
hold = generate_sentence()
while stop:
    if len(hold) <= 160:
        #api.update_status(hold)
        #time.sleep(900)#Tweet every 15 minutes
        print hold
        stop = False
    else:
        hold = generate_sentence()



#  To make smarter have word frequency prefer nouns that follow other thingys. Have a larger data set.
