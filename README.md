# Introductiong to Computer Science - Fall 2017

## Lab 7 - A Taxing Lab

**Purpose:** In this lab you will get more experience writing functions in JavaScript. You will also practice using the HTML `<script>` element. You will design and write a simple webpage that computes net pay after subtracting taxes.

**Practice:** This is largely just additional practice for the concepts and techniques that we've already explained.

**Instructions:** In this repository, there is a a web page file called `payroll.html`. Once you have cloned this repository, study the code in the file.

Notice that there are two functions in the script element at the top of the page. The first function, `roundMoney()`, rounds numbers to two decimal places. It is complete and works properly. You do not need to make, nor should you make, any changes to it. It is a function you will **call** from the second function. The second function, `calculate()`, is there for you to implement. Make note of the comments that describe _what_ the function does.

Note that the `<body>` element is complete and should not be changed. You must provide correct JavaScript code for the `calculate()` function that is started for you in the `<head>` element. After entering the gross salary, the user should click the Calculate Taxes and Net Pay button. When the tax amounts are computed, they must be rounded to the nearest cent (hundredth of a dollar). The `roundmoney()` function is provided to round the dollar amount to two decimal places. When `roundMoney()` is called, its argument must be a number. Both tax amounts must be rounded before they are displayed in the output `<div>`.

When the button is clicked, an output `<div>` should be filled with the following information:

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
