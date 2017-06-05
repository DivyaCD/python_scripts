#!/usr/bin/python
from random import randint

def display():
        for itr in word_arr:
                if any(itr.lower() in ch for ch in vowels):
                        print('\x1b[6;31;47m'+question[word_arr.index(itr)]+' '+'\x1b[0m'),
                else:
                        print question[word_arr.index(itr)]+' ',
        print;

def check():
        if any(letter in ch for ch in word_arr):
                for itr in range(len(word_arr)):
                        if letter==word_arr[itr]:
                                question[itr]=letter;
                if question == word_arr:
                        print 'WIN!!!';
                        exit();
        else:
                global count;
                count+=1;
                print 'You have ',(8-count),' chances to win!'


print "~~~~~~~~~~~~~~~~~~~HANGMAN~~~~~~~~~~~~~~~~~~~~";
with open("words","r") as file_with_words:
        words=file_with_words.readlines();
        random_line=randint(0,len(words));
        word=words[random_line].replace('\n','').lower();
word_arr=list(word);
vowels=('a','e','i','o','u');
no_of_chances=8;
count=0;
question='_' * len(word);
question=list(question);
display();

while(count<no_of_chances):
        letter=raw_input("Enter the char:").lower();
        check();
        display();
print "The word is",word
