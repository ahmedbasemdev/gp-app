import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import chromadb
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA


template = '''
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know,don't try to make up an answer.

{context}

Question: {question}
Answer:
'''

class ChatBotManager():
    def __init__(self) -> None:

        embedding_func = OpenAIEmbeddings(api_key=os.environ.get("OPENAI_API_KEY"))
        persistent_client = chromadb.PersistentClient("shifaa_VDB")

        db = Chroma(client=persistent_client,collection_name="main_collection",
                         embedding_function=embedding_func)
        
        prompt = PromptTemplate(template=template,
                input_variables=['context','question',])
        
        retriver = db.as_retriever(search_type='similarity', search_kwargs={"k":2})
        llm = OpenAI(temperature=0)

        self.qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff',retriever=retriver,
                                        chain_type_kwargs={"prompt": prompt})
    def generate_answer(self, question):

        answer = self.qa.run({"query":question})

        return answer