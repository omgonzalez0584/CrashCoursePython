from survey import AnonymousSurvey

#Define a question , and make a survey.
question  = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Languaje: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

#Show the survey result
print("\nThanks you to everyone who participied in the survey!")
my_survey.show_result()
