from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableBranch
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    model='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation',
    huggingfacehub_api_token=os.getenv("HF_Token")
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Answer the following quesion \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser() 

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': 'what is the product we are talking about?',
'text': docs[0].page_content})

print(result)