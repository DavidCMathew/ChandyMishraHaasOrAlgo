Assignment Submission
David Cheria Mathew: 2020mt12077

Chandy–Misra–Haas Algorithm for the OR model

Requirements
Program was developed and tested on python 3.9 and Windows 10


Input format
1) The input.txt file
Input must be provided in the form of a Wait For Graph represented in the form of an nxn matrix
such that matrix[i][j] = 1 if process i is dependent on (waiting for) process j.


eg1 : to represent a graph like below

0 ---> 1 --> 4
^      |     |
|      v     v
3<---- 2     5

The input.txt would be
0,1,0,0,0,0
0,0,1,0,1,0
0,0,0,1,0,0
1,0,0,0,0,0
0,0,0,0,0,1
0,0,0,0,0,0

eg2 : to represent at graph like below
0 ---> 1 --> 4
^      |     |
|      v     v
3 <--- 2 <-- 5

The input.txt would be
0,1,0,0,0,0
0,0,1,0,1,0
0,0,0,1,0,0
1,0,0,0,0,0
0,0,0,0,0,1
0,0,1,0,0,0


Note:
    a) All indices start at 0
    b) No process can be dependent on itself (this is filtered in input parsing)
    c) The matrix shape has to be nxn
    d) These provided 2 inputs can be directly pasted into file

2) Initiating process for the algorithm.
Program will give a prompt as shown below:

Please enter the initiator for CMH algorithm[0-n]:

User must enter a value between 0 and n-1 (0 included) to select which process will initiate the algorithm
Note:
    a) Index starts at 0


Running the program
To run the program, just run the python file using
python main.py
In command prompt.