# coding: utf-8

# In[48]:

poem = """Let me die a youngman's death
not a clean and in between
the sheets holywater death
not a famous-last-words
peaceful out of breath death

When I'm 73
and in constant good tumour
may I be mown down at dawn
by a bright red sports car
on my way home
from an allnight party

Or when I'm 91
with silver hair
and sitting in a barber's chair
may rival gangsters
with ham-fisted tommyguns burst in
and give me a short back and insides

Or when I'm 104
and banned from the Cavern
may my mistress
catching me in bed with her daughter
and fearing for her son
cut me up into little pieces
and throw away every piece but one

Let me die a youngman's death
not a free from sin tiptoe in
candle wax and waning death
not a curtains drawn by angels borne
'what a nice way to go' death
Roger McGough"""

poem = poem.lower().split()
print poem


# In[49]:

words = {}
for i in poem:
    if i[0] == 'a':
        words['a'] == i
    print words


# In[50]:

twist = filter(lambda x: not(x == ',' or x == ' ' or x == '.' or x.isdigit()), poem)
print twist


# In[81]:

words = {}
for word in twist:
    letter = word[0]
    try:
        words[letter].append(word)
    except:
        words[letter] = [word]
print words


# ### words
# * it's a dict
# * the key is a letter
# * the value is a list
#
# ### counter (function)
# * Counter takes a list
#
# ### count
# * it's a dict
#
# # goal:
# * you want to pass a dict with the values that are lists
# * and you want to return a dict, where the values are dicts
# * The return dict values, look like count

# In[107]:

#{a: {apples: 2, and: 1, animals:1, are:2},f:{fruits:1},g:{good:1},n:{not:1}}
def counter(words_list):
    count = {}
    for w in words_list:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1

    return count

counts = {}
for key, value in words.iteritems():
    counting = counter(value)
    counts[key] = counting


print counts
