# Scientific Computic with Python
## Python projects from [FreeCodeCamp](https://www.freecodecamp.org/)

1. Arithmetic Arranger
2. Time Calculator

***
## Arithmetic Arranger

Given a list of problems (ex: ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) return a vertically
arranged string of every problem as in primary school:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
The returned string contains all problems formatted.

### Error Handling :
1. No more than 5 problems can be processed in a function call.
2. Only digits in both operands.
3. Only addition and subtraction as operator.
4. Both operands have a limit of 4 digits.
   
### Formatting rules :
1. There should be a single space between the operator and the longest of the two operands
2. The operator will be on the same line as the second operand
3. Both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
4. Numbers should be right-aligned.
5. There should be four spaces between each problem.
6. There should be dashes at the bottom of each problem.
7. The dashes should run along the entire length of each problem individually.

Result of the addition or subtraction should be returned as a fourth line only if a second parameter is given as True:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
***
## Time Calculator

From a string with a starting time, a duration time and (optional) a day of the week,
return the addition of starting and duration time, with the correct time period, and (optional) the day of that time.

Finally add the number of day elapsed if any.

ex: add_time("11:43 PM", "24:20", "tueSday") should return "12:03 AM, Thursday (2 days later)"

### Rules
1. Hours should be between 1 and 12.
2. Minutes should be between 00 and 59
3. The starting day parameter must be case insensitive
4. When only 1 day passed the correct input is "(next day)"

