from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    # pages = []
    # pages = loader.load_and_split()
    # print(pages)
    # docs = ""
    # for item in pages:
    #     print(item.metadata)
    #     # docs += item.page_content
    #     # print(docs)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator="\n")
    chunks = text_splitter.split_documents(documents=documents)
    last_chunk = chunks[-1]
    print(last_chunk)
    return last_chunk

def hw02_2(q2_pdf):
    pass

print("star hw2")
hw02_1(q1_pdf)