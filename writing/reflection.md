# Data Types

## Benedek Kaibas

## Program Output

### What is the output from running the following commands?

Use a fenced code block to provide the output for this command.

- `python demonstrate-variable-limitations.py`

Since I wrote a function to make to more easily to run the program, mine output will be a littlebit different.
Here is the ouput of my code when I run the demonstrate-variable-limitations.py
```
1.0 is not the same as 1.1
1.0 is the same as 1.0
.33333 + .33333 + .33333 is not equal to 1
.33333333333 + .33333333333 + .3333333333 is not equal to 1
The value of 1/3 is 0.3333333333333333
0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is equal to 1
1/3 + 1/3 + 1/3 is equal 1

```

Use a fenced code block to provide the output for this command.

- `python compare-variables.py`

This is the ouput that I got when I was running the compare-variables.py file with my functions that I have added to it. 
```
    1.0 is not the same as 1.1
    1.0 is the same as 1.0
    .33333 + .33333 + .33333 is not equal to 1
    .33333333333 + .33333333333 + .3333333333 is not equal to 1
    The value of 1/3 is 0.3333333333333333
    0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is equal to 1
    1/3 + 1/3 + 1/3 is equal 1


```


## Program Questions

### Why is it not feasible to perform the computation `2**2**100`?

Provide a one-paragraph response to this question.

The number is just too big for the program to output it and most of the computers cannot handle this large amount of number. 

### What is the value of `1/3` according to the Python language? Why?

Provide a one-paragraph response to this question.

Since / in python provides a floating-point division the value of this will be 0.333333. If we want to make sure that we get for example
0.3 as the ouput than we can use Python's built in function for that which is called prec() and stands for precision which makes absolute sense
in this case. 



### Why is the value of `.33333 + .33333 + .33333 == 1` equal to `False`?

Provide a one-paragraph response to this question.

Because of the many decimal numbers in this case the python program there will be an overflow and it will be more than one. If we use 1/3 + 1/3 + 1/3 then we will get exactly one since when python breaks 1/3 to decimal numbers it will stop at 0.3 instead of 0.333333333. What is interesting is that if we just do 
print(1/3) we will get 0.3333333, but since the program sees that there is an addition following the number it will know that it has to use the prec() built in function for it. This is an easy example for that in python value overflows can happen and we have to pay attention of always checking our values and testing our code. 

(Did you remember to add your name?!)