# Avengers Quiz
The Avengers Quiz is an application where users can test their knowledge 
on the Marvel Avengers movie series. The quiz is a command-line application built with Python, users of the application are to be asked ten questions and their score is kept track of throughout the duration of the quiz. Once the user finishes the quiz, the user will see their result along with a leaderboard of previous users results. Google Sheets will keep track of the leaderboard and display the results at the end of the quiz. Users will be able to retry the quiz if they so choose.

## Contents 

- [User Experience](#user-experience)
  - [Flowchart](#flowchart)
  - [User Stories](#user-stories)
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

## Credits

### Content
- Code Institute [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) code helped to connect application to Google Sheets API
- The quiz questions used are from [PONLY](https://ponly.com/marvel-trivia-quiz/)
- Simulate typing effect in the terminal [Slack Overflow](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
- Avengers logo was generated from [Emoji Combos](https://emojicombos.com/avengers-symbol)

### Media
- [FigJam](https://www.figma.com/figjam/) was used to create the flowchart.