#!/usr/bin/python

def display():
        for itr in word_arr:
                if any(itr.lower() in ch.lower() for ch in vowels):
                        print('\x1b[6;31;47m'+question[word_arr.index(itr)]+' '+'\x1b[0m'),
                else:
                        print question[word_arr.index(itr)]+' ',
        print;

def check():
        if any(letter.lower() in ch.lower() for ch in word_arr):
                for itr in range(len(word_arr)):
                        if letter.lower()==word_arr[itr].lower():
                                question[itr]=letter.lower();
                if question == word_arr:
                        print 'WIN!!!';
                        exit();
        else:
                global count;
                count+=1;
                print 'You have ',(8-count),' chances to win!'

print "~~~~~~~~~~~~~~~~~~~HANGMAN~~~~~~~~~~~~~~~~~~~~";
word="COMPUTER";
word_arr=list(word.lower());
vowels=('a','e','i','o','u');
no_of_chances=8;
count=0;
question='_' * len(word);
question=list(question);
display();

while(count<no_of_chances):
        letter=raw_input("Enter the char:")
        check();
        display();
