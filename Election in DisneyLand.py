"""
Election in DisneyLand
Problem Description
Disney Land had an election on 1st April, 2018. Disney Land is divided into different constituencies.

Different parties who fought in the Election are as follows:-

Party 1 : AAA

Party 2 : BBB

Party 3 : Others

Disney Land is rolling out a new political process. Under this process, Disney Land will be divided into N * M equal
parts called constituencies. These constituencies will then have to be aggregated into Political seats. The winner of
the maximum number of seats will be the winner of the elections and will come to power in Disney Land.

The Aggregation process will involve distributing N*M constituencies into K Seats such that

Number of constituencies that are a part of a Electoral Seat is maximum i.e. of size B*B

No constituency is left out

There is no overlap of constituencies across Seats

Distribution of constituencies in Seats is equal

The party which wins maximum constituencies in a given Seat wins that Seat. Winner of maximum Seats wins the election.

For representational purpose, N*M constituencies of Disney Land are represented as a matrix. The winning political party
in that constituency is represented with number as follows

Party AAA -> 1

Party BBB -> 2

Others -> 3

Given the matrix, find B*B different constituencies in the Disney Land (B < N, M). Find B in such a way that, B is
maximum.

Unfortunate reality of Elections in this day and age is, Horse Trading. Disney Land is no different. After the election,
some party may bribe some other party to surrender a particular constituency to win that seat.

Your task is to find which party won the Election after due process, including Horse-trading. If no party has a
majority, then print "No Majority".

Constraints
Input Format
First Line indicates the Row (N) and Column (M) of the total number of constituencies in Disney Land.

Next N lines contain the data about which party has won which constituency

Next Line (After the N Lines of Seats) contains number of Horse-trades (H) that took place during the elections.

Next H Lines contains a data tuple <X, Y, Z> where

X & Y are the row & column of the seat where bribe took place, and

Z is the Party who initiated the horse trading.

Output
First Line should contain the party who has the majority before horse-trading and the number of seats of that party,
separated by a colon (:) or No Majority

Second Line should contain the party who has majority after horse-trading and the number of Seats of that party,
separated by a colon (:) or No Majority

Test Case

Explanation
Example 1

Input

4 4

1 1 2 2

2 3 2 3

1 1 3 3

2 1 3 3

1

1 1 2

Output

Initial Majority Party:Seats = AAA:2

Party Won Party:Seats = BBB:2

Explanation

From the input having 4*4 matrix; wherein N = 4 and M = 4, it is divided into 4 equal constituency of 2*2 matrix each.

First Seat:-

1 1

2 3

Second Seat:-

2 2

2 3

Third Seat:-

1 1

2 1

Fourth Seat:-

3 3

3 3

The Party who won the First Seat = AAA

The Party who won the Second Seat = BBB

The Party who won the Third Seat = AAA

The Party who won the Fourth Seat = Others

From the Seat wins, it is clear that the Party who has the initial majority = AAA

Now, the constituency present in Row = 1 and Column = 1 is bribed by Party BBB.

Hence, that Seat (First Seat) after the Bribing process will be:-

2 1

2 3

Hence, the Party who won the First Seat = BBB

Thus, after horse-trading activities complete, the Party who finally won the Election = BBB
"""

n, m = map(int, input().rstrip().split())
b = 0

for i in range(2, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        b = i
        break
if b == 0:
    exit(0)
data = []
for i in range(n):
    data.append([int(x) for x in input().rstrip().split()])
seats = [-1, 0, 0, 0]
for i in range(0, n - b + 1, b):
    for j in range(0, m - b + 1, b):
        temp = [-1, 0, 0, 0]
        for k in range(i, i + b):
            for l in range(j, j + b):
                temp[data[k][l]] += 1
        seats[temp.index(max(temp))] += 1

d = {1: 'AAA', 2: 'BBB', 3: 'Others'}
if seats[0] == seats[1] == seats[2]:
    print('No Majority')
else:
    print('Initial Majority Party:Seats = {}:{}'.format(d[seats.index(max(seats[1:]))], max(seats[1:])))

h = int(input())
for _ in range(h):
    x, y, z = map(int, input().rstrip().split())
    data[x - 1][y - 1] = z

seats = [-1, 0, 0, 0]
for i in range(0, n - b + 1, b):
    for j in range(0, m - b + 1, b):
        temp = [-1, 0, 0, 0]
        for k in range(i, i + b):
            for l in range(j, j + b):
                temp[data[k][l]] += 1
        seats[temp.index(max(temp))] += 1

if seats[0] == seats[1] == seats[2]:
    print('No Majority')
else:
    print('Party Won Party:Seats = {}:{}'.format(d[seats.index(max(seats[1:]))], max(seats[1:])))
