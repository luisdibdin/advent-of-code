# Advent of Code

Attempting each day of the Advent of Code with a TDD approach. Experimenting with perhaps some long winded solutions as well to have a play with different clean coding ideas.

### Day One Challenges

The main challenge with day one is that a string "nineeight" should count as "98" and so does "nineight". When doing a regex sub using a dictionary to map pattern and replacement you would get "9ight" which is not right. To get around this I had to give up on trying to replace the strings and use a lookahead to create a string that would look like "9nin8ight" as the cursor is on the preceeding character so replaces that instead. Not the cleanest but it did solve the issue. Would love to revisit and get it replacing the strings correctly.