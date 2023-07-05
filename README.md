# Quiz-App

Python GUI Quiz App using questions from the open source [Open Trivia Database](https://opentdb.com/)

## Requirements

python3 and tkinter, requests, json, random, html, pyttsx3 modules and a working internet connection to fetch the questions from the database

## Installation (Skip if modules are already installed)

Ensure that you have python3 and pip installed on your system

Run the following command in the terminal

```pip install requests pyttsx3```

## Usage

> Run the following command in the terminal ```python3 quiz.py```

> Enter the number of questions you want to answer, the difficulty level and the category of questions and click on start button

> Use the radio buttons to select the answers of the question and click on next button to go to the next question

> You may quit the quiz at any time by clicking on the quit button

> At the end of the quiz the score would be displayed

## Note

running quiz.py creates a data.json file which contains all fetched questions and answers, they can be used for review after the quiz

main.py is a CLI version and gui.py is a basic GUI version of quiz.py

they are not required to run the quiz app
