Josephus problem Solution

Article: https://medium.com/@diwaslama/solving-josepheus-359c13ecf33f

Youtube Reference for Josephus: https://youtu.be/uCsD3ZGzMgE?si=wnLeeidSTuvV92v5

Explanation for code:
Find the Biggest "Magic" Number: First, you find the biggest number that is a power of 2 (like 2, 4, 8, 16, 32, and so on) that is still less than or equal to the number of players. Let's say you
have 10 players. The biggest "magic" number less than 10 is 8 (because 8 is 2×2×2, and it's less than 10).

Count the Extra Players: Next, you see how many players are more than this "magic" number. In our case, with 10 players, we have 2 extra players (because 10 minus 8 is 2).

The Last Standing Spot: Now, you double the extra players (so 2 becomes 4) and add 1. For our 10 players, this makes 5 (because 4 plus 1 is 5). So, if you stand in the 5th spot in the circle, you'll be the last one standing!
