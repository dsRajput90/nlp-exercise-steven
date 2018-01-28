
# coding: utf-8

# In[66]:

#Necessary imports

import nltk
from nltk.corpus import *
from nltk.corpus import state_union
from nltk.corpus import wordnet
from nltk.book import *
import pylab, matplotlib, random


# In[181]:

#1. Create a variable phrase containing a list of words. Review the operations described in the previous chapter, including addition, multiplication, indexing, slicing, and sorting.

sent='the lion is the king of the jungle'
phrase = sent.split()
phrase.append('hello')
phrase[2:5]
sorted(map(lambda x:x.lower(),phrase))


# In[183]:

#2. Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?

austen=nltk.corpus.gutenberg.words('austen-persuasion.txt')
print(sorted(map(lambda x:x.lower(),austen)))


# In[184]:

print(sorted(set(map(lambda x:x.lower(),austen))))


# In[186]:

#3. Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus reader nltk.corpus.webtext.words() to access some sample text in two different genres.

brown.words(categories=[brown.categories()[0],brown.categories()[1]])


# In[45]:

#4. Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of men, women, and people in each document. What has happened to the usage of these words over time?

def tabulate(cfdist, words, categories):
    print('%-16s' % 'Category', end=' ')
    for word in words:
        print('%6s' % word, end=' ')
    print()
    for category in categories:
        print('%-16s' % category, end=' ')
        for word in words:
            print('%6d' % cfdist[category][word], end=' ')
        print()
        
        
cfd = nltk.ConditionalFreqDist(
    (fileid, word)
    for fileid in state_union.fileids()
    for word in state_union.words(fileid))


# In[47]:

tabulate(cfd, ['men', 'women', 'people'], state_union.fileids())


# In[55]:

#5. Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use: member_meronyms(), part_meronyms(),  substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().

wordnet.synset('book.n.01').part_holonyms()
wordnet.synset('book.n.01').substance_holonyms()
wordnet.synset('book.n.01').member_holonyms()


# In[69]:

print(wordnet.synset('tree.n.01').part_holonyms())
print(wordnet.synset('tree.n.01').substance_holonyms())
print(wordnet.synset('tree.n.01').member_holonyms())
print(wordnet.synset('tree.n.01').part_meronyms())
print(wordnet.synset('tree.n.01').substance_meronyms())
print(wordnet.synset('tree.n.01').member_meronyms())
print(wordnet.synset('tree.n.01').hyponyms())


# In[ ]:

#6.  In the discussion of comparative wordlists, we created an object called translate which you could look up using words in both German and Spanish in order to get corresponding words in English. What problem might arise with this approach? Can you suggest a way to avoid this problem?

#ans: Circular translations could result in inaccuracies, even errors. So while translating from one language to another and then translating back, comparing with other languages could be helpful to reduce imperfections.


# In[188]:

#7. According to Strunk and White's Elements of Style, the word however, used at the start of a sentence, means "in whatever way" or "to whatever extent", and not "nevertheless". They give this example of correct usage: However you advise him, he will probably do as he thinks best. (http://www.bartleby.com/141/strunk3.html) Use the concordance tool to study actual usage of this word in the various texts we have been considering. See also the LanguageLog posting "Fossilized prejudices about 'however'" at http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print(emma.concordance('however'))
brn = nltk.Text(nltk.corpus.brown.words('ca01'))
print(brn.concordance('however'))
cht = nltk.Text(state_union.words(state_union.fileids()[0]))
print(cht.concordance('however')) #mistake in the usage of however!


# In[189]:

#8. Define a conditional frequency distribution over the Names corpus that allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).

cfd = nltk.ConditionalFreqDist(
        (fileid, name[0])
        for fileid in names.fileids()
        for name in names.words(fileid))
cfd.plot()


# In[190]:

#9. Pick a pair of texts and study the differences between them, in terms of vocabulary, vocabulary richness, genre, etc. Can you find pairs of words which have quite different meanings across the two texts, such as monstrous in Moby Dick and in Sense and Sensibility?

from __future__ import division
len(text2)/len(set(text2))
len(text3)/len(set(text3))
fdist2=nltk.FreqDist([w.lower() for w in text2 if len(w)>5])
fdist3=nltk.FreqDist([w.lower() for w in text3 if len(w)>5])
sorted(fdist2.items())[:50]
sorted(fdist3.items())[:50]

#study the occurance of any word using concordance


# In[131]:

#10. Read the BBC News article: UK's Vicky Pollards 'left behind' http://news.bbc.co.uk/1/hi/education/6173441.stm. The article gives the following statistic about teen language: "the top 20 words used, including yeah, no, but and like, account for around a third of all words." How many word types account for a third of all word tokens, for a variety of text sources? What do you conclude about this statistic? Read more about this on LanguageLog, at http://itre.cis.upenn.edu/~myl/languagelog/archives/003993.html.

