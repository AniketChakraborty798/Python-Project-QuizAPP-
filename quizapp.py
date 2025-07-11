# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 18:22:05 2025

@author: Aniket Chakraborty
"""
def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        try:
            answer = int(input("Enter your choice (1-4): "))
            if q["options"][answer - 1].lower() == q["answer"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print("❌ Wrong! The correct answer was:", q["answer"])
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Skipping question.")

    print(f"\nYour final score is {score}/{len(questions)}")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "HTML", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "Agatha Christie", "Dan Brown"],
        "answer": "J.K. Rowling"
    }
]

run_quiz(questions)
