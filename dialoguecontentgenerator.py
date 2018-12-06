# -*- coding: utf-8 -*-
"""
Created on Mon Dec 3 13:16:49 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Machine learning and response to randomly generated dialogue.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Dialogue Content Generator [Computer software]. Github repository <https://github.com/alanjpan/Dialogue-Content-Generator>

Note this software's license is GNU GPLv3.
"""

import math
import random
import os

stopwords = ['i', 'a', 'about', 'an', 'are', 'as', 'at', 'be', 'by', 'com', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'the']

ConfuciusChain = {}
DarwinChain = {}
TolstoyChain = {}
ASmithChain = {}
ThoreauChain = {}

responsechain = {}
message = ''

def build_MarkovChain(text, MarkovChain):
    global ConfuciusChain
    global DarwinChain
    global TolstoyChain
    global ASmithChain
    global ThoreauChain
    words = text.replace("\n"," ").replace("\t"," ").split(' ')
    for i in range(len(words)):
        words[i] = words[i].replace(" ","")
    index = 1
    for word in words[index:]:
        key = words[index-1]
        if key in MarkovChain:
            MarkovChain[key].append(word)
        else:
            MarkovChain[key] = [word]
        index += 1

responsive = ['yes']
transition = ['the']
def generate_debate(count, MarkovChain):
    global message
    global responsechain
    global responsive
    #evaluate question
    word1 = random.choice(transition)
    #evaluate response
    for i in responsechain:
        if i in message:
            responsive.append(i)
    message = ''
    message = word1.capitalize()
    while (len(message.split(' ')) < count) or not message.endswith('.'):
        try:
            if random.randrange(0, 100) > 70:
                word2 = random.choice(responsechain[word1])
            elif random.randrange(0, 100) > 90:
                word2 = random.choice(MarkovChain[word1])
            else:
                word2 = random.choice(MarkovChain['the'])
        except Exception:
            word2 = 'the'
        word1 = word2
        message += ' ' + word2
    print(message)

def generate_question(count, MarkovChain):
    global message
    global transition
    global responsechain
    #store response
    responsechain.clear()
    messaged = []
    messaged = message.split(" ")
    #randomly clear a fifth of previous message memory
    for i in range(int(len(messaged)/5)):
        messaged.remove(random.choice(messaged))
    index = 1
    for word in messaged[index:]:
        key = messaged[index-1]
        if key in responsechain:
            responsechain[key].append(word)
        else:
            responsechain[key] = [word]
        index += 1
    message = ''
    if random.randrange(0, 100, 1) > 50:
        while not message.endswith('?'):
            word1 = random.choice(list(MarkovChain.keys()))
            message = word1.capitalize()
            while (len(message.split(' ')) < count):
                word2 = random.choice(MarkovChain[word1])
                word1 = word2
                message += ' ' + word2
    else:
        word1 = random.choice(list(MarkovChain.keys()))
        message = word1.capitalize()
        while (len(message.split(' ')) < count) or not message.endswith('.'):
            word2 = random.choice(MarkovChain[word1])
            word1 = word2
            message += ' ' + word2
    transition.clear()
    transition = message.split(' ')
    print(message)

#load Thoreau
filename = 'C:\\Users\\alanp\\Desktop\\SJTU\\Problem Solving with AI Techniques W F 3hrs\\Proj4\\Thoreau Walden.txt'
with open(filename, errors = 'ignore') as file_object:
    input = file_object.read()
    file_object.close()
build_MarkovChain(input, ThoreauChain)

#load Darwin
filename = 'C:\\Users\\alanp\\Desktop\\SJTU\\Problem Solving with AI Techniques W F 3hrs\\Proj4\\Darwin Origin of Species.txt'
with open(filename, errors = 'ignore') as file_object:
    input = file_object.read()
    file_object.close()
build_MarkovChain(input, DarwinChain)

#load Tolstoy
filename = 'C:\\Users\\alanp\\Desktop\\SJTU\\Problem Solving with AI Techniques W F 3hrs\\Proj4\\War and Peace.txt'
with open(filename, errors = 'ignore') as file_object:
    input = file_object.read()
    file_object.close()
build_MarkovChain(input, TolstoyChain)




ndebate = random.randrange(20, 50, 1)
print('\nTolstoy:')
generate_debate(ndebate, TolstoyChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, TolstoyChain)

ndebate = random.randrange(20, 50, 1)
print('\nThoreau:')
generate_debate(ndebate, ThoreauChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, ThoreauChain)

ndebate = random.randrange(20, 50, 1)
print('\nDarwin:')
generate_debate(ndebate, DarwinChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, DarwinChain)

ndebate = random.randrange(20, 50, 1)
print('\nTolstoy:')
generate_debate(ndebate, TolstoyChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, TolstoyChain)

ndebate = random.randrange(20, 50, 1)
print('\nThoreau:')
generate_debate(ndebate, ThoreauChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, ThoreauChain)

ndebate = random.randrange(20, 50, 1)
print('\nDarwin:')
generate_debate(ndebate, DarwinChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, DarwinChain)

ndebate = random.randrange(20, 50, 1)
print('\nTolstoy:')
generate_debate(ndebate, TolstoyChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, TolstoyChain)

ndebate = random.randrange(20, 50, 1)
print('\nDarwin:')
generate_debate(ndebate, DarwinChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, DarwinChain)

ndebate = random.randrange(20, 50, 1)
print('\nThoreau:')
generate_debate(ndebate, ThoreauChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, ThoreauChain)

ndebate = random.randrange(20, 50, 1)
print('\nDarwin:')
generate_debate(ndebate, DarwinChain)
nquestion = random.randrange(5, 15, 1)
generate_question(nquestion, DarwinChain)

ndebate = random.randrange(40, 60, 1)
print('\nTolstoy:')
generate_debate(ndebate, TolstoyChain)



"""

filename = 'C:\\Users\\alanp\\Desktop\\SJTU\\Problem Solving with AI Techniques W F 3hrs\\Proj4\\Confucius Analects.txt'
with open(filename, errors = 'ignore') as file_object:
    input = file_object.read()
    file_object.close()
build_MarkovChain(input, ConfuciusChain)


filename = 'C:\\Users\\alanp\\Desktop\\SJTU\\Problem Solving with AI Techniques W F 3hrs\\Proj4\\Confucius Great Learning.txt'
with open(filename, errors = 'ignore') as file_object:
    input = file_object.read()
    file_object.close()
build_MarkovChain(input, ConfuciusChain)


filename = 'C:\\Users\\alanp\\Desktop\\SJTU\\Problem Solving with AI Techniques W F 3hrs\\Proj4\\Smith Wealth of Nations.txt'
with open(filename, errors = 'ignore') as file_object:
    input = file_object.read()
    file_object.close()
build_MarkovChain(input, ASmithChain)
"""