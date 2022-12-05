# Football Stars
Readme from https://github.com/Christo107/Training_Quiz/blob/main/README.md

Football Stars is a text-based game where everything is determined by the randomly generated statistics. You will never experience the same game twice.

The live website on Heroku can be accessed at the following link: [View my Live Website on Heroku here](https://football-stars.herokuapp.com/)

## CONTENTS

* [Features](#features)
    *  [Team selection](#trainee-name-request)
    *  [Team statistics](#introduction-and-instructions)
    *  [Game events](#questions)
    *  [Attack/defend](#final-score-and-thank-you)
    *  [Targets and Outcomes](#results-worksheet)
    *  [Input Validation]
    *  [Ascii Art]
* [User Experience](#user-experience)
    *  [User Stories](#user-stories)
* [Design](#design)
    *  [Process Flow](#process-flow)
    *  [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)   
    *  [Languages Used](#languages-used)
    *  [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [User Story Testing](#user-story-testing)
    * [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)

## Features

### Existing Sections
- #### **Team Selection**
    - The game has 10 preset team names.
    - The user is presented with a list of 5 of those randomly chosen
    - The user selects the team.
    - Their choice of team is then removed from the team list and 1 of the reamining teams is chosen as the opposition.

![Team Selection Image]()
![Team chosen image]()

- #### **Team Statistics**
    - 
    
![Introduction and Instructions image](./assets/documentation/images/intro_instructions.jpg)

- #### **Questions**
    - The questions appear one at a time, along with the 3 possible options
    - There is then a space for the user to enter their answer along with a further reminder that the options are only a, b or c.

![Question Format image](./assets/documentation/images/question_format2.jpg)

- #### **Final Score and Thank you**
    - once the user reaches the end of the quiz, the trainee is congratulated and told their final score.
    - A message appears informing them that the results worksheet is being updated
    - They are thanked and wished a nice day

![Final Score and Thank You image](./assets/documentation/images/final_window.jpg)

- #### **Results Worksheet**
    - This Google sheet contains all the trainees who have completed the quiz along with the score they achieved. 

![Results Worksheet Image](./assets/documentation/images/result_worksheet.jpg)

### Future Features
- Future improvements will include logging the incorrect answers of the trainee for the teacher to identify areas that need improvement.
- Username validation - If two users have the same name, an error will appear to ask them to enter an initial to distinguish them.

## User Experience
A number of features have been added to improve the user experience while using the app. These include adding a pause between lines of text appearing to avoid bombarding the user with too much information at one time. Also, the screen is cleared after the introduction and after each question, to de-clutter the interface for the user. The user is asked whether they would like to proceed with the quiz rather than starting automatically.
### User Stories
#### Client Goals
- As a trainer/teacher, I want to be able to keep a log of the trainees who have completed the quiz, so I can follow up with any who haven't yet.
    * I tested that the username of the trainees is passed to the results worksheet only after they complete the quiz. **Passed**
- As a trainer/teacher, I want to be able to keep a log of the the scores each trainee got, so I know if they require further training.
    * I tested that the score of the trainees is passed to the results worksheet as they complete the quiz, and is listed on the same row to avoid mistakes. **Passed**
- As a trainer/teacher, I want the trainees to be able to access the quiz without any problem, so they can complete the quiz
    * I tested that the users could complete the quiz without issue. **Passed**
#### User Goals
- As a trainee, I want to be able to enter my name and proceed with the quiz, so I can find out my how well I know the training material
    * I tested that the trainee can enter a username and proceed with the quiz. **Passed**
- As a trainee, I want to be able to understand what the quiz consists of, so I know how long it will take
    * I tested that the instructions for the quiz are displayed each time a trainee begins the quiz. **Passed**
- As a trainee, I want to be able to proceed when I am ready, so I can be prepared to answer the questions
    * I tested that the trainee can only proceed if they answer Y to the "ready to proceed" question. **Passed**
- As a trainee, I want to be able to see which questions I get wrong, so I know what I need to study more
    * I tested that the incorrect answers are flagged to the user as they go through the quiz. **Passed**
- As a trainee, I want to be able to see my final score, so I know how I did in the quiz
    * I tested that the final score is displayed to the trainee when they complete the quiz. **Passed**

## Design
- The design of the quiz is simple and straightforward in nature. How the quiz is to be used did not require any visual image elements, and these would be a distraction for the trainee. I wanted to first provide instructions to the user so they understood what was required of them to complete the quiz. also, where errors could be made, I wanted to provide feedback to guide back to where they should be.
- The code uses a loop to iterate through the questions and answers. If the question bank needs to be expanded in future, a separate file may be created to store these.
- To make completing the quiz a more pleasant experience, pauses have been added at specific points, and the screen is cleared down to avoid "option paralysis"

### Process Flow
Below is a flow chart to demonstrate the actions that take place while using the app

![Process Flow Chart Image](./assets/documentation/images/app_process_flow.png)

### Accessibility
The app provides feedback to the user at various stages to instruct them if they have made an error, for example, if they do not enter a name at the beginning, they are instructed to enter a name to proceed. 

## Technologies used
- Snipping Tool for screenshots
### Languages used
- Python

### Frameworks, Libraries and Programs used
- [GitHub](https://github.com)
- [Gitpod](https://gitpod.io/workspaces)
- [Heroku](https://www.heroku.com)
- [Chrome Dev Tools](https://www.google.com/intl/en_ie/chrome/)

## Testing

### Validator Testing
- The code was run through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) and showed no errors.
[CI Python Linter Result Image](./assets/documentation/images/ci_python_linter_result.jpg)
### User Story Testing
- I used the user stories to perform manual testing on the quiz to see whether there were any blockers to the user goals identified above. The results are listed above in the [User Stories](#user-stories) section

## Bugs
### Fixed Bugs
- **Start Quiz Welcome message bug** – If the user didn’t enter name, but instead hit enter, but then entered name a second time, they wouldn’t receive the personalised welcome message
    - Fix – Added if statement to restart start_quiz function if name not entered
- **Question text not appearing bug** – the questions weren’t appearing in the run_quiz function, only the answers.
    - Fix - Added while loop to print question text
- **Screen Clearing bug** – I wanted each question to appear on it’s own on each page, to avoid clutter, but the screen was clearing before the correct answer and score was appearing.
    - Fix - Added os clear functionality at certain points to de-clutter user interface
- **Proceed if not y or n bug** - A bug whereby the quiz would start no matter what letter you would put in the "ready to begin(y/n) field. 
    - Fix - Added while loop to stop keep asing question until either y or n entered.
- **Proceed if N twice Bug** - when the user is first asked if they'd like to proceed, and they answer n, a warning is shown to tell them it is a mandatory quiz and they must complete it before their deadline. The question of proceeding(y/n) is then displayed again. If they answer n again, the quiz still commences.
    - Fix - To fix this bug, I decided to change my approach to the validation. Instead of having an if statement that looked at what to do if = y, then what to do elif = n, I incorporated the code into the above while loop, which displays an instruction to enter y to begin, or else complete at another time. This stopped a user proceeding until they enter y to the question.
    ```
    while begin_quiz != "y":
        begin_quiz = input(f"Please enter 'y' to begin {NAME}, else "
                           "complete the quiz another time: ")
    ```

### Known Bugs
- **Correct answer bug** – if a user chose the incorrect answer, the program should tell them what the correct answer was. There was a bug where the correct answer wasn’t displaying correctly, with parentheses and commas. This bug still exists, so I have removed the need to show the full value of the correct answer, instead ony showing the initial a,b or c until a fix can be found

![Correct Answer bug](./assets/documentation/images/correct_answer_bug.jpg)

## Deployment
The project was deployed on Heroku using the following method:
1. Add dependencies in GitPod to requirements.txt file with command "pip3 freeze > requirements.txt"
2. Commit and push to GitHub as usual
3. Go to the Heroku Dashboard
4. Click "Create new app"
5. Name app and select location
6. Add Config Vars for Creds and Port in Settings tab
7. Add the buildbacks to Python and NodeJS in that order.
8. Select appropriate deployment method e.g. GitHub
9. Connect to Github and link to repo
10. Enable Automatic Deploys and deploy manually
11. Click on Deploy.
## Credits
- Run_quiz function based on code by Leah Fisher https://github.com/cornishcoder1/Food_of_Japan_Quiz with suggestions by Declan_5P(Slack username) and [Sean Young-aluminati](https://github.com/seanyoung247).
- Exporting results functionality based on Love_Sandwiches demo project by CI.
- Jason Dunton for his advice certain aspects of my project