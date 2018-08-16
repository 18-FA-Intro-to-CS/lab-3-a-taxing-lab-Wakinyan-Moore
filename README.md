# Introductiong to Computer Science - Fall 2018

## Lab 3 - A Taxing Lab

**Purpose:** In this lab you will get more experience writing functions in Python. You will also practice writing and calling functions defined in a program. You will design and write a simple program that computes net pay after subtracting taxes.

**Practice:** This is largely just additional practice for the concepts and techniques that we've already covered.

**Instructions:** In this repository, there is a a python script called `payroll.py`. Once you have cloned this repository, study the code in the file.

Notice that aside from the `main()` function, there are two functions at the top of the file. The first function, `round_money()`, rounds numbers to two decimal places. It is complete and works properly. You do not need to make, nor should you make, any changes to it. It is a function you will **call** from the second function. The second function, `calculate()`, is there for you to implement. Make note of the comments that describe _what_ the function does.

Note that the `main()` function is complete and should not be changed. You must provide correct Python code for the `calculate()` function that is started for you in the file. When the tax amounts are computed, they must be rounded to the nearest cent (hundredth of a dollar). The `round_money()` function is provided to round the dollar amount to two decimal places. When `round_money()` is called, its argument must be a number. Both tax amounts must be rounded before they are output to the console.

When the final input is entered, the following information must be printed to the console.

* The gross salary
* The amount of federal tax
* The amount of state tax
* The amount of net pay

Here is a sample output produced with the gross salary is $1267.58, the federal tax rate is 12% and the state tax rate is 5%.

```
The gross pay is: $1267.58
The federal tax is: $152.11
The state tax is: $63.38
The net pay is: $1052.09
```

Once you have completed the assignment, commit and push the repository back to your master branch.
