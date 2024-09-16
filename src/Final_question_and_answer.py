
import openai

class QuestionAndAnswer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_insights(self, data_summary):
        """Get insights from OpenAI based on the data summary."""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Here is a summary of the sales data:\n{data_summary}\n\nProvide insights and suggestions based on this data.",
            max_tokens=150
        )
        return response.choices[0].text.strip()
