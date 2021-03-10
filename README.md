# Project Plan
Group Members: Kyle Myint, Lucas Bruner, Ava Brooks, David Kim
    
## Website URL: 
http://chessthegame.cf

## Website Direct IP
http://76.176.72.123:3000/

## [Commerical]()

## README Guidance 
### Major Technicals:
* Web API
* ELO System
* Databases
* Signup/Login
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
* Raspberry Pi
* WOW

### Incorporating College Board Requirements: 
* Creative development
   * Use collaboration and program design and development to learn how these 2 topics are very important to creating programs
* Data
   * Use data compression and extracting information from data to explore how computers use and handle data to produce information and solve problems
* Algorithms and programming
   * Use algorithms and simulations to create programs that solve problems or show creativity
   * Algorithmic efficiency 
* Computer systems and networks
   * How computers and network systems work using the internet and parallel distributed computing
   * How to use multiple computers to split up work and make process faster
* Impact of computing/ethics
   * Effect of computing on society, economy, culture, and everyday life
   * Legal and ethical responsibilities as a programmer
   * Digital divide, computing bias, and safe computing

### Incorporating Tech Talks




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


## Table of Collaborators:
| Name | Github ID |
| ------------- | ----------- | 
|Kyle Myint | kylem314 |
|Lucas Bruner | notkobalt |
|Ava Brooks | avabrooks |
|David Kim | DavidKim37 |

## Project Plan 
[Full README.md with grades from this trimester](https://docs.google.com/document/d/1ksmFpIRDhS-dvuICdMOBlyGIHcLlXs96FeMo1Ji3Azw/edit#heading=h.lgigd2ujewnv)





