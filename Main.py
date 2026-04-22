import random

# Questions database
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI and ML?",
        "options": ["A. Python", "B. Java", "C. C++", "D. HTML"],
        "answer": "A"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Elon Musk", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bill Gates"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    }
]

def run_quiz():
    score = 0
    questions = random.sample(quiz_data, len(quiz_data))  # shuffle questions

    print("\n🎯 Welcome to the Quiz Game!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        # Validation
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid input! Please enter A, B, C, or D: ").strip().upper()

        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print(f"🏁 Quiz Over! Your Score: {score}/{len(quiz_data)}")

def main():
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
