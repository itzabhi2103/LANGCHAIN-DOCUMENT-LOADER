from langchain_community.document_loaders import TextLoader
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
    template='Write a summary for the following poen \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt")

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))