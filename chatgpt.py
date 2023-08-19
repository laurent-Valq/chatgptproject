import os
import sys

##import openai
#from langchain.chains import ConversationalRetrievalChain, RetrievalQA


#from langchain.embeddings import OpenAIEmbeddings
#
#from langchain.indexes.vectorstore import VectorStoreIndexWrapper
#
##from langchain.vectorstores import Chroma

import constants
from langchain.document_loaders import TextLoader  # is going to read the data
from langchain.indexes import VectorstoreIndexCreator
##from langchain.llms import OpenAI
##from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]
print(query)

loader = TextLoader('data.txt')                    # is the local file that textloader is going to read
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))


# Enable to save to disk & reuse the model (for repeated queries on the same data)
#PERSIST = False
#
#query = None
#if len(sys.argv) > 1:  
#  query = sys.argv[1]
#
#if PERSIST and os.path.exists("persist"):
#  print("Reusing index...\n")
#  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
#  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
#else:
#  #loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
#  loader = DirectoryLoader("data/")
#  if PERSIST:
#    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
#  else:
#    index = VectorstoreIndexCreator().from_loaders([loader])
#
#chain = ConversationalRetrievalChain.from_llm(
#  llm=ChatOpenAI(model="gpt-3.5-turbo"),
#  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
#)
#
#chat_history = []
#while True:
#  if not query:
#    query = input("Prompt: ")
#  if query in ['quit', 'q', 'exit']:
#    sys.exit()
#  result = chain({"question": query, "chat_history": chat_history})
#  print(result['answer'])
#
#  chat_history.append((query, result['answer']))
#  query = None
