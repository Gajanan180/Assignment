Question
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

The number of ways to attend classes over N days.
The probability that you will miss your graduation ceremony.

Prerequisite
Python 3 must be installed in your local machine.

How to run ?
To run the assignment execute following command:

python main.py 5

Approach
On any given day there could be two possibilties either you attend the classes or you miss the classes. I am generating all possible permutation of attending classes (i.e. 2 ^ No_of_days).

Next I am filtering all permutation which has 4 or more consecutive days of absence.

To compute probability I am simply dividing count of invalid permutation by total permutation.

###  Test Case 1

For 5 days

Impact Analysis Task>py main.py 5

Number of days is 5

List of probability of that student he/she will absent/present in class =  ['AAAAA', 'AAAAP', 'AAAPA', 'AAAPP', 'AAPAA', 
'AAPAP', 'AAPPA', 'AAPPP', 'APAAA', 'APAAP', 'APAPA', 'APAPP', 'APPAA', 'APPAP', 'APPPA', 'APPPP', 'PAAAA', 
'PAAAP', 'PAAPA', 'PAAPP', 'PAPAA', 'PAPAP', 'PAPPA', 'PAPPP', 'PPAAA', 'PPAAP', 'PPAPA', 'PPAPP', 'PPPAA', 
'PPPAP', 'PPPPA', 'PPPPP']

Number of ways to attend classes over 5 days is 32

The student is absent for 4 or more consecutive days =  ['AAAAA', 'AAAAP', 'PAAAA']

probability of that student to miss graduation ceremony is 3/32


## Test Case 2

Cjc_Gajanan\Impact Analysis Task>py main.py 10
Number of days is 10
Number of ways to attend classes over 10 days is 1024
probability of that student to miss graduation ceremony is 251/1024