import os
from dotenv import load_dotenv
from typing import Any
import openai
load_dotenv()

API_KEY = os.environ.get('API_KEY')


class GPT:
    def __init__(self):
        openai.api_key = API_KEY
        self.completion = openai.Completion()
        self.context = '''Human: Hello, who are you?
        AI: I am doing great. How can I help you today?
        '''

    def ask(self, question: str):
        prompt = f'{self.context}Human: {question}\nAI:'
        print('before')
        response: Any = self.completion.create(
            prompt=prompt, engine="davinci", stop=['Human:'], temperature=0.9,
            top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
            max_tokens=30)
        answer: str = response.choices[0].text.strip()

        self.context = f'{self.context}Human: {question}\nAI: {answer}\n'
        print('updated context', self.context)
        return answer
