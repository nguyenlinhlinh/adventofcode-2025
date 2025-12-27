# adventofcode-2025


activate environment 
```bash
source ./bin/activate
```
## Day 1
## Day 2
**Problem:** given ranges of numbers find all the invalid numbers which are numbers made of sequence of digits repeated twice.

**Solution part 1:**: iterate from range start to range end and check if the number of digits are even. If number of digits is even compare the first half with the second half to see if they are the same.

**Solution part 2:** Comming soon...
## Day 3
**Problem:** given a list of string of digits choose a specific number of digits from the string to get the largest possible number.

**Solution part 1:** Since it only requires 2 digits and the inputs is not so large it is enough with 2 for loops to get the combination of two digits which gives largest number from the string.

**Solution part 2:** Solved by using the two pointers and greedy algorithm to choose the largest number in the range. 
To get the largest number with 12 digits iterate 12 times. For the first digit the search range should be from 0 to n - 11. For the second digit the search range should be from postion of first digit + 1 to n - number of digit left to choose (which is 11) + 1. This continues until we get 12 digits number.

## Day 4
**Problem**: Given a grid with position of rollpapers marked with `@` and empty position marked with `.`. A roll of paper can be removed if it has fewer than 4 rolls of paper in the eight adjacent positions.
- Part 1: Find how many rollpapers can be removed.
- Part 2: Find how many rollpapers can be removed if once a rollpaper is removed the fork can access more rolls of paper which might also be able to remove.

**Solution part 1:** Solved by iterating through all position in the grid and check the eight adjacent positions to see if there are fewer than 4 rolls of paper.

**Solution part 2:** Solved by introducing a set of possitions with rollpapers from grid. This allows removing roll of paper during the iterations. 

## Day 5
**Problem:** Give a list of ranges and a list of numbers. Ranges can be overlapp.
- Part 1: count the number of numbers that are in at least one range.
- Part 2: count the numbers in ranges instead. For example 4-10 means there is 7 numbers in this range.

**Solution part 1:**: For each number iterate through the ranges and check if the number i in that range. If yet break the iteration.

**Solution part 2:**: Merge ranges to eliminate the overlapp between ranges. Merging by sorting the ranges after start number of the ranges. Create a auxilary array and for each range check if it is overlapp with the last range in auxilary array. If yes add the new range from the last number of last range in auxilary array + 1 to the last number of the current range which is being proccessed to the auxilary array. Lastly, count the numbers in ranges using this formula: start - end + 1.

## Day 6
**Problem:** Given a list of problems. Each problem has a group of numbers that need to be either added or multiplied together. 
- Part 1: find the sum of all problems.
- Part 2: each problem is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. Find the sum of all problems.

**Solution part 1:** have an array called `result` with length which is the number of problems. The initial values in `result` are values of the first row of each problem.
Iterate through each row and for each column add or multiply the value in the column with the value in `result`for that specific column.

**Solution part 2:** solved by rotating the matrix storing the problems and then calculation the sum as part 1. 

## Day 7
**Problem:** Given a grid with start position of the beam on top the grid. The beam moves downward on the grid. If the beam encounters a splitter it will be stopped and splitted into 2 new beams one on the left and one on the right of the splitter.
- Part 1: how many times will the beam be splitted?
- Part 2: the split changes so that the beam will either take the right path or left path. Count how many different paths would the beam traveled.

**Solution part 1:** iterate through the row of the grid and every time a beam encounter a splitter count it and add the two new beams for the next iteration.

**Solution part 2:** solved by using BFS and an auxilary dictionary called `endpos` to store the current number of paths that pass through a position. Since endpos collects the number of paths that the beams pass through a position it is important to update it with value from previous position to the next position. Total path is counted when a beam reaches the end position of the grid.