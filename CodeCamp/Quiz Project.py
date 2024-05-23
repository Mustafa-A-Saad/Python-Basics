# Related to Quiz
import Quiz
question_prompts = [
    "What is my Name\n(A) Boogey\n(B) Tefa\n(C) Commandos\n\n",
    "What is my Age\n(A) 27\n(B) 18\n(C) 28\n\n",
    "What is my Game\n(A) LoL\n(B) Valo\n(C) Hollw Knight"
    ]

questions = [
    Quiz.Question(question_prompts[0],"a"),
    Quiz.Question(question_prompts[1],"c"),
    Quiz.Question(question_prompts[2],"b"),
]

def run_test(test):
    score = 0
    for question in test:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got "+str(score)+"/" +str(len(questions))+" Correct")

run_test(questions)