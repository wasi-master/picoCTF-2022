# File Run 2
Tags: `Category: Reverse Engineering`\
Author: Mubarak Mikail

## Description

Can you open this safe?\
I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:\
`picoCTF{password}`

## Hints

(None)

## Solution

Opening the file and browsing around a bit shows a peculiar string: `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`. It's just a base64 encoded flag, decode it and make it into the picoCTF flag format.
