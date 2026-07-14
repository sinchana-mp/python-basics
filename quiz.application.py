questions = [
    {
        "question": "What is the capital of India?",
        "options": ["1. Delhi", "2. Mumbai", "3. Chennai", "4. Kolkata"],
        "answer": "1"
    },
    {
        "question": "Which language are you learning?",
        "options": ["1. Java", "2. Python", "3. C++", "4. HTML"],
        "answer": "2"
    },
    {
        "question": "Which data structure stores multiple values?",
        "options": ["1. List", "2. Integer", "3. Float", "4. Boolean"],
        "answer": "1"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "1. Central Processing Unit",
            "2. Computer Personal Unit",
            "3. Central Program Utility",
            "4. Control Processing User"
        ],
        "answer": "1"
    }
]

score = 0

print("--- Quiz Application ---")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer: ")

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n--- Result ---")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 75:
    print("Excellent Performance!")
elif percentage >= 50:
    print("Good Performance!")
else:
    print("Need More Practice!")