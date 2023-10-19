from langchain.document_loaders import UnstructuredFileLoader, OnlinePDFLoader,UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from api_keys import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_API_ENV
import csv
import pandas as pd

def process_message(message, title):
	pinecone.init(
		api_key=PINECONE_API_KEY,
		environment=PINECONE_API_ENV
	)
	index_namee = "pinex"

	embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)


	from langchain.chat_models import ChatOpenAI
	from langchain import PromptTemplate, LLMChain
	from langchain.prompts.chat import (
		ChatPromptTemplate,
		SystemMessagePromptTemplate,
		HumanMessagePromptTemplate
	)
	from langchain.schema import (
		AIMessage,
		HumanMessage,
		SystemMessage
	)

	index = pinecone.Index('pinex') 

	llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3, openai_api_key=OPENAI_API_KEY, max_tokens=1600)

	template = "You are a helpful expert. You will read and understand the following infromation extracted from the patient information leaflet of ""{drug}"" and then answer the questions asked. {documents}"
	system_message_prompt = SystemMessagePromptTemplate.from_template(template)
	human_template = "{question}"
	human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
	chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

	chain = LLMChain(llm=llm, prompt=chat_prompt)

	docsearch = Pinecone(index, embeddings.embed_query, 'text')

	df = pd.read_csv('table200row.csv', sep='|')
	

	query = message
	docs = docsearch.similarity_search(query, namespace=df.loc[df.TITLE == title].SETID.to_string(index=False), include_metadata=True)
	query_response = index.query

	new_list = []
	for x in docs:
		new_list.append(x.page_content)
	q = list(set(new_list))

	print(q)
	response = chain.run(documents=q, question=query, drug=title)


	return response
