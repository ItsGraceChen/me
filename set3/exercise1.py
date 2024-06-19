# -*- coding: UTF-8 -*-
"""Set 3, Exercise 1.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Using a while loop make a list of numbers that goes from the start number up
    to, but not including, the stop number, in increments of step. E.g.:
        start: 3
        stop: 10
        step: 2
        will return: [3, 5, 7, 9]
    Look up for how range() works in the python docs. You could  answer this
    with just the range function, but we'd like you to do it the long way.
    """
    start = 3
    stop = 10
    step = 2
    
    loop_ranger=[]
    for x in range(start, stop, step):
        loop_ranger.append(x)
    return loop_ranger

def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2

    You can either reuse loop_ranger, or the range function that in the standard library
    """
    start = 3
    stop = 20
    step = 2

    answer=[]
    for x in range(start, stop, step):
        answer.append(x)
    return answer

#########################################################################
def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for a function called "input"
    """
    list=[4, 9, 14, 19]
    stubborn_asker=[]
    guess=input(f"I'm thinking of a few numbers between 1 and 20. Guess one")
    if guess in list == False:
        print("Try again")
    else: print("You got it!")
    return stubborn_asker


    ##print("give me a a lower bound")
    #lowerbound=input
    #print("Now give me a a upper bound")
    #upperbound=input
    #numberIamthinkingof = 8
    #firstguess = False
#
 #   while not firstguess:
  #      if firstguess < numberIamthinkingof:
   #         print("lower")
    #    if firstguess > numberIamthinkingof:
     #       print(f"higher")
    #return stubborn_asker
#########################################################################

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    not_number_rejector = []

    number = int(f"give me a number")

    not_number=False

    if not_number:
        print("that's not a number, try again")
    else: print("That's a number. Good job")
    return not_number_rejector


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    return None


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
