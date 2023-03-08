import gspread
from google.oauth2.service_account import Credentials
from time import sleep

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


quiz_data = [
    {
    "question": "During which war did Captain America get his superhuman abilities?", 
    "options": [
    "(a) Civil War", 
    "(b) World War I", 
    "(c) World War II", 
    "(d) The Cold War"],
    "answer": "c"
    },
    {
    "question": "Who is the villain in Guardians of the Galaxy: Vol 1?", 
    "options": [
    "(a) Thanos", 
    "(b) Ronan The Accuser", 
    "(c) Obidiah Stane", 
    "(d) Yondu Udonta"],
    "answer": "b"
    },
    {
    "question": "Which of the following characters did not disappear during the ”blip”?", 
    "options": [
    "(a) Spiderman", 
    "(b) Black Panther", 
    "(c) Doctor Strange", 
    "(d) Rocket"],
    "answer": "d"
    },
    {
    "question": "Which of the following characters dies in Avengers (2012)?", 
    "options": [
    "(a) Nick Fury", 
    "(b) Steve Rogers", 
    "(c) Phil Coulson", 
    "(d) Maria Hill"],
    "answer": "c"
    },
    {
    "question": "What is Mjölnir?", 
    "options": [
    "(a) Loki’s Scepter", 
    "(b) Captain America’s Shield", 
    "(c) Winter Soldier’s Arm", 
    "(d) Thor’s Hammer"],
    "answer": "d"
    },
    {
    "question": "In Avengers Infinity War, Tony Stark tells Bruce Banner: “You are embarrassing me in front of the…”",
    "options": [
    "(a) Magicians", 
    "(b) Avengers", 
    "(c) Aliens", 
    "(d) Wizards"],
    "answer": "d"
    },
    {
    "question": "Who is the first avenger to meet Nick Fury?", 
    "options": [
    "(a) Captain Marvel", 
    "(b) Captain America", 
    "(c) Iron Man", 
    "(d) Black Widow"],
    "answer": "a"
    },
    {
    "question": "What does Thanos want to bring to the universe?", 
    "options": [
    "(a) Hope", 
    "(b) Balance", 
    "(c) Peace", 
    "(d) Destruction"],
    "answer": "b"
    },
    {
    "question": "How did Steve Rogers and Sam Wilson meet for the first time?", 
    "options": [
    "(a) While running", 
    "(b) At a bar", 
    "(c) In the army", 
    "(d) At a museum"],
    "answer": "a"
    },
    {
    "question": "In which Marvel Phase was Ant Man introduced?", 
    "options": [
    "(a) Phase 1", 
    "(b) Phase 2", 
    "(c) Phase 3", 
    "(d) Phase 4"],
    "answer": "b"
    },
]

user_name = ""
score = 0

def begin_quiz():
    """
    Get users name and prompt the user if they wish to play the quiz.
    """

    global user_name
    
    user_name = input("Please enter your name\n")

    play_quiz = ""

    while play_quiz not in ["y", "n"]:
       
        play_quiz = input(("Do you want to begin the quiz? (y/n) \n")).lower()

        if(play_quiz == "n"):
            print(f"Thank you {user_name}, please try the quiz another time!")

            quit()

        if(play_quiz not in ["y", "n"]):
                print("Invalid Input! Please enter yes (y) or no (n)\n")

def display_question(index, question, options):
    """
    Print questions and loop through options array and print each value
    """

    print(f"Question {index}/10 \n")

    print(question + "\n")

    for option in options:
        print(option)

    print("Please enter your answer (a, b, c, or d): ")


def check_answer(answer, question_answer):
    """
    Checks the answers to the questions if both values are equal. 
    One point will be added to the score. 
    If the answer is wrong no points will be added.
    """
    global score

    if(answer.lower() == question_answer.lower()):
        print("Correct answer\n")

        score += 1
    else:
        print("Incorrect answer\n")


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

            answer = input().lower()

            print("\n")

            if(answer not in ["a", "b", "c", "d"]):
                print("Invalid Input! Please enter a, b, c, or d\n")

        check_answer(answer, quiz["answer"])

        print("------------------------------------------ \n")

    display_result()

            
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

    print("Please enter a, b, c, or d and hit the enter key to answer the question\n")


def update_leaderboard(data):
    """
    Add user-name and score to Google Sheets
    """

    print("Exporting your results to database....\n")

    update_workout = SHEET.worksheet("leaderboard")
    update_workout.append_row(data)

    print("Results exporting successfully!!\n")

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

    print(values)

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

    print(f"Congratulations {user_name}, on completing the quiz!\n")

    play_again = ""

    print(f"You scored {score}/10\n")

    data = [user_name, score]

    update_leaderboard(data)

    sleep(4)

    display_leaderboard()

    while play_again not in ["y", "n"]:
        play_again = input("Would you like to replay the quiz? (y/n)\n")

        if(play_again not in ["y", "n"]):
                print("Invalid Input! Please enter yes (y) or no (n)\n")

        if play_again.lower() == "y":
            print("Restarting quiz....\n")
            replay_quiz()
        elif play_again.lower() == "n": 
            print(f"Thank you {user_name}, for taking the quiz!\n")
            print("Quitting application.....")
            quit()


def replay_quiz():
    """
    Prints restarting messages and calls run_quiz function.
    """

    global score

    score = 0

    print("Restarting the quiz\n")

    print(f"Best of luck {user_name}\n")

    run_quiz()

def main(): 
    """
    Call program main functions
    """

    quiz_information()

    begin_quiz()

    run_quiz()


main()