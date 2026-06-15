from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)

# llm = HuggingFaceEndpoint(
#     model='Qwen/Qwen2.5-7B-Instruct',
#     task='text-generation',
#     huggingfacehub_api_token=os.getenv("HF_Token")
# )

# model = ChatHuggingFace(llm=llm)