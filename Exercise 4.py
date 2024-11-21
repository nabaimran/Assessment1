# 4. Primitive Quiz 

answer = input("What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct!")
else:
    print("Wrong answer.")

# multiple questions
questions = {
    "What is the capital of Germany?": "berlin",
    "What is the capital of France?": "paris",
    "What is the capital of Iraly?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the capital of Belgium?": "brussels",
    "What is the capital of Portugal?": "lisbon",
    "What is the capital of Greece?": "athens",
    "What is the capital of Netherlands?": "amsterdam",
    "What is the capital of Poland?": "warsaw",
    "What is the capital of Austria?": "vienna"
}

for question, correct_answer in questions.items():
    answer = input(question + " ")
    if answer.lower() == correct_answer:
        print("Correct!")
    else:
        print("Wrong answer.")

