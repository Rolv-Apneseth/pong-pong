# pong-pong
 A 2 player game made with pygame, heavily inspired by the classic game Pong but with a slight twist.

## What I learned
* Making a game with pygame
* Object collisions
* Use of OOP 

## Installation
1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/)
2. Clone the repository by opening your command line/terminal and run: 
```git clone https://github.com/Rolv-Apneseth/pong-pong.git```
    * Note: if you don't have git, it can be downloaded from [here](https://git-scm.com/downloads).
3. Install the requirements for the program.
    * In your terminal, navigate to the cloned directory and run: ```python3 -m pip install -r requirements.txt```
4. To start the game, run: ```python3 main.py```

## Usage
1. Once the game is run, you will be met with a starting window which explains the controls and how to play
2. Left click with the mouse when both players know their controls (AD for player1 and left and right arrow keys for player 2)
3. To generate a ball in the middle of the screen, either player can hit the spacebar. This ball will then move in a random direction. This allows players to try and play strategically and generate a new ball when there is already a ball headed for the oponent's side
    * Spawning of balls is on a 2 second cooldown so that they can't be spammed. Note that balls do not have collisions with each other.
4. A point is scored when a ball reaches the oponent's goal, and a player wins when 20 points are scored

