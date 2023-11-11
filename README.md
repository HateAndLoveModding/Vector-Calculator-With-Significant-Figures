# Vector Calculator README

## About

This is a program that adds two vectors together and includes the right number of significant figures based on the requirements in the Apologia Physics textbook. See the section below to see how the program works.

## How it works

First, it will ask you to input the magnitudes and angles of two vectors.
Then it will count how many significant figures are in each number.
Then it determines the minimum number of significant figures of the magnitude and angle of the first vector.
It does the same to the second vector.
It converts the angle in degrees to radians.
Then it determines the x1, x2, y1, and y2 values by multiplying the magnitude times either the sine or cosine of the angle and rounds to the number of significant figures determined in the last steps.
It determines the least number of significant figures from the values calculated previously.
Then it adds x1 and x2 together, y1 and y2, and converts them to the correct number of significant figures.
It counts the number of significant figures in both the x and y values and determines the least number of significant figures.
Then it takes the arctangent of y divided by x converts it back to degrees and converts it to the correct number of significant figures.
Finally, it takes the square root of x squared plus y squared and converts it to the correct number of significant figures.

## Known issues

Sometimes the x1, x2, y1, or y2 values can end in a significant zero. When the value is converted back to a number to perform more operations, Python automatically trunicates the ending zero making it have one less significant figure than it should have which then sometimes causes the final answer to be wrong.
