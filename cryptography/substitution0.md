# Substitution 0

Tags: `Category: Cryptography`, `Substitution`\
Author: Will Hong

## Description

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
Download the message [here](https://artifacts.picoctf.net/c/380/message.txt).

## Hints

<details>
<summary>Hint 1</summary>

Try a frequency attack. An online tool might help.

</details>

## Solution

You *should* do it manually and figure out the flag with that, and that's far more fun. But I've used an [online decoder](https://www.dcode.fr/monoalphabetic-substitution) for convenience, The output was

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Hereupon Legrand arose, with a grave and stately air, and brought me the beetle from a glass case in which it was enclosed. It was a beautiful scarabaeus, and at that time unknown to naturalists—of course a great prize in a scientific point of view. There were two round, black spots near one extremity of the back, and a long one near the other. The scales were exceed. ingly hard and glossy, with all the appearance of burnished gold. The weight of the insect was very remarkable, and, taking all things into consideration, I could hardly blame Jupiter for his opinion respecting it

THE FLAG IS: PICOCTF{5UB5717U710N_3V0LU710N_03055505}
```

