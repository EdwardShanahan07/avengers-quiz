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
    Get users name and prompt the user if they wish to play the quiz
    """

    global user_name
    
    user_name = input("Please enter your name\n")

    play_quiz = ""

    while play_quiz not in ["y", "n"]:
        play_quiz = input(("Do you want to begin the quiz? (y/n)")).lower()

        if(play_quiz == "n"):
            print(f"Thank you {user_name}, please try the quiz another time!")

            quit()


def run_quiz ():
    """
    Loop through quiz_data and print question and options.
    Prompt the correct answer and check if the answer is correct or incorrect
    """
    global score

    for quiz in quiz_data:
        answer = ""
        while answer not in ["a", "b", "c", "d"]:
            
            print(quiz["question"] + "\n")

            for option in quiz["options"]:
                print(option)

            print("\n")

            print("Please enter your answer (a, b, c, or d): ")

            answer = input()

            print("\n")

        if(answer == quiz["answer"]):
            print("Correct answer\n")

            score += 1
        else:
            print("Incorrect answer\n")

        print("------------------------------------------ \n")

            

def load_quiz_information():
    """ 
    Print the avengers logo and information about the quiz 
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



def main(): 
    """
    Call programs main functions
    """

    load_quiz_information()

    begin_quiz()

    run_quiz()


main()