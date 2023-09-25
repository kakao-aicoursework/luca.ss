import os
import openai


from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import (
    HumanMessage,
)

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import tiktoken

class OpenaiBot:

    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    PROMPT_DIR = f"{BASE_DIR}/prompt"
    DATA_DIR = f"{BASE_DIR}/assets"

    prompts = {}
    INTENT_PROMPT = f"{PROMPT_DIR}/intent.txt"
    DEFAULT_PROMPT = f"{PROMPT_DIR}/default.txt"
    ASK_KAKAO_PROMPT = f"{PROMPT_DIR}/ask_kakao.txt"


    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")
        self.chains = {
            'intent_chain': create_chain(llm=self.llm, template_path=self.INTENT_PROMPT, output_key='intent'),
            'default_chain': create_chain(llm=self.llm, template_path=self.INTENT_PROMPT, output_key='output'),
            'askkakao_chain': create_chain(llm=self.llm, template_path=self.INTENT_PROMPT, output_key='intent')
        }
        

    def ask(self, question: str):
        # return self.chat([HumanMessage(content=question)])
        return self.llm(question)
    
    def ask_with_langchain(self, question: str):
        pass

    def read_prompt(file_path: str):
        with open(file_path, "r") as f:
            prompt_template = f.read()
        return prompt_template
    
    def create_chain(llm, template_path, output_key):
        return LLMChain(
            llm=llm,
            prompt=ChatPromptTemplate.from_template(
                template=read_prompt(template_path)
            ),
            output_key=output_key,
            verbose=True,
        )
