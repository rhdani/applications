import os
import argparse
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

# 1. Setup API Key
os.environ["OPENAI_API_KEY"] = "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"
# 1. Initialize modern components
llm = ChatOpenAI(model="gpt-4o", temperature=0)
#prompt = ChatPromptTemplate.from_template("Summarize the following text concisely:\n\n{text}")
#prompt = ChatPromptTemplate.from_template("The following is the text form of a receipt. Summarize the receipt and list out the items purchased, date of purchase, and how many items are food items and how many are medicines:\n\n{text}")
prompt = ChatPromptTemplate.from_template("The following is a combination of receipts from Costco, Palo Alto Medical Foundation and Rite-Aid. Summarize the receipts and list out the items purchased, dates of purchase, and how many items are food items and how many are medicines:\n\n{text}")

# 2. Build the chain using the Pipe operator (|)
# This is the modern replacement for load_summarize_chain
summarize_chain = prompt | llm | StrOutputParser()

# 3. Usage
parser = argparse.ArgumentParser(description="Input file name")
parser.add_argument("filename", help="Path to the input file")
args = parser.parse_args()

loader = TextLoader(args.filename)
docs = loader.load()
content = docs[0].page_content

# Invoke the chain
summary = summarize_chain.invoke({"text": content})
print(summary)
