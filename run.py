from time import sleep
import os
import sys
import gspread
from google.oauth2.service_account import Credentials
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
    Pauses the terminal for 2 seconds and clears the terminal
    """
    sleep(2)

    os.system('clear')


def validate_user_name(user_name):
    """
    Validates user_name input to see if it matches the criteria.
    """
    if user_name == "":
        print("Please don't enter an empty value!\n")
    elif len(user_name) > 12:
        print("Name shouldn’t be more than 12 chartectors long!\n")
    elif len(user_name) < 3:
        print("Name shouldn’t be less than 3 chartectors!\n")
    else:
        return True


def display_question(index, question, options):
    """
    Print questions and loop through options array and print each value
    """

    print(f"Question {index}/10 \n")

    print(question + "\n")

    for option in options:
        print(option)

    print("Please enter your answer (a, b, c, or d):\n")


def check_answer(answer, question_answer):
    """
    Checks the answers to the questions if both values are equal.
    One point will be added to the score, if the answer is correct.
    If the answer is wrong no points will be added.
    """
    global score

    if answer.lower() == question_answer.lower():
        print("Correct answer!\n")

        score += 1
    else:
        print("Incorrect answer!\n")


def sort_by_score(elem):
    """
    Sort the leaderboard list by the score value
    and returns the value into integer.
    """
    return int(elem[1])


def quiz_information():
    """
    Print the Avengers logo and information about the quiz.
    """

    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
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
⠀⠉⠉⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n""")

    print("Welcome to the Avengers quiz!\n")

    print("Take this quiz to see how well you know the Marvel film series, Avengers.\n")

    print("There are ten questions in total, and all questions are multiple-choice.\n")

    print("The choices are a, b, c, and d for all ten questions.\n")

    print("Please enter a, b, c, or d and hit the enter key to answer the question.\n")


def begin_quiz():
    """
    Get user name and prompt the user if they wish to play the quiz.
    """

    global user_name
    while True:
        user_name = input("Please enter your user name and hit the enter key:\n").strip()

        if validate_user_name(user_name):
            break

    play_quiz = ""

    while play_quiz not in ["y", "n"]:
        play_quiz = input(("Do you want to begin the quiz? (y/n) \n")).lower()

        if play_quiz == "n":
            print(f"Thank you {user_name}, please try the quiz another time!")

            sys.exit()

        if play_quiz not in ["y", "n"]:
            print("Invalid Input! Please enter yes (y) or no (n)\n",)

    clear_terminal()


def run_quiz():
    """
    Loop through quiz_data and print questions and options.
    Request the correct answer and verify whether the answer
    is correct or incorrect.
    """

    for index, quiz in enumerate(quiz_data, start=1):
        answer = ""

        while answer not in ["a", "b", "c", "d"]:

            display_question(index, quiz["question"], quiz["options"])

            answer = input("\n").lower()

            print("\n")

            if answer not in ["a", "b", "c", "d"]:
                print("Invalid Input! Please enter a, b, c, or d\n")

        check_answer(answer, quiz["answer"])

        clear_terminal()

    display_result()


def update_leaderboard(data):
    """
    Add user-name and score to Google Sheets
    """

    print("Exporting your results to database....\n")

    update_workout = SHEET.worksheet("leaderboard")
    update_workout.append_row(data)

    print("Results exported successfully!!\n")


def display_leaderboard():
    """
    Get all values from the leaderboard worksheet.
    Sort the values array to get top scores first on the list.
    Print out username and score of the top 5 highest vales
    """

    data = SHEET.worksheet("leaderboard")

    values = data.get_all_values()

    values.sort(key=sort_by_score, reverse=True)

    print("Top 5 users\n")

    print("Username\t Score\n")

    for index in range(0, 5):
        print(f"{values[index][0]}\t\t {values[index][1]}\n")


def display_result():
    """
    Print the score and ask the user if they are interested in replaying.
    Calls update_leaderboard function to add user name and score Google Sheets
    If the user chooses to play again, the replay_quiz function will be called.
    If the user decides not to play again, the application will quit.
    """

    global score

    print(f"Congratulations {user_name}, on completing the quiz!\n")

    play_again = ""

    print(f"You scored {score}/10\n")

    data = [user_name, score]

    update_leaderboard(data)

    display_leaderboard()

    while play_again not in ["y", "n"]:
        play_again = input("Would you like to replay the quiz? (y/n)\n")

        if play_again not in ["y", "n"]:
            print("Invalid Input! Please enter yes (y) or no (n)\n")

        if play_again.lower() == "y":
            print("Restarting quiz....\n")
            score = 0
            replay_quiz()
        elif play_again.lower() == "n":
            print(f"Thank you {user_name}, for taking the quiz!\n")
            print("Quitting application.....")
            quit()


def replay_quiz():
    """
    Prints restarting messages and calls run_quiz function.
    """

    print("Restarting the quiz\n")

    print(f"Best of luck {user_name}\n")

    clear_terminal()

    run_quiz()


def main():
    """Call program main functions"""

    quiz_information()

    begin_quiz()

    run_quiz()


main()
