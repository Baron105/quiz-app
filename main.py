import requests
import json
import html
import random
import time

def get_categories():
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["trivia_categories"]

def get_questions(amount, category, difficulty):
    if category == 0:
        if difficulty == "any":
            url = f"https://opentdb.com/api.php?amount={amount}"
        else:
            url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}"
    else:
        if difficulty == "any":
            url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
        else: 
            url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["results"]

def display_question(question):
    print(html.unescape(question["question"]))
    options = question["incorrect_answers"] + [question["correct_answer"]]
    random.shuffle(options)
    options = [html.unescape(option) for option in options]
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = input("Your answer (enter the corresponding number): ")
    return options[int(answer) - 1] == html.unescape(question["correct_answer"])

def play_quiz():
    cat_list = [0]
    categories = get_categories()
    print("Categories:")
    for category in categories:
        print(f"{category['id']}. {category['name']}")
        cat_list.append(category['id'])
    print("0. Any Category")
    
    category_id = int(input("Select a category: "))
    if category_id not in cat_list:
        print("Enter a valid category.")
        return
    
    difficulty = input("Select a difficulty: ")

    amount = int(input("How many questions do you want to answer? Enter a number less than 50: "))
    if amount > 50 or amount < 1:
        print("Invalid amount. Exiting...")

    questions = get_questions(amount, category_id, difficulty)
    score = 0

    ready = input("Are you ready? Press Enter to start the quiz...")
    if ready:
        return

    for question in questions:
        print("\n" + "=" * 50)

        if display_question(question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\n" + "=" * 50)
    print(f"Quiz completed! Your score: {score}/{amount}")

play_quiz()