import random
import os
import datetime
from commentary import for_single, for_boundary, for_six, for_wicket, for_bowling, for_misc, dot_line

# Create directory with current date and time
datetime_now = datetime.datetime.now()
dir_name = datetime_now.strftime("%d-%m-%Y_%H-%M-%S")
path = os.path.join('.', dir_name)
# os.mkdir(path)
# os.chdir(path)

# Function to accept only integer inputs for scoring
def intOnlytoscore(xy):
    while True:
        try:
            xinpa = int(input(xy))
            if 0 <= xinpa <= 6:
                return xinpa
            else:
                print("The score should range 0-6")
        except ValueError as e:
            print(e)

# First batting function
def battingfirst():
    usr_score = []
    com_score = []
    wick = 10
    while True:
        over = input("Enter the overs you need to play = ")
        if over.isdigit():
            over = int(over)
            break
        else:
            print("**Please enter a valid input**")
    ball = over * 6

    wick_c = 0
    ball_c = 0
    run_c = 0
    rran = range(1, ball + 1)

    while True:
        if wick_c > 9 or ball_c == ball:
            break
        usr_inp = intOnlytoscore("On Strike = ")
        ball_c += 1
        ball_r = ball - ball_c
        comp_inp = random.randint(0, 6)
        com_score.append(comp_inp)

        if usr_inp == comp_inp:
            wick_c += 1
            for_wicket()
            dot_line(wick_c, ball_r)
        else:
            run_c += usr_inp
            usr_score.append(usr_inp)
            if usr_inp == 6:
                for_six()
            elif usr_inp == 4:
                for_boundary()
            elif usr_inp == 1:
                for_single()

        if ball_c / 6 in rran:
            print(f"the score is {run_c}-{wick_c}")

    player_score = run_c
    print(f"Player {run_c}-{wick_c} in {ball_c}")

    busr_score = []
    bcom_score = []
    bwick = 10
    bover = over
    bball = bover * 6

    bwick_c = 0
    bball_c = 0
    brun_c = 0

    while True:
        if bwick_c > 9 or bball_c == bball or brun_c > player_score:
            break
        busr_inpb = intOnlytoscore("Bowl = ")
        bball_c += 1
        bball_r = bball - bball_c
        bcomp_inp = random.randint(0, 6)
        bcom_score.append(bcomp_inp)

        if busr_inpb == bcomp_inp:
            bwick_c += 1
            for_wicket()
            dot_line(bwick_c, bball_r)
        else:
            brun_c += bcomp_inp
            busr_score.append(bcomp_inp)
            if bcomp_inp == 6:
                for_six()
            elif bcomp_inp == 4:
                for_boundary()
            elif bcomp_inp == 1:
                for_single()

        if bball_c / 6 in rran:
            print(f"the score is {brun_c}-{bwick_c}")

    computer_score = brun_c
    print(f"{brun_c}-{bwick_c} in {bball_c} balls")

    if computer_score > player_score:
        final_res = f"Computer won the match by {computer_score - player_score}"
    elif computer_score < player_score:
        final_res = f"You won the match by {player_score - computer_score}"
    else:
        final_res = "Scores are Level -- Match Draw"

    print(final_res)

# First bowling function
def bowlingfirst():
    busr_score = []
    bcom_score = []
    bwick = 10

    while True:
        bover = input("Enter the overs you need to play = ")
        if bover.isdigit():
            bover = int(bover)
            break
        else:
            print("**Please enter a valid input**")

    bball = bover * 6
    bwick_c = 0
    bball_c = 0
    brun_c = 0
    rran = range(0, bball)

    while True:
        if bwick_c > 9 or bball_c == bball:
            break
        busr_inpb = intOnlytoscore("Bowl = ")
        bball_c += 1
        bball_r = bball - bball_c
        bcomp_inp = random.randint(0, 6)
        bcom_score.append(bcomp_inp)

        if busr_inpb == bcomp_inp:
            bwick_c += 1
            for_wicket()
            dot_line(bwick_c, bball_r)
        else:
            brun_c += bcomp_inp
            if bcomp_inp == 6:
                for_six()
            elif bcomp_inp == 4:
                for_boundary()
            elif bcomp_inp == 1:
                for_single()
            busr_score.append(busr_inpb)

        if bball_c / 6 in rran:
            print(f"the score is {brun_c}-{bwick_c}")

    computer_score = brun_c
    print(f"{brun_c}-{bwick_c} in {bball_c} balls")

    usr_score = []
    com_score = []
    wick = 10
    over = bover
    ball = over * 6
    wick_c = 0
    ball_c = 0
    run_c = 0

    while True:
        if wick_c > 9 or ball_c == ball or run_c > computer_score:
            break
        usr_inp = intOnlytoscore("On Strike = ")
        ball_c += 1
        ball_r = ball - ball_c
        comp_inp = random.randint(0, 6)
        com_score.append(comp_inp)

        if usr_inp == comp_inp:
            wick_c += 1
            for_wicket()
            dot_line(wick_c, ball_r)
        else:
            run_c += usr_inp
            usr_score.append(usr_inp)
            if usr_inp == 6:
                for_six()
            elif usr_inp == 4:
                for_boundary()
            elif usr_inp == 1:
                for_single()

        if ball_c / 6 in rran:
            print(f"the score is {run_c}-{wick_c}")

    player_score = run_c
    print(f"Player {run_c}-{wick_c} in {ball_c}")

    if computer_score > player_score:
        final_res = f"Computer won the match by {computer_score - player_score}"
    elif computer_score < player_score:
        final_res = f"You won the match by {player_score - computer_score}"
    else:
        final_res = "Scores are Level -- Match Draw"

    print(final_res)

# Toss mechanism
coin = ["head", "tail"]
play_selection = ["batting", "bowling"]
coin_random = random.choice(coin)

while True:
    usr_in = input("Head or Tail == ").lower()
    if usr_in in coin:
        break
    else:
        print("**Please enter a valid input**")

if usr_in == coin_random:
    print("You won the toss")
    while True:
        usr_selection = input("Batting or Bowling == ").lower()
        if usr_selection in play_selection:
            break
        else:
            print("**Please enter a valid input**")

    if usr_selection == "batting":
        print("You opt to Bat")
        battingfirst()
    else:
        print("You opt to bowl")
        bowlingfirst()
else:
    print("Computer won the toss")
    play_random = random.choice(play_selection)
    if play_random == "batting":
        print("Computer chooses to Bat")
        bowlingfirst()
    else:
        print("Computer chooses to Bowl")
        battingfirst()