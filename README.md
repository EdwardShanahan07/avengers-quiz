# Avengers Quiz
The Avengers Quiz is an application where users can test their knowledge 
on the Marvel Avengers movie series. The quiz is a command-line application built with Python, users of the application are to be asked ten questions and their score is kept track of throughout the duration of the quiz. Once the user finishes the quiz, the user will see their result along with a leaderboard of previous users results. Google Sheets will keep track of the leaderboard and display the results at the end of the quiz. Users will be able to retry the quiz if they so choose.

[Deployed Site](https://avengers-quiz-app.herokuapp.com/)

## Contents 

- [User Experience](#user-experience)
  - [Flowchart](#flowchart)
  - [User Stories](#user-stories)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## User Experience 

### Flowchart
The flowchart describes how the program will run and give me an idea of what functions and logic are needed.
![](./readme-assets/img/flowchart.jpg)

### User Stories 
- As a user, I want to see instructions on how the quiz works. 
- As a user, I want to enter my name. 
- As a user, I want the choice to play or quit the application. 
- As a user, I want to see the question and multiple-choice options. 
- As a user, I want to see if my answer choices were correct or incorrect. 
- As a user, I want to keep track of what question number I am on. 
- As a user, when I finish the quiz, I want to see my score. 
- As a user, I want to see previous users' scores on a leaderboard. 
- As a user, I want to choose to replay or quit the application. 

## Testing

### Bugs 

#### Fixed Bugs 
- When printing the logo, I got the error message "EOL while scanning string literal." Two main reasons for this error message are missing quotes or strings spanning multiple lines. The Avengers logo spans numerous lines, I added triple quotes to the string and it fixed the error.

## Deployment 

### Local Deployment
To deploy this project locally, use Git clone in the terminal:
```console
git clone https://github.com/EdwardShanahan07/avengers-quiz.git
```

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

### Content
- Code Institute [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) code helped to connect application to Google Sheets API
- The quiz questions used are from [PONLY](https://ponly.com/marvel-trivia-quiz/)
- Simulate typing effect in the terminal [Slack Overflow](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
- Avengers logo was generated from [Emoji Combos](https://emojicombos.com/avengers-symbol)

### Media
- [FigJam](https://www.figma.com/figjam/) was used to create the flowchart.
