# Computational thinking and programming skills

## Q1

Write a Python program that will tell you how old you will be on your next birthday. Your program should:

* prompt you to enter your age
* add 1 to the entered age
* output your age on your next birthday.

You should use meaningful variable name(s), correct syntax and indentation in your answer.

[5 marks]

## Q2

Write a Python program that will calculate the volume of a rectangular swimming pool with a depth of two metres. The formula for calculating the volume is:

```text
volume = length x width x depth
```

Your program should:

* prompt the user to enter the length in metres (the value should be a whole number)
* prompt the user to enter the width in metres (the value should be a whole number)
* calculate the correct volume
* output the volume.

You should use meaningful variable name(s), correct syntax and indentation in your answer.

[5 marks]

## Q3

The OR logic gate outputs a 1 if either of the two inputs are 1, otherwise it will output a 0. For example:

* if the two inputs are 0 and 1 then it will output a 1
* if the two inputs are both 0 then it will output a 0

Write a Python program that will output the result of performing an OR logic gate.

Your program should:

* keep asking the user to enter two values until they enter two values, each of which must be either a 0 or a 1
* calculate the correct output from an OR gate using the two inputs that have been entered
* output the result of the OR gate.

You should use meaningful variable name(s), correct syntax and indentation in your answer.

[7 marks]

## Q4

Write a Python program that plays the following number guessing game. Your program should:

* randomly generate a 2 digit numeric code (ie numbers between 10 and 99)
* allow the user 10 turns to guess the code as follows:
  * prompt the user to enter a 2 digit number (validation is not required)
  * calculate the number of correct digits in the correct place
  * output a suitable message followed by the number of correct digits in the correct place
* output a suitable message if the user has guessed the 2 digit code correctly within 10 turns
* output a suitable message along with the correct code if the user has had 10 turns and failed to guess the code correctly

To generate a random number between two values you can use the Python command

```python
random.randrange(x, y)
```

This will generate a random integer between x and y - 1 inclusive. For example, the command random.randrange(2,8) will generate a random number between 2 and 7.

You should use meaningful variable name(s), correct syntax and indentation in your answer.

The first line of the program has been completed for you:

```python
import random
```

[10 marks]
