                                    Math Quiz Game

A command-line math quiz game written in Python that generates 10 random math problems based on the user’s selected difficulty level and operator. After each incorrect answer, the correct answer is displayed. The final score is shown at the end of the quiz.

I.Features

--Select difficulty level (1–5)
--Choose operator: +, -, *, /
--Random number generation based on level
--10 automatically generated questions
--Input validation for level, operator, and answers
--Displays correct answer when user is wrong
--Division answers rounded to 2 decimal places
--Final score displayed at the end

II.How the Program Works

The program is structured into four main functions:

                   1.level()
--Prompts the user to choose a level between 1 and 5.
--Continues prompting until valid input is entered.
--Returns the selected level.

Difficulty Levels
Level	Number    Range
1	   1-digit    (1–9)
2	   2-digit    (10–99)
3	   3-digit    (100–999)
4	   4-digit    (1000-9999)
5	   5-digit    (10000-99999)

                   2.operator()
Prompts the user to choose a mathematical operator:
--(+) Addition
--(-) Subtraction
--(*) Multiplication
--(/) Division
--Re-prompts until a valid operator is entered.
--Returns the chosen operator.

                   3.generator(lev)
--Generates a random number based on the selected level.
Uses:
--randint() from the random library
--For level 1 → 1-digit number.
--For levels 2–5 → generates numbers using powers of 10.

                    4.main()
--Initializes score to 0.
--Gets user level and operator choice.
--Uses Python match-case (Python 3.10+) to handle operations.
--Asks 10 questions.
--Checks user answers.
--Increments score for correct answers.
--Displays correct answer if user is wrong.
--Prints final score.

Operation Behavior
-Addition (+)
--User inputs integer.
--Compares with x + y.
--Shows correct answer if incorrect.
-Subtraction (-)
--User inputs integer.
--Compares with x - y.
--Shows correct answer if incorrect.
-Multiplication (*)
--User inputs integer.
--Compares with x * y.
--Shows correct answer if incorrect.
-Division (/)
--Displays instruction
--User must input a float.
--Shows correct answer if incorrect.

III.Scoring System
--10 total questions 
--1 point for each correct answer 
--Final score is displayed


