
Using Vim to remove lines (range of line) from large text file using bash.
```shell
ex -sc '1d2000|x' file
```


``` 
meaning:
    1 move to first line
    2000 select 2000 lines
    d delete
    x save and close
```
