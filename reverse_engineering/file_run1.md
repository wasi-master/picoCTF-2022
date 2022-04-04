# File Run 1
Tags: `Category: Reverse Engineering`\
Author: Will Hong

## Description

A program has been provided to you, what happens if you try to run it on the command line?
Download the program [here](https://artifacts.picoctf.net/c/309/run).

## Hints

<details>
<summary>Hint 1</summary>

To run the program at all, you must make it executable (i.e. `$ chmod +x run`)

</details>
<details>

<summary>Hint 2</summary>

Try running it by adding a '.' in front of the path to the file (i.e. `$ ./run`)

</details>

## Solution

By using the `file` command on that file, we can determine that the file is an elf binary. And can only be ran from an linux environment. So I used WSL for this and used `chmod +x run` to add the eXecutable flag to the file so that it can be executed. Then I just used `./run` to run the file and it worked and showed me the flag.

Or, alternatively, you can use the `strings` command to get the flag