fdist5 = FreqDist(w.lower() for w in text5)
fdist5.plot(29, cumulative=True)


# In[191]:

#11. Investigate the table of modal distributions and look for other patterns. Try to explain them in terms of your own impressionistic understanding of the different genres. Can you find other closed classes of words that exhibit significant differences across different genres?

cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genre = brown.categories()
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genre,samples=modals)


# In[193]:

#12. The CMU Pronouncing Dictionary contains multiple pronunciations for certain words. How many distinct words does it contain? What fraction of words in this dictionary have more than one possible pronunciation?

cmd = nltk.corpus.cmudict.dict()
#print(len(set(map(lambda x:x.lower(),cmd))))
ctr=0
for k in cmd:
    if(len(cmd[k])>1):
        ctr=ctr+1
print(ctr)


# In[148]:

#13. What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n').

syn=list(wordnet.all_synsets('n'))
ctr=0
for s in syn:
    if(len(s.hyponyms())==0):
        ctr=ctr+1
print(ctr/len(syn) * 100)


# In[194]:

#14. Define a function supergloss(s) that takes a synset s as its argument and returns a string consisting of the concatenation of the definition of s, and the definitions of all the hypernyms and hyponyms of s.

def supergloss(s):
    res=s.definition() + '\n'
    for w in s.hyponyms():
        res += ' ' + str(w) + ' ' + w.definition() + "\n"
    for w in s.hypernyms():
        res += ' ' + str(w) + ' ' + w.definition() + "\n"
    return res


print(supergloss(wordnet.synset('tree.n.01')))


# In[195]:

#15. Write a program to find all words that occur at least three times in the Brown Corpus.

print((lambda x:x in nltk.corpus.brown.words() and brown.words().count(x) >=3,brown.words()))


# In[196]:

#16. Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), as we saw in 1.1. Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()). Which genre has the lowest diversity (greatest number of tokens per type)? Is this what you would have expected?

def lexical_diversity(text):
    return len(text)/len(set(text))

cfd=nltk.ConditionalFreqDist(
    (category, lexical_diversity(nltk.Text(brown.words(categories=category))))
    for category in brown.categories())

cfd.plot()


# In[199]:

#17. Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

def freq_words(words):
    content = [w for w in words if w.lower() not in stopwords.words('english')]
    return nltk.FreqDist(content).most_common(50)

freq_words(text1)


# In[200]:

#18. Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

def freq_words_bi(words):
    content = [w for w in words if w.lower() not in stopwords.words('english')]
    return nltk.FreqDist(nltk.bigrams(content)).most_common(50)

freq_words_bi(text1)


# In[41]:

#19. Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.

genres=brown.categories()
words= ['people', 'earth', 'country', 'science', 'sports', 'space', 'love']
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

cfd.tabulate(conditions=genres, samples=words)


# In[48]:

#20. Write a function word_freq() that takes a word and the name of a section of the Brown Corpus as arguments, and computes the frequency of the word in that section of the corpus.

def word_freq(word,section):
    freq=FreqDist([w for w in brown.words(categories=section)])
    return freq.__getitem__(word)

word_freq('love','romance')


# In[58]:

#21. Write a program to guess the number of syllables contained in a text, making use of the CMU Pronouncing Dictionary.

text = ['love', 'new', 'yankee', 'really']
new_entries=[y for x,y in enumerate(nltk.corpus.cmudict.entries()) if y[0] in text]


# In[55]:

#22. Define a function hedge(text) which processes a text and produces a new version with the word 'like' between every third word.

def hedge(text):
    new_text=[]
    counter=1
    for word in text:
        new_text.append(word)
        if(counter%3==0):
            new_text.append('like')
        counter+=1
    return ' '.join(new_text)

hedge(text3)


# In[63]:

#23.  Zipf's Law: Let f(w) be the frequency of a word w in free text. Suppose that all the words of a text are ranked according to their frequency, with the most frequent word first. Zipf's law states that the frequency of a word type is inversely proportional to its rank (i.e. f × r = k, for some constant k). For example, the 50th most common word type should occur three times as frequently as the 150th most common word type.

done_ent=[]
total_len=0
for entry in new_entries:
    if entry[0] not in done_ent:
        total_len+=len(entry[1])
        done_ent.append(entry[0])
        
total_len


# In[81]:

# Write a function to process a large text and plot word frequency against word rank using pylab.plot. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale). What is going on at the extreme ends of the plotted line?

from decimal import *
def freq_rank(text):
    fdist=FreqDist([w.lower() for w in text])
    keys=fdist.keys()
    freq=[]
    rank=[]
    n=1
    
    for w in keys:
        frequency = Decimal.logb(Decimal(fdist[w]))
        freq.append(frequency)
        rank.append(Decimal.logb(Decimal(n)))
        n+=1
        
    pylab.plot(rank,freq)
    return pylab.show()
    


