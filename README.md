# Scientific Computic with Python
## Python projects from [FreeCodeCamp](https://www.freecodecamp.org/)

1. Arithmetic Arranger
2. Time Calculator
3. Budget App
4. Shape Calculator
5. Probability Calculator

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

***
## Budget App

Create a Category class which can take a name parameter for instantiation.
Upon instantiation initialize a ledger attribute as an empty list to record every transaction in this budget category.
Each transaction is added in the ledger with a function call, checking balance for validity.

When printed, the Category object should be like :
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Additionally, a function create_spend_chart() outside the class take a list of Category objects as parameters and return
a spend chart with graphical representation of percentages spent by category.
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
### Rules
1. A function deposit() should append an amount and a description to the category ledger.
2. A function withdraw() should append a negative amount and a description only if the balance of the category allows it.
3. A function transfer() should use withdraw() from a category (if possible) and deposit() on another category.
4. The function get_balance() return the amount total of a category.
5. The function check_funds() uses get_balance() to return True or False for a transaction.
6. The percentage spent should be rounded down at the nearest 10

***
## Polygon Area Calculator

Create a class Rectangle, and a Square class which inherits methods and attributes from Rectangle.
Rectangle is initialized with width and height attributes.

Each polygon must be formatted when printed :
```
Ex : rect = Rectangle(5, 10)
     sq = Square(4)
     print(rect)
>>>  "Rectangle(width=5, height=10)"
     print(sq)
>>>  "Square(side=4)"
```
### Rules
1. Area, Perimeter, Diagonal of the objects should be returned with 3 different methods.
2. The method get_picture() should return a string representation of the polygon using "*" character.
   ```
   Ex: 7x4 rectangle is :
   
   *******
   *******
   *******
   *******
   ```
3. The method get_amount_inside(shape) should return the number of passed in shape that can fit in the shape which call the method.
```
Ex: 
rect = Rectangle(9, 6)  
sq = Square(4)

                      2 sq fits in rect
 * * * * * * * * *    * * * *   * * * *
 * * * * * * * * *    * * * *   * * * * 
 * * * * * * * * *    * * * *   * * * * 
 * * * * * * * * *    * * * *   * * * * 
 * * * * * * * * * 
 * * * * * * * * *
 
rect.get_amount_inside(sq) shoul return 2
```

***
## Probability Calculator

Create a Hat class that takes a variable number of arguments.
Arguments specify a color and a number of balls.  
Ex:   
new_hat = Hat(yellow=3, blue=2)  
A new hat is initialized with a contents attribute which is a list of all balls in the form of their color name.  
Ex:  
new_hat.contents = [ "yellow", "yellow", "yellow", "blue", "blue"]  

A draw(number) method must (pseudo)randomly draw a ball in the hat, append it to a list and remove it from the hat a given number of time.  
The list should then be returned.

Finally, an experiment() method should exist outside the class Hat.
It takes four arguments  :  
- hat (a hat object)
- expected_balls (a dictionary with the balls color name and their expected count. Ex: {"yellow":3, "blue":1}
- num_balls_drawn (a number of balls to draw from the hat in each experiment)
- num_experiments (the number of experiments to perform)
```
ex:  
hat = Hat(black=6, red=4, green=3)
probability = experiment(
               hat=hat,
               expected_balls={"red":2,"green":1},
               num_balls_drawn=5,
               num_experiments=2000
              )
```
This method should return a percentage of successful experiments where the balls that were drawn had at least those of expected_balls.



