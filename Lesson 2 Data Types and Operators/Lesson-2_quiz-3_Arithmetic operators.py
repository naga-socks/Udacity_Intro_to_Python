'''
Jhonatan Nagasako
Udemy-Intro to Python
Lesson 2: Data Operators
3. Quiz

Problem 1: Write an expression that calculates the average of 23, 32 and 64
- Place the expression in this print statement
'''
problem_1 = (23+32+64)/3

print("Problem 1", problem_1)

'///////////////////////////////NEXT SECTION////////////////////////'
'''
In this quiz you're going to do some calculations for a tiler. Two parts of a
floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5
tiles wide by 7 tiles long. Tiles come in packages of 6.

2. How many tiles are needed?
3. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be
left over?
'''
# Fill this in with an expression that calculates how many tiles are needed.
sec1 = 9*7
sec2 = 5*7
secTotal = sec1+sec2
#print("Problem 2", secTotal)
print(secTotal)

# Fill this in with an expression that calculates how many tiles will be left over.

numTitles = (17*6)%secTotal
#print("Problem 3",numTitles)
print(numTitles)
