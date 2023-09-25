# Jackpot-Simulator

our Objective is to simulate a slot machine! For Example should the use decide to take two 
attempts, on a slot machine with three slots (like what you see above). The Output should be: 
[[3,2,1],[7,7,7]] 
The program should be able to dynamically change how many attempts the user would like to make 
in a single sitting; the number of slots in the machine (above there are three); as well as the number 
of shape in the slot machine (the more shapes the harder a match is!). 
To get the basics of this program working you only need to use Lists & Loops. 
Bonus: If the user gets a match, the program will report they won! If they don’t get a match, the 
program will report they didn’t win (this requires knowledge on IF-Statements). 
 
Hints 
1) Create two lists, “empty_board” & “slot_machine”. The slot machine list will store the 
output from the slot machine, the empty board will store this output from each attempt 
made. In the given example [[3,2,1],[7,7,7]]: 
Slot machine first equals [3,2,1], the results are appended to the empty_board list. The Slot 
machine list is reset to empty, and a new set of values are generated from the slot machine, 
then they are appended to the empty board list. This is repeated for the number of attempts 
made. 
2) In order to get values from the slot_machine. We get them randomly using the random 
package! A package is functionality that isn’t loaded into Python by default. We can use the 
code “import random” to import the package. The function slot = random.randint(x,y) 
returns a random value and assigns it to slot. The value is between x & y (including both x & 
y). Use this function to generate the values for each of the slots. 
3) It’s important that the output is somewhat nice to look at, and that the user has some input 
into the program. Why not make the number of slots & number of attempts an input that 
the user can type in on starting the program. Using the print function you can make some 
nice outputs, after each attempt maybe print out the results?
