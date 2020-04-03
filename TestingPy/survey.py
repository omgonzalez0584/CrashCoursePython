
class AnonymousSurvey():
    """Collect anonymous answer to a survey question."""

    def __init__(self,question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_responses(self,new_responses):
        """Store a single response to the survey."""
        self.responses.append(new_responses)

    def show_result(self):
        """Show all the responses that have been given."""
        for response in self.responses:
            print('-' + response)
