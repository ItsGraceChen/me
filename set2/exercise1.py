"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  
# it printed "hello! Let's get started"

# It will print the words in order because it is a list
some_words = ["what", "does", "this", "line", "do", "?"] 
# Establish some_words = ["what", "does", "this", "line", "do", "?"] 

# It will only print one of the words listed 
for word in some_words:
    print(word)
# It printed "what", when pressed again it gives the next word in the line, until the entire list has been 

# It will print a word from the list at random
for x in some_words:
    print(x)
# It did the same thing as the previous one

# It will print into one sentence
print(some_words)
# ['what', 'does', 'this', 'line', 'do', '?']
# some_words contains more than 3 words

# after printing "what", "does", "this" then it will say "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words")
# since the LENgth of the list is more than 3, then it printed the words "some_words contains more than 3 words"

#it will print the platform with my username on it
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())
# UsefulFunction() = print(platform.uname()), so when you run it, it's actually running print(platform.uname()).
# In other words, "usefulFunction()"" is the shortcut of "print(platform.uname())"

#run the funtion
usefulFunction()
# prints out where this file is running and my user desktop