A sudoku solver I made for fun during a CS101 lab. It takes a sudoku as a 2D array, with each empty square represented as an asterisk. 
It then goes through each empty square and creates a list of possibilities for each while turning squares with a single possibility into actual numbers and repeats this process.
Then the program checks each empty square and goes through each possibility of the squares horizontal, vertical and in the same square to see if it has any unique possibilities,
in which case the square would be assigned that unique value.
