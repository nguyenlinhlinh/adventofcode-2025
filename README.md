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