import gspread
from google.oauth2.service_account import Credentials
from time import sleep
import sys, time
import os
from quiz import quiz_data


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('avengers_quiz')

sales = SHEET.worksheet('leaderboard')

user_name = ""

score = 0

def clear_terminal(): 
    """
    Pauses the terminal for 5 seconds and clears the terminal
    """
    sleep(2)

    os.system('clear')


def slow_print(str, duration):
    """
    Pints out string in a typing effect.
    """
    
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(duration)


def validate_user_name(user_name):

    """
    Validates user_name input to see if it matches the criteria.
    """
    
    if user_name == "":
        print("Please don't enter an empty value!")
    elif len(user_name) > 12:
        print("Name shouldn’t be more than 12 chartectors long!")

    elif len(user_name) < 3:
        print("Name shouldn’t be less than 3 chartectors!")
    else: 
        return True

def display_question(index, question, options):
    """
    Print questions and loop through options array and print each value
    """

    print(f"Question {index}/10 \n")

    slow_print(question + "\n", 3./90)

    for option in options:
        slow_print(option, 3./90)

    slow_print("Please enter your answer (a, b, c, or d): ", 3./90)


def check_answer(answer, question_answer):
    """
    Checks the answers to the questions if both values are equal. 
    One point will be added to the score. 
    If the answer is wrong no points will be added.
    """
    global score

    if(answer.lower() == question_answer.lower()):
        slow_print("Correct answer\n", 4./90)

        score += 1
    else:
        slow_print("Incorrect answer\n", 4./90)


def quiz_information():
    """ 
    Print the Avengers logo and information about the quiz.
    """

    slow_print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣾⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⣿⡿⠟⠛⠋⣽⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀
⠀⠀⢀⣾⣿⠟⠁⠀⠀⠀⣼⣿⣿⠏⢸⣿⣿⡏⠻⣿⣷⡀⠀⠀
⠀⢠⣿⡟⠁⠀⠀⠀⠀⣼⣿⣿⡟⠀⢸⣿⣿⡇⠀⠈⢻⣿⡄⠀
⢠⣿⡟⠀⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⢸⣿⣿⡇⠀⠀⠀⢻⣿⡄
⣸⣿⠇⠀⠀⠀⠀⣼⣿⣿⣿⠁⠀⠀⠘⢿⣿⡇⠀⠀⠀⠘⣿⣇
⢿⣿⠀⠀⠀⠀⣰⣿⣿⣿⣇⣀⣀⣀⣼⣦⡙⠇⠀⠀⠀⠀⣿⡿
⢸⣿⡇⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⠀⠀⠀⢸⣿⡇
⠀⢿⣿⡀⣸⣿⣿⣿⠟⠉⠉⠉⠉⠉⣿⠟⣡⡆⠀⠀⢀⣿⡿⠀
⠀⠈⠛⣰⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠠⠾⠿⠇⠀⣠⣿⡿⠁⠀
⠀⠀⣰⣿⣿⣿⡟⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠋⠀⠀⠀
⠀⣰⣿⣿⣿⡿⠰⠿⣿⣶⣶⣶⣶⣶⣶⣿⠿⠟⠉⠀⠀⠀⠀⠀
⠀⠉⠉⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n""", 2./90)

    slow_print("Welcome to the Avengers quiz!\n", 3./90)

    slow_print("Take this quiz to see how well you know the Marvel film series, Avengers.\n", 4./90)

    slow_print("There are ten questions in total, and all questions are multiple-choice.\n", 4./90)

    slow_print("The choices are a, b, c, and d for all ten questions.\n", 4./90)

    slow_print("Please enter a, b, c, or d and hit the enter key to answer the question.\n", 4./90)

def begin_quiz():
    """
    Get users name and prompt the user if they wish to play the quiz.
    """

    global user_name
    
    while True:
        user_name = input("Please enter your name\n").strip()

        if validate_user_name(user_name):
            break

    play_quiz = ""

    while play_quiz not in ["y", "n"]:
       
        play_quiz = input(("Do you want to begin the quiz? (y/n) \n")).lower()

        if(play_quiz == "n"):
            slow_print(f"Thank you {user_name}, please try the quiz another time!", 4./90)

            quit()

        if(play_quiz not in ["y", "n"]):
                slow_print("Invalid Input! Please enter yes (y) or no (n)\n", 4./90)

    clear_terminal()


def run_quiz ():
    """
    Loop through quiz_data and print questions and options. 
    Request the correct answer and verify whether the 
    answer is correct or incorrect.
    """

    for index, quiz in enumerate(quiz_data,start=1):
        answer = ""

        while answer not in ["a", "b", "c", "d"]:

            display_question(index, quiz["question"], quiz["options"])

            answer = input("\n").lower()

            print("\n")

            if(answer not in ["a", "b", "c", "d"]):
                slow_print("Invalid Input! Please enter a, b, c, or d\n", 4./90)

        check_answer(answer, quiz["answer"])

        clear_terminal()

    display_result()


def update_leaderboard(data):
    """
    Add user-name and score to Google Sheets
    """

    slow_print("Exporting your results to database....\n", 4./90)

    update_workout = SHEET.worksheet("leaderboard")
    update_workout.append_row(data)

    slow_print("Results exporting successfully!!\n", 4./90)


def display_leaderboard():
    """
    Get all values from the leaderboard worksheet.
    Sort the values array to get top scores first on the list.
    Print out username and score of the top 5 results
    """
    def score_value_key(elem):
        return elem[1]

    data = SHEET.worksheet("leaderboard")

    values = data.get_all_values()

    values.sort(key=score_value_key, reverse=True)

    slow_print("Top 5 users\n", 4./90)

    slow_print("Username\t Score\n", 4./90)

    for index in range(0, 5):
        print(f"{values[index][0]}\t\t {values[index][1]}\n")


def display_result():
    """
    Print the score and ask the user if they are interested in replaying.
    Calls update_leaderboard function to add user name and score Google Sheets
    If the user chooses to play again, the replay_quiz function will be called.
    If the user decides not to play again, the application will quit.
    """

    slow_print(f"Congratulations {user_name}, on completing the quiz!\n", 4./90)

    play_again = ""

    slow_print(f"You scored {score}/10\n", 4./90)

    data = [user_name, score]

    update_leaderboard(data)

    display_leaderboard()

    while play_again not in ["y", "n"]:
        play_again = input("Would you like to replay the quiz? (y/n)\n")

        if(play_again not in ["y", "n"]):
                slow_print("Invalid Input! Please enter yes (y) or no (n)\n", 4./90)

        if play_again.lower() == "y":
            slow_print("Restarting quiz....\n", 4./90)
            replay_quiz()
        elif play_again.lower() == "n": 
            slow_print(f"Thank you {user_name}, for taking the quiz!\n", 4./90)
            slow_print("Quitting application.....", 4./90)
            quit()


def replay_quiz():
    """
    Prints restarting messages and calls run_quiz function.
    """

    global score

    score = 0

    slow_print("Restarting the quiz\n", 4./90)

    slow_print(f"Best of luck {user_name}\n", 4./90)

    clear_terminal()

    run_quiz()

def main(): 
    """
    Call program main functions
    """

    quiz_information()

    begin_quiz()

    run_quiz()


main()