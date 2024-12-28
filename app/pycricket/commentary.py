import random

def for_single():
    com_for_single = ["Good cricket all round", "That seems to be missing leg...and its single",
                      "That's a Proper Cricket Shot.", "Excellent batting conditions", "Good cricket all round"]
    print(random.choice(com_for_single))

def for_boundary():
    commentry_for_boundary = ["Good cricket all round", "When He Hits It, It Stays Hit.",
                              "Hats placed in the gaps/vacant region", "That's a screamer", "Excellent batting conditions",
                              "Straight down the ground", "What a lovely shot!...its six", "Only he can play that shot"]
    print(random.choice(commentry_for_boundary))

def for_six():
    com_for_six = ["Good cricket all round ok", "Just over the fielder", "That's a hugeeeee hit! oke",
                   "That's a screamer", "Excellent batting conditions oke", "That's massive and out of the ground",
                   "Maxxxxximumm ok", "What a lovely shot!...its six", "Only he can play that shot", "That's huge",
                   "That's a maximum"]
    print(random.choice(com_for_six))

def for_wicket():
    com_for_wick = ["In the air...and taken", "Good cricket all round", "Excellent line and length",
                    "That's some good short stuff", "Straight Down the Fielder Throat.", "Right Up in the Blockhole.",
                    "...And he makes no mistake.", "Edged and taken.", "That's a screamer",
                    "In the air...fielder coming underneath and taken", "Batsman tried a fancy stroke and threw his wicket",
                    "The break cost him his wicket as batsman tends to lose some concentration", "Ball goes like a tracer bullet",
                    "What a catch!", "From the middle of the bat and taken", "In the air...fielder takes it!", "Bowled him",
                    "Excellent delivery"]
    print(random.choice(com_for_wick))

def for_bowling():
    com_for_bowling = ["It depends on how well the spinners bowl", "Good cricket all round", "Did it pitch in line",
                       "Excellent effort on the boundary", "He has a go at the stumps", "Direct hits are always dangerous",
                       "That's sloppy work by the fielder.", "He's Bowling a Good Line and Length", "...And he makes no mistake.",
                       "Beautiful spell"]
    print(random.choice(com_for_bowling))

def for_misc():
    com_for_misc = ["School boy stuff (Sunil Gavaskar's favourite when the batsman doesn't drag his bat in the crease)",
                    "We are up for a treat!", "Cricket Is the Winner.", "The Key Will Be Early Wickets.",
                    "The next few overs would be crucial.", "They need to go for wickets now.", "Stopping runs should be the topmost priority"]
    print(random.choice(com_for_misc))

def dot_line(x, y):
    var = " WICKET "
    var2 = " "
    print(var.center(35, "-"))
    print(f"wicket no {x} gone")
    print(f"Ball remaining {y}")
    print(var2.center(35, "-"))