# Basic Mod 2

Tags: `Category: Cryptography`\
Author: Will Hong

## Description

A new modular challenge!\
Download the message [here](https://artifacts.picoctf.net/c/500/message.txt).\
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.\
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Hints

<details>
<summary>Hint 1</summary>

Do you know what mod 37 means?

</details>

<details>
<summary>Hint 2</summary>

mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

</details>

## Solution

A simple script

```python
with open("message.txt") as f:
    numbers = [int(n) for n in f.read().split()]
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    print("".join(characters[pow(i % 41, -1, 41)-1] for i in numbers))
```

1. First we open the file containing the message and save the file pointer to a variable named `f`
2. We create a list of integers from the message by reading the contents and splitting it by spaces
3. We make a list of characters we need to map to
4. We get the modular inverse of the `mod 41` of each number and get the corresponding character and print all of them
