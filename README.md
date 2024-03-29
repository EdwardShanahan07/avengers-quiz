# Avengers Quiz
The Avengers Quiz is an application where users can test their knowledge 
on the Marvel Avengers movie series. The quiz is a command-line application built with Python, users of the application are to be asked ten questions and their score is kept track of throughout the duration of the quiz. Once the user finishes the quiz, the user will see their result along with a leaderboard of previous users results. Google Sheets will keep track of the leaderboard and display the results at the end of the quiz. Users will be able to retry the quiz if they so choose.

[Deployed Site](https://avengers-quiz-app.herokuapp.com/)

## Contents 

- [User Experience](#user-experience)
  - [Flowchart](#flowchart)
  - [User Stories](#user-stories)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Libraries](#libraries)
  - [Programs Used](#programs-used)
- [Testing](#testing)
  - [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Known Bugs](#known-bugs)
  - [Manual Testing](#manual-testing)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Acknowledgments](#acknowledgments)

## User Experience 

### Flowchart
The flowchart describes how the program will run and give me an idea of what functions and logic are needed.
![](./readme-assets/img/flowchart.jpg)


### User Stories 
- As a user, I want to see Avengers logo and welcome message. 
- As a user, I want to see instructions on how the quiz works. 
- As a user, I want to create my user name. 
- As a user, I want the choice to play or quit the application. 
- As a user, I want to see the question and multiple-choice options. 
- As a user, I want to see if my answer choices were correct or incorrect. 
- As a user, I want to keep track of what question number I am on. 
- As a user, when I finish the quiz, I want to see my score. 
- As a user, I want to see previous users' scores on a leaderboard. 
- As a user, I want to choose to replay or quit the application. 

## Features 

### Welcome
![](./readme-assets/img/feature-welcome.png)

### Instructions 
![](./readme-assets/img/feature-information.png)

### Create User Name
![](./readme-assets/img/feature-username.png)

### Quiz Questions
![](./readme-assets/img/feature-questions.png)

### Results
![](./readme-assets/img/feature-results.png)

### Leaderboard
![](./readme-assets/img/feature-leaderboard.png)

### Play Again
![](./readme-assets/img/feature-replay.png)

## Technologies Used

### Languages 

- Python

### Libraries 

- os library was used to clear the terminal.
- time library was used to pause the terminal for a short duration.
- gspread was used to connect application to Google Sheets.
- google.oauth2.service_account grants the application access to Google Cloud API

### Programs Used

- Git was used for version control
- GitHub to store applications code
- GitPod was used to code the application
- [FigJam](https://www.figma.com/figjam/) was used to create the flowchart.


## Testing

### Validation
I used the [Code Institute Python](https://pep8ci.herokuapp.com/) Linter to check validation. I got multiple "line too long" error messages in both run.py and questions.py. I fixed both files, and no errors are appearing at this time.

<details>

  <summary>PEP8 questions.py before:</summary>

  ![](./readme-assets/img/validation-questions-before.png)

</details>

<details>

  <summary>PEP8 questions.py after:</summary>

  ![](./readme-assets/img/validation-questions-after.png)

</details>

<details>

  <summary>PEP8 run.py before:</summary>

  ![](./readme-assets/img/validation-run-before.png)

</details>

<details>

  <summary>PEP8 run.py after:</summary>

  ![](./readme-assets/img/validation-run-after.png)

</details>

### Bugs 

#### Fixed Bugs 

| Bug | Error Message |  Fix |
| -------------        |     -------------      |         ------------- |
| Logo not printing to the terminal  | "EOL while scanning string literal."    | The logo spans multiple lines of code. I used triple quotations to fix this error.    |
| No validation when entering user name  | None   | Added validate_username function. This function will check for validation    |
| display_leaderboard not sorting list by score properly. |  None   | Added sort_by_score function. This function will return the score as an integer. When the leaderboard is displayed it will sort by the highest score first     |

### Known Bugs
No known bugs at this time.

### Manual Testing

| Feature | Expected Outcome |  Testing Performed  | Result | Pass/Fail |
| -------------        | -------------      | ------------- | ------------- | ------------- |
Logo and welcome message | When the application begins, the Avengers logo and welcome message should display. | None | Logo and welcome message displayed correctly. | Pass |
Quiz Information | Information about the quiz and how to play should be displayed. | None | Quiz information displayed correctly  | Pass |
Create username | Option to enter user name| Typed my username | Enter my user name without any issues. | Pass |
Play quiz | Choose to play or quit the quiz.| Type "y" to play the quiz. Type "n" to quit the quiz. | Quiz started when "y" key entered.  Application closed when the "n" key was entered. | Pass |
Question and multiple choice option | The question and the four possible options should be displayed.| None | The question and four multiple-choice answers were displayed correctly.  | Pass |
Check if my answer is correct or incorrect. | After I enter my answer, I should see if my answer is correct or incorrect.| Entered an option, and it was correct. I tested the next question, and the option was incorrect.|   | Pass |
Keep track of the quiz's progress.  | I should see what question number I am on.| None | Question progress is updated with every question.  | Pass |
Display results of quiz  | When I finish the quiz, I should see my result.| None | Result displayed correctly  | Pass |
Display Leaderboard  | Leadboard should display with the scores of the top five users.| None | Leaderboard displayed correctly.  | Pass |
Display Leaderboard  | Leadboard should display with the socre of the top five users| None | Leaderboard displayed correctly  | Pass |
Replay quiz  | Option to replay or quit the quiz.z| Enter "y" to restart the quiz. Enter "n" to quit the application.  | The quiz restarted when "y" was entered, and the application closed when "n" was entered.  | Pass |



## Deployment 

### Local Deployment

#### How to Clone
1. Open up a terminal
2. Change to the directory where you want the location of the cloned depository 
3. Copy the code below and paste it into the terminal:
```console
git clone https://github.com/EdwardShanahan07/avengers-quiz.git
```
4. Hit the enter key to clone the depositiry

#### How to Fork
1. Login or signup to Github
2. Search for this repository: [EdwardShanahan07/avengers-quiz](https://github.com/EdwardShanahan07/avengers-quiz)
3. Ont the top right corner, click Fork

### Heroku Deployment
These steps were used to deploy this app using [Heroku](https://www.heroku.com/):

1. In GitPod, add the list of requirements using this command in the terminal "pip3 freeze > requirements.txt".
2. Commit and push code to Github.
3. Sign up or log in to Heroku.
4. On the Heroku dashboard, locate the "New" button and select "Create New App".
5. Enter the app name and make sure it's a unique name.
6. Enter your region.
7. Click the "Create App" Button.
8. Navigate to the "Settings" tab. 
9. Under the "App Information" Section, locate the "Reval Config Vars" and click it.
10. Add the first variable.
11. Set the value of "KEY" input to "CREDS" and copy the creds.txt file in GitPod.  Paste the content into the value input.
12. Click the "Add" button to save the variable.
13. Add the second variable.
14. Set the value of "KEY" to "PORT" and the value to "8000".
15. Click the "Add" button to save the variable.
16. Underneath the "Config Vars" section, locate the Buildpacks section, and click the "Add Buildpack" button.
17. Select "Python" as the first Buildpack and save changes.
18. Add another Buildpack by clicking the "Add Buildpack" button again.
19. Select "nodejs" as the second Buildpack.
20. Scroll back up to the menu and select the "Deploy" tab.
21. Click "GitHub" as the Deployment Method.
22. Search for your repo name and click the "Connect" button.
23. Click the "Enable Automatic Deploys" button under the GitHub Connect section.
24. Ensure the "main branch" is selected and click the "Deploy branch" button.
25. Once the app is built, a "View"  button will appear. 
26. Click the "View" button to see the application deployed.

## Credits

### Code Used
- Code Institute [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) code helped to connect application to Google Sheets API

### Content
- The quiz questions used are from [PONLY](https://ponly.com/marvel-trivia-quiz/)
- Avengers logo was generated from [Emoji Combos](https://emojicombos.com/avengers-symbol)

### Acknowledgments 

Thanks to Code Institute for helping me build this application with their course content.

Thanks to friends and family for testing this application.

Thanks to my mentor, Jubril Akolade, for feedback on this project.
