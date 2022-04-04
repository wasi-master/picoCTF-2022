# Substitution 1

Tags: `Category: Cryptography`, `Substitution_cipher`\
Author: Will Hong

## Description

A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.
Download the message [here](https://artifacts.picoctf.net/c/415/message.txt).

## Hints

<details>
<summary>Hint 1</summary>

Try a frequency attack.

</details>

<details>
<summary>Hint 2</summary>

Do the punctuation and the individual words help you make any substitutions?

</details>

## Solution

You *should* do it manually and figure out the flag with that, and that's far more fun. But I've used an [online decoder](https://www.dcode.fr/monoalphabetic-substitution) for convenience, The output was

```text
CTFs (short for capture the flag) are a type of computer security competition. Contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. Challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. CTFs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. For this problem, the flag is: picoCTF{FR3JU3NCY_4774CK5_4R3_C001_7AA384BC}
```

