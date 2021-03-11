# Project Plan
Group Members: Kyle Myint, Lucas Bruner, Ava Brooks, David Kim
    
## Website URL: 
http://chessoffline.cf

## Website Direct IP
http://76.176.72.123:3000/

## [Commerical](https://www.youtube.com/watch?v=VVEMsOZa-p0)

## README Guidance 
### Planning on [Scrumboard](https://github.com/kylem314/P5-Gim-Vamps-Project/projects/1)
### Major Technicals:
* Web API(David)
  * Created an app route that takes in variables as a second argument [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py#L159-L169)
  * Created a dropdown menu that sends different modes of chest as the second argument on menu [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/base.html#L35-L43)
  * Formatted code so that everything would be accessed via variable input on html page [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/webapi2.html)
* ELO System(Kyle)
    * [Repl.it demonstration of the system](https://repl.it/@KyleMyint/Chess-ELO-System#main.py), thought process, and equations
        * Wow and thought process explained in comments in repl link
        * How to run:
        * Run repl (linked above)
        * Choose a mode and enter 1 or 2 of the usernames (found in accounts.txt)
    * When a game ends, the [elo function](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/elopupdate.py) is run, and the results are used to edit the user database with the new scores.
* Databases(Ava)
    * Chess.db holds 3 tables: user([found here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/user.py#L12-L22)), game, and game_move(both found [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/replaygamehtml.py#L8-L17)
        * User holds username/password info as well as ELO stats
        * Game holds game ids
            * Back end where game is created on [replaygame.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/replaygamehtml.py#L18-L34)
* Signup/Login(Ava)
    * Signup form is created on [signup.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/signup.html) where users input username and password
        * Includes elements of HTML5 [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/signup.html#L14) and java script [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/signup.html#L33-L45)
    * User_create function in [user.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/user.py#L30-L35) creates user and sends data to chess.db and default ELO scores are added
        * Back end uses POST to get info on [flaskmain.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py#L111-L121)
        * If successful, user is redirected to a signup confirm page
    * Login form is created on [login.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/login.html)
        * Uses validate_user function on [user.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/user.py#L46-L53) to check for inputted username in the database
            * Back end uses POST and calls validate_user function
            * If username is found and passwords match, user will be logged in
            * Login function uses flask attributes such as login_required, @login_manager.user.loader, and login_user
    * Profile.html page uses login_required
        * [Flaskmain.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py#L74-L77) grabs session info for username and 3 ELO scores which are displayed on [profile.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/profile.html) using jinja variables
    * How to run:
        1. If you are a new user, create an account by signing up
        2. Once signed up, you can either go straight to playing, or log in to see your current stats. 
        3. Start playing
* Raspberry Pi(Lucas)
    * Port forwarded Pi IP using internet console dashboard, this way other users can connect to it when the server is online.'
    * Used a free domain website to create a custom domain for the website that cloaks the original IP. ([URL](chessoffline.cf)
    * Runs on Gunicorn and Nginx
    * Since the Pi is always on, it runs 24/7!
    * Able to clone project on Pi using 'git clone' and can easily update with 'git pull'
* WOW(chess)(Ava/Kyle/David)
    * Creating game and storing data:
        * Each game id is unique using get_next_game function [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/replaygamehtml.py#L26-L41)
        * Functions [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/chessdata.py#L277-L303) on chessdata.py get usermove1, usermove2, color of the move, and the number in sequence of the move
        * Saves to database after each turn is done [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py#L184-L196) by calling [this function](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/replaygamehtml.py#L19-L23) from chessdata.py
        * Backend code and logic found in [chessdata.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/chessdata.py), [htmlToPython](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/htmlToPython.py), and [htmlToPythonAdditions](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/htmlToPythonAdditions.py)
    * Replaying a Game
        * Games are sorted by gameid in database
        * Use post to submit form with entered game id [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py#L127-L137)
        * Calls [get_game_replay](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/replaygamehtml.py#L43-L45) function that query's through database to find game id
        * Data is then printed accordingly [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/replaygamedata.html#L20-L28) using jinja forloops and variables
    * How to run:
        * Start new multiplayer game
            *Can play or just move a few pieces around for testing purposes
        * Remember game ID
        * Input game ID into replay game under play menu(some games with data already include 24 and 33)
     * Multiplayer games:
         * With the code from first trimester, the chess board is being stored in one place and cannot be duplicated on multiple webpages on the same device, thus making it hard to code and check using Intellij
         * Back end shows data updating by pulling and showing data on [joingamedata.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/joingamedata.html). Shows data being constantly updated after every move
              * How to run a test:
                   * Open 2 windows of the chess website
                   * On window 1, create a new multiplayer game and make as many moves as desired
                   * On window 2, input the game ID into join game, here you should be able to see all the moves coming from the other tab/user, modeling the multiplayer function
                   * By updating after every move and pulling on another tab, players are able to play at the same time
                       
### Incorporating College Board Requirements: 
* Creative development
    * Collaboration: 
Throughout the development of our website, we have collaborated with either partners or teams in order to complete different big ticket goals that we wouldn't have been able to complete on our own.  By ourselves, we wouldn't have been able to code a complete chess website, but with input and collaboration with a team, we were able to complete it.
    * Creative Development: 
This trimester's project built upon some of our work from the first trimester, in which we had coded a working game of chess in Python.  Here, we converted that program into a website, complete with databases and accounts for users to save their scores and data on previous games.  A challenge that our team faced in the development process was figuring out how to use Python functions with HTML code, but we managed to overcome it through saving data on databases in real time (which enabled playing the game with people on other devices) and using POST forms to extract data from the site.

* Data
    * Use data compression and extracting information from data to explore how computers use and handle data to produce information and solve problems
    * Store data for future use: 
Within our website, we store data on each game in a database as the game is played.  Users are able to view their past games, and we are able to search through the database to find relevant information which is used to replay the game.
    * Other uses: Data is stored in real time allowing for other users to 'pull' that data from a replaygame. This can be used to see other moves/strategies and connects users on the site by following the how to run instructions under the WOW/chess. 

* Algorithms and programming
    * Used for: 
Creating a function that can be used multiple times within a program, with variable inputs and outputs, in order to repeat a process in different locations.
    * In our project: 
We use algorithms in *many* different places, as they are useful in expediting portions of code. For example, in movepieceai, there is a [function](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/ba9db2517c6aa9f4fa7add61df93a5280ee885a8/movepieceai.py#L422) to evaluate moves which is run for every move possible given a certain board.
* Computer systems and networks
   * How computers and network systems work using the internet and parallel distributed computing
   * How to use multiple computers to split up work and make process faster
    * In our project, multiple computers and networks are used to make the games possible. The user's device connects with the backend on our server to ensure the most quality in our game as possible. 
* Impact of computing/ethics
   * Effect of computing on society, economy, culture, and everyday life
   * Legal and ethical responsibilities as a programmer
   * Digital divide, computing bias, and safe computing
    * In our project, you can clearly see the impact of ethics and computing simply by the enjoyment of the users using the website in-hand. Our approach to an online competitive chess website is completely legal and ethical, and provides a lot of value for the user playing the game. 
* Practiced not voicing over for [commerical](https://www.youtube.com/watch?v=6gtWMTjAztI) which are the requirements for the final project

### Incorporating Tech Talks
* Databases
    * CRUD
        * Create, read, update, delete
        * Use different data types(INT, String, ETC) and parameters(primary_key, notnull, null, etc) to create table
    * One db, chess.db in project
        * 3 tables: user created in ([user.py](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/user.py#L12-L22)), game_move and game created in [replaygame.html](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/replaygamehtml.py#L8-L23)
        * Used for user creation and storing information from chess games(move number, color move, etc)     
        * Data in db is pulled and shown on website using jinja for loops and variables on replaygamedata and joingamedata
* HTML 5/JS
    * Used attributes such as min and max length, input required, and place holders [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/signup.html#L11-L27)
    * Used JS functions to validate passwords matching [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/signup.html#L33-L44)
* REST APIs
    * Used [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/templates/webapi2.html)(front end) using jinja variables and loops
    * Backend [here](https://github.com/kylem314/P5-Gim-Vamps-Project/blob/main/flaskmain.py#L180-L190)
    * Data is pulled from lichess and displays ranked players on different sites
* Lists/dictionaries



## Summary: 
Create a chess-based website using Python, Flask, SQLAlchemy, and a Raspberry Pi with an internet domain that has the following features:
* Username/Password login system w/ profiles
    * Profiles show data from database about stats
* Database of profiles with statistics based on previous games
* Play against other players, or against an AI with different difficulties
* Be able to replay past games from a database and see moves
* Rules & Settings

## Big Ticket Goals:
* A working chess game, integrated into our website
* Profile system using a database, where people can find data such as past games, winrate, etc.
* Menu to navigate to all parts of the website


## Table of Collaborators:
| Name | Github ID |
| ------------- | ----------- | 
|Kyle Myint | kylem314 |
|Lucas Bruner | notkobalt |
|Ava Brooks | avabrooks |
|David Kim | DavidKim37 |

## Project Plan 
[Full README.md with grades from this trimester](https://docs.google.com/document/d/1ksmFpIRDhS-dvuICdMOBlyGIHcLlXs96FeMo1Ji3Azw/edit#heading=h.lgigd2ujewnv)





