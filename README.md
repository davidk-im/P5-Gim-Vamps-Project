# Project Plan
Group Members: Kyle Myint, Lucas Bruner, Ava Brooks, David Kim

## 1/15 Scrum Team Tickets
[1.](https://github.com/kylem314/P5-Gim-Vamps-Project/projects/1#card-52921614) Create database to store Username and Password information from completing the signup form on signup.py
* Created [flaskmain.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py) with POST method to push username and password information to database. If else statement used, else code used, to test for errors in code. 
* Created [user.py](https://gist.github.com/avabrooks/ea2f743a91e594ddd5afc01387217f3b) to create functions defining the database and the variables in it. 
* Created [chess.db](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/chess.db) to store usernames and passwords. Also created a blank one in case of error. 
* How to run: 
    1. From home page select sign up button. 
    2. Fill out the 3 fields, the form will not go through without filling out all fields.The form will also not go through if your passwords do not match(CSS integration).
    3. After creating your account, you will be redirected to the play menu, where the chess games will soon be implemented.
    4. Example of completed code showing data in database [here](https://docs.google.com/document/d/1FsY9-SmcStAdhVpmfUdrwxXERZDZkiBrXjHaocRAvAM/edit)
    5. Goal for next week: Connect database so users can log in. 
 
[2.](https://github.com/kylem314/P5-Gim-Vamps-Project/projects/1#card-52931009) Design, and create the leaderboards page to eventually be used with a database.
* Created [leaderboards.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/leaderboards.html)
* Used a variety of CSS styles to make it look really beautiful
* How to run:
    1. Starting at the home page, select the leaderboards button.
    2. Scroll down and view various users' ELO, their amount of wins, and their spot on the board.
    3. Eventually, upon completion of a game and gaining/losing some ELO, you can then have the option to go straight to the leaderboards to see where you have moved to.
[3.](https://github.com/kylem314/P5-Gim-Vamps-Project/projects/1#card-52619938) Formulate and code the ELO ranking system for users
* Created a [separate repository](https://repl.it/@KyleMyint/Chess-ELO-System#main.py) to keep code for now
* Once the database for users is set up on the website, this code could be integrated in order to give or take away ELO points based on games or puzzles a user completes
* How to run:
    1. Run repl code
    2. Type "1" to see the score for running a tactic puzzle
    3. Type "Alex" to see what score user Alex would recieve after completing said puzzle (Note: in temp 'database', Alex has an initial ELO of 1300 for tactics, and a streak of 3 wins
    4. Type "y" to see what Alex would get if he were to solve the puzzle correctly - in this case, he gains 11 points
    5. Read comments on main.py to see the formula and thought process behind our ELO system
4. 

(links to each ticket are linked on the number)

### Scrum Master Grading: 
Score: number/20<br>
Highlight 3-4 goals completed by team here


## Website URL: 
http://chessthegame.cf
## Website Direct IP
http://76.176.72.123:3000/

## Summary: 
Create a chess-based website using Python, Flask, SQLAlchamy, and a Raspberry Pi with an internet domain that has the following features:
* Username/Password login system w/ profiles
* Database of profiles with statistics based on previous games
    * For example, a user could search for their win rate against another user, or find their games with that user
* Be able to view match history, and see game codes to see your past games
* Play against other players, or against an AI with different difficulties
* Be able to replay past games from a database
* Rules & Settings

## Big Ticket Goals:
* A working chess game, integrated into our website
* Profile system using a database, where people can find data such as past games, winrate, etc.
* Menu to navigate to all parts of the website

## Home Page
![Home](https://i.imgur.com/gNVUUmI.png)

## About Us Page
![About Us](https://i.imgur.com/wd0f1Ut.png)

## Incorporating College Board Requirements: 
* Big Idea 1: Creative Development
    * Use web and program designs to create a plan for the project(project plan in README.md)
    * Create Scrum Boards to track progress and development of the project
    * Use graphics/storyboard to plan the website design 
* Big Idea 2: Data
    * Using a SQLAlchemy database to save user information 
        *Use this information for user login
    *Database for storing information such as past chess games with moves, win/loss statistics, and win rates versus other players
* Big Idea 3: Algorithms and programming
    * Use graphics/storyboard to plan the website design/UI 
        * Want a simple, professional look color and design wise
    *Create design with HTML and CSS
* Big Idea 4: Computer Systems and Networks
    * Deploying website using a raspberry pi that runs 24/7
        * Internet domain
    * Using GET/POST
        * User information and login
        * Past game information
* Big Idea 5: Impact of computing
    * Website will not be used for illegal or malicious purposes
    * Players can learn or strengthen their chess skills by using our website
    * User credentials are secure and have protection from database leaks
    * Crediting work from first trimester to those who created that code

## Tracking Sheet/Schedule:
* Found on Repo, created a scrum board found in projects
    * Has 5 tracking steps: backlog, assigned, in progress, ready for deploy, and completed 
* Delivery plans/deadlines for big milestones
* Big ticket features with visuals

## Table of Collaborators:
| Name | Github ID |
| ------------- | ----------- | 
|Kyle Myint | kylem314 |
|Lucas Bruner | notkobalt |
|Ava Brooks | avabrooks |
|David Kim | DavidKim37 |

## Link To Project Plan:
https://docs.google.com/document/d/1ksmFpIRDhS-dvuICdMOBlyGIHcLlXs96FeMo1Ji3Azw/edit




