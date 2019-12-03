# Data Processing
An implementation of a Python program which processes students’ survey data. The data is provided in a text file with some specific format. The user will have the program process all the students data, and then the user will have the possibility to check how similar specific pairs of students’ responses are.
## Prerequisites
- Have Python installed
- Install the attached txt file or you can invent one on your own. More information on this below.
## Running the tests
- A data file is provided under the name "IN_ALL_DATA.txt". The file contains the numbers of students with responses each. You can 
invent other files, with different number of students and/or answers. Make sure to rename appropriately.
- This description uses ‘line’ to refer to one student’s data. One ‘line’ is a string, where the last character is ‘\n’.
- Each line contains the student‘s name, then at least one space, and then the student’s answers coded from 1 to 5, separated by spaces.
### Assumptions
- Students’ names do not include  spaces.
- Answers are ordered by question number.
#### Example
With 3 students and 10 answers each  
name        4 1 5 1 4 2 1 5 4 3    
otherName       3 1 4 3 1 4 4 5 5 2   
anotherName    4 4 1 3 2 2 3 5 3 5  
Hence, the string generated will be:  “name        4 1 5 1 4 2 1 5 4 3\notherName       3 1 4 3 1 4 4 5 5 2\nanotherName    4 4 1 3 2 2 3 5 3 5\n”.
### Messages to be provided when comparing pairs of students’ responses: 
90% or more same responses (in the same positions) ====  really have a lot in common (>90%)!     
50% or more ====  have about half opinions in common! 
2 or more ====   have just few opinions in common (<50%) 
Less than 2 ====  have nothing in common! 
## Author:
- Huy Nguyen
## Acknowledgements:
- Sample runs provided by the course instructor and the TAs.
- Inspiration and Hardwork
