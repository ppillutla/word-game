# word-game

**RULES:**
There is a 7 letter target word. Your objective is twofold: get as many points as you can, and guess the 7 letter word before time runs out.

**How to get points:**
Guess 4-6 letter words that can be formed with letters from the target 7 letter word.
4 letter word = 4 points
5 letter word = 5 points
6 letter word = 6 points

Example: 
Target Word = 'ROUTERS'

Player doesn't know anything about the target word yet except that it is 7 letters. 

Guess 1: 'ROPE'

Result: 0 points, 'R', 'O', and 'E' are marked as "found" letters

--> this is worth 0 points because ultimately the word 'ROPE' can't be formed using only letters from the (unknown) target word 'ROUTERS'

Guess 2: 'ROTE'

Result: 4 points, 'R', 'O', 'T', 'E' are all marked as found letters

--> this is worth 4 points because the word 'ROTE' can be formed using only a subset of letters from the (unknown) target word 'ROUTERS'

Guess 3: 'ROUTE'

Result: 5 points, 'R', 'O', 'U', 'T', 'E' are all marked as found letters

--> this is worth 5 points because the word 'ROUTE' can be formed using only a subset of letters from the (unknown) target word 'ROUTERS'

At this point, the player knows 5 out of the 7 letters of the target word, and might guess a few more words of length 4-6 characters to rack up some points before guessing the target 7 letter word:

Guess 4: 'TOUR'

Result: 4 points

Guess 5: 'TRUE'

Result: 4 points

Guess 6: 'ROUTED'

Result: 0 points

Guess 7: 'ROUTER'

Result: 6 points

Guess 8: 'ROUTERS'

Result: Found target word! Plus 10 points!

Total Points: 23 + 10 = 33 points.
