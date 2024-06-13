# *************************************************
# Part Of Speech Project
# CPSC 3750 - AI 
# BY: Michael, Devjot, and Tarun
# Jun 6th 2024
# *************************************************

# importing libraries, tkinter, and nltk

import tkinter
from tkinter import *


import tkinter as tk

# fix import packages later..
# also, nltk sou

import tkinter.messagebox as mbox
import nltk

from nltk.corpus import stopwords
# toeknize, like tags stored in variables for each word, and using those tags 
# we describe using constraints if a word is a noun, verb, etc.


from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure the required NLTK data is available
nltk.download('stopwords')
nltk.download('punkt')

# standard data pulled off the web, nltk site, etc.

nltk.download('averaged_perceptron_tagger')


stop_words = set(stopwords.words('english'))

# show this in gui jpeg images to user when they click POF button.

def show_pof():
    # hard-coded.
    mbox.showinfo("Parts Of Speech", "There are 8 parts of speech in the English language:\n\n"
                                     "1.) Noun - NN, NNP, NNS, NNPS\n"
                                     "2.) Pronoun - PRP\n"
                                     "3.) Verb - VB, VBD, VBG, VBN, VBP, VBZ\n"
                                     "4.) Adjective - JJ, JJR, JJS\n"
                                     "5.) Adverb - RB, RBR, RBS\n"
                                     "6.) Preposition - IN\n"
                                     "7.) Conjunction - IN, CC\n"
                                     "8.) Interjection - UH")
# for example NN means a word is a noun


def calculate_pof():
    nouns1, pronouns1, verbs1, adjectives1, adverbs1, prepositions1, conjunctions1, interjections1 = ([] for _ in range(8))
    # as u can see i made the range of 8 in total for output.
    pos_tags = {
        'NN': nouns1, 'NNP': nouns1, 'NNS': nouns1, 'NNPS': nouns1, # same comment from above.

        'PRP': pronouns1,
        'VB': verbs1, 'VBD': verbs1, 'VBG': verbs1, 'VBN': verbs1, 'VBP': verbs1, 'VBZ': verbs1,
        'JJ': adjectives1, 'JJR': adjectives1, 'JJS': adjectives1,
        'RB': adverbs1, 'RBR': adverbs1, 'RBS': adverbs1,

        
        'IN': prepositions1,
        
        'CC': conjunctions1,
        'UH': interjections1
    }

    text = text_enter.get("1.0", "end-1c")
    tokenized = sent_tokenize(text)

    
    for sentence in tokenized:
        
        wordsList = [word for word in nltk.word_tokenize(sentence) if word not in stop_words]
        tagged = nltk.pos_tag(wordsList)
        # tags, (tokenization)

        for word, pos in tagged:
# for-loop for the word in each of the tags.


            if pos in pos_tags:
                pos_tags[pos].append(word)

                # append function used here 

    mbox.showinfo("Count of POF", 
                  f"Nouns: {len(nouns1)}\nNouns are: {', '.join(nouns1)}\n\n" # display to user in gui
                  f"Pronouns: {len(pronouns1)}\nPronouns are: {', '.join(pronouns1)}\n\n"
                  f"Verbs: {len(verbs1)}\nVerbs are: {', '.join(verbs1)}\n\n"

                  
                  f"Adjectives: {len(adjectives1)}\nAdjectives are: {', '.join(adjectives1)}\n\n"
                  
                  f"Adverbs: {len(adverbs1)}\nAdverbs are: {', '.join(adverbs1)}\n\n"
                  
                  f"Prepositions: {len(prepositions1)}\nPrepositions are: {', '.join(prepositions1)}\n\n"
                  #
                  # fix later.
                  f"Conjunctions: {len(conjunctions1)}\nConjunctions are: {', '.join(conjunctions1)}\n\n"
                  
                  f"Interjections: {len(interjections1)}\nInterjections are: {', '.join(interjections1)}")

def clear_text():
    text_enter.delete("1.0", "end")
# button that clears the stuff the user entered, 

# gui

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"): # gui, display to user.
        window.destroy()

# exit button

# GUI setup
window = Tk()


window.geometry("1000x700")
# prefences set for the window

window.title("Part Of Speech Calculator")

# this entire section for the GUI setsup the window that will pop open
# size, function of button, etc.

start1 = Label(window, text='Part of Speech Calculator', font=("Arial", 35), fg="magenta", underline=0)
start1.place(x=200, y=10)

enter_label = Label(window, text="Enter Your text or paragraph here...", font=("Arial", 30), fg="brown")
enter_label.place(x=150, y=100)

text_enter = tk.Text(window, height=15, width=80, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3, relief="solid")
text_enter.place(x=50, y=150)


# these are set of buttons 

pofb = Button(window, text="POF", command=show_pof, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
pofb.place(x=150, y=570)

calculateb = Button(window, text="CALCULATE", command=calculate_pof, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
calculateb.place(x=280, y=570)

resetb = Button(window, text="CLEAR", command=clear_text, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
resetb.place(x=530, y=570)

exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 20), bg="red", fg="blue", borderwidth=3, relief="raised")
exitb.place(x=700, y=570)

window.protocol("WM_DELETE_WINDOW", exit_win)

# loop until exit clicked.

window.mainloop()
# done. 