# In[90]:

freq_rank(text1)


# In[204]:

# Generate random text, e.g., using random.choice("abcdefg "), taking care to include the space character. You will need to import random first. Use the string concatenation operator to accumulate characters into a (very) long string. Then tokenize this string, and generate the Zipf plot as before, and compare the two plots. What do you make of Zipf's Law in the light of this?

def freq_rank_scramble(text):
    n = 0
    scrambled = ''
    freq = []
    rank = []

    while n < len(text):
        scrambled = scrambled + ' ' + random.choice(text)
        n = n + 1

    scrambled = scrambled.split()

    fdist = nltk.FreqDist([w.lower() for w in scrambled])
    keys = fdist.keys()

    n = 1
    for w in keys:
        frequency = Decimal.logb(Decimal(fdist[w]))
        freq.append(frequency)
        rank.append(Decimal.logb(Decimal(n)))
        n = n + 1
    
    pylab.plot(rank, freq)
    return pylab.show()


# In[91]:

freq_rank_scramble(text1)


# In[121]:

#24. Modify the text generation program in 2.2 further, to do the following tasks:
# Store the n most likely words in a list words then randomly choose a word from the list using random.choice(). (You will need to import random first.)
# Select a particular genre, such as a section of the Brown Corpus, or a genesis translation, one of the Gutenberg texts, or one of the Web texts. Train the model on this corpus and get it to generate random text. You may have to experiment with different start words. How intelligible is the text? Discuss the strengths and weaknesses of this method of generating random text.
# Now train your system using two distinct genres and experiment with generating text in the hybrid genre. Discuss your observations.

i=0
word='romance'
num=10
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
for i in range(num):
    print(word)
    words = list(cfd[word].keys())
    print(len(words))
    if(len(words)>=num):
        
        words=words[:num]
    word = random.choice(words)
    


# In[201]:

#25.  Define a function find_language() that takes a string as its argument, and returns a list of languages that have that string as a word. Use the udhr corpus and limit your searches to files in the Latin-1 encoding.

def find_language(text):
    languages=[]
    target_languages=[]
    
    for name in udhr.fileids():
        if 'Latin1' in name:
            languages.append(name)
    
    for lang in languages:
        if text in udhr.words(lang):
            target_languages.append(lang)
    
    return target_languages

find_language('of')


# In[202]:

#26. What is the branching factor of the noun hypernym hierarchy? I.e. for every noun synset that has hyponyms — or children in the hypernym hierarchy — how many do they have on average? You can get all noun synsets using wn.all_synsets('n').

def branching_factor(synset_group):
    total=0
    count=0
    
    for synset in synset_group:
        if synset.lemmas() != []:
            total = total + len(synset.lemmas())
            count+=1
    
    return total/count

branching_factor(wordnet.synsets('n'))


# In[203]:

#27. The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')). Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.

def calc_avg(synsets):
    total=0;
    avg=0;
    all_words=[];
    for syn in synsets:
        all_words+=syn.lemma_names()
    
    total=len(set(all_words))
    
    avg = total/len(synsets)
    return avg

print(calc_avg(wordnet.synsets('n')))
print(calc_avg(wordnet.synsets('v')))
print(calc_avg(wordnet.synsets('a'))) #adjective
print(calc_avg(wordnet.synsets('r'))) #verb


# In[212]:

#28. Use one of the predefined similarity measures to score the similarity of each of the following pairs of words. Rank the pairs in order of decreasing similarity. How close is your ranking to the order given here, an order that was established experimentally by (Miller & Charles, 1998): car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, lad-brother, crane-implement, journey-car, monk-oracle, cemetery-woodland, food-rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest, lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string. 

def similarity(word1,word2):
    syn1 = wordnet.synset(word1 + ".n.01")
    syn2 = wordnet.synset(word2 + ".n.01")
    
    return syn1.path_similarity(syn2)


#solution
print("car-automobile " + str(similarity("car","automobile")))
print("gem-jewel " + str(similarity("gem","jewel")))
print("journey-voyage " + str(similarity("journey","voyage")))
print("boy-lad " + str(similarity("boy","lad")))
print("coast-shore " + str(similarity("coast","shore")))
print("asylum-madhouse " + str(similarity("asylum","madhouse")))
print("magician-wizard " + str(similarity("magician","wizard")))
print("midday-noon " + str(similarity("midday","noon")))
print("furnace-stove " + str(similarity("furnace","stove")))
print("food-fruit " + str(similarity("food","fruit")))
print("bird-cock " + str(similarity("bird","cock")))

