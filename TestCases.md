# Manual Test Cases

Project: Rock Paper Scissors – Best of 3  
Application Type: Console Game  
Technology: Python

---

## TC_01 – Valid Full Input

**Scenario:** Enter valid full word input

Steps:
1. Run program
2. Enter "rock"

Expected Result:
Program accepts input and continues game

Actual Result:
Input accepted

Status: Pass

---

## TC_02 – Valid Shortcut Input

**Scenario:** Enter shortcut input

Steps:
1. Run program
2. Enter "r"

Expected Result:
System converts "r" to "rock"

Actual Result:
Shortcut correctly converted

Status: Pass

---

## TC_03 – Invalid Input Handling

**Scenario:** Enter invalid input

Steps:
1. Run program
2. Enter "abc"

Expected Result:
Error message displayed and user prompted again

Actual Result:
Error message displayed

Status: Pass

---

## TC_04 – Winner Logic

**Scenario:** User = rock, Computer = scissors

Expected Result:
Output displays "You win!"

Actual Result:
Correct output displayed

Status: Pass

---

## TC_05 – Draw Scenario

**Scenario:** Both choose same option

Expected Result:
Output displays "Draw!"

Actual Result:
Correct output displayed

Status: Pass
