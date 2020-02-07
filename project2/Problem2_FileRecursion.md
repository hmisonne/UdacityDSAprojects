# Finding Files

For this project, I had to implement a recursive algorithm to find all the paths of files under a directory that end with a specifix suffix.

## Data Structure
To solve this problem, I used a list in which I stored all the paths.

m = number of files per folder
mf = number of subfolders in folder

## Time complexity
First, I needed to iterate through the folder content which takes O(m)
Then, I go to each subfolder recursively which takes O(m * mf)
