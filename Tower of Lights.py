"""
Tower of Lights
Problem Description
There are N number of Light towers (L1...LN) with height (Hi). Amount of area lighted by a tower of height Hi is shown
in the image.

https://www.tcscodevita.com/CodevitaV7/images/Tower%20of%20Lightsimage1.jpeg

Total Area for this case is Hi2. These towers are placed on a long road. You need to find the total amount of area has
light.

Constraints
1 <= T <= 100

1 <= N <= 1000

0<= P <= 1000

1<= H <= 1000

Input Format
The first line contains one Integer T, the number of test cases.

For each test case,

The first line contains one Integer N, the number of light towers. In next N lines, each line contains two integers P
and H, where P represents the position and H represents the height.

Output
T double values in T lines represent the area for each test case.

Test Case

Explanation
Example 1

Input 1

1

10 2

Output

4.0

Example 2

Input 2

3 4 8 6 2 12 3

2

5 4

7 4

Output

70.75

23.0

Explanation picture for Example #2 and Example #1

 https://www.tcscodevita.com/CodevitaV7/images/Tower%20of%20Lightsimage2.png
"""


class Traingle:
    def __init__(self, p, h, l, r):
        self.p = p
        self.h = h
        self.l = l
        self.r = r


t = int(input())
for __ in range(t):
    overlap = 0
    n = int(input())
    traingles = []
    for _ in range(n):
        p, h = [int(x) for x in input().rstrip().split()]
        traingles.append(Traingle(p, h, p - h, p + h))

    traingles = sorted(traingles, key=lambda x: (x.l, x.h))

    i, j = 0, 0
    try:
        while i < n:
            deleted = 0
            j = i + 1
            while j < n:
                if traingles[j].l >= traingles[i].r:
                    break
                if traingles[i].r >= traingles[j].r:
                    del traingles[j]

                    n -= 1
                    continue
                if traingles[j].l < traingles[i].r:
                    overlap += ((traingles[i].r - traingles[j].l) / 2) ** 2
                j += 1
            i += 1
    except Exception as e:
        pass
    area = 0
    for traingle in traingles:
        area += traingle.h ** 2
    print(round(float(area - overlap), 2))
