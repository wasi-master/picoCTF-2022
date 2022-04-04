# Basic Mod 1

Tags: `Category: Cryptography`\
Author: Will Hong / LT 'SYREAL' JONES

## Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar).
The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

## Hints

<details>
<summary>Hint 1</summary>

Maybe other passwords will have hints about the leak?

</details>

## Solution

A simple script

```python
import codecs

passwords_file = open("leak/passwords.txt")
usernames_file = open("leak/usernames.txt")

for username, password in zip(
    usernames_file.read().splitlines(),
    passwords_file.read().splitlines()
):
    if username == "cultiris":
        print(codecs.encode(password, "rot_13"))

passwords_file.close()
usernames_file.close()

```

1. First we open both the passwords and usernames files
2. We loop through all the usersnames and passwords
3. If the username is `cultiris` we  rotate it 13 characters forward to get our flag. This is essentially a caesar cipher
