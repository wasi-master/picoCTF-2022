# Transportation Trial

Tags: `Category: Cryptography`, `cryptography`\
Author: Will Hong

## Description

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message [here](https://artifacts.picoctf.net/c/457/message.txt     ).

## Hints

<details>
<summary>Hint 1</summary>

Split the message up into blocks of 3 and see how the first block is scrambled

</details>

## Solution

A simple python script

```python
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with open('message.txt') as f:
    data = f.read()
    print("".join(i[2]+i[0]+i[1] for i in chunks(data, 3)))
```

1. We define a chunks function that will split the message up info blocks of 3
2. We open the file and save the contents to a variable named data
3. We add the last, first, and middle characters together for each chunk and print the result

And you'll get your flag
