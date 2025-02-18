from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
import re

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
    # 1. 使用 PyPDFLoader 讀取 PDF 檔案
    pdf_loader = PyPDFLoader(q2_pdf)
    documents = pdf_loader.load()

    contents = ""
    for document in documents:
        contents += document.page_content + "\n"

    # 2. 使用 RecursiveCharacterTextSplitter 來分割文本
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10,  # 每個 chunk 的最大字數，可根據需要調整
        chunk_overlap=0,  # 設定不重疊
        separators=["[ \n]第.*[章條][ \n]"],
        length_function=len,  # 使用字串長度來決定分割位置
        is_separator_regex=True
    )

    # 分割文件為多個 chunks
    chunks = text_splitter.split_text(contents)
    # 4. 嘗試將每一章，每一條切分成單獨的 chunk
    # final_chunks = []
    print(len(chunks))


    # # 定義分割邏輯，根據章節和條文來分割
    # count = 0
    # for chunk in chunks:
    #     content = chunk.page_content
    #     # 根據章節模式找到所有章節
    #     chapters = re.split(chapter_pattern, content)
    #     for chapter in chapters:
    #         # 根據條文模式再分割每一章
    #         articles = re.split(article_pattern, chapter)
    #         for article in articles:
    #             # 將每一條分割為單獨的 chunk
    #             if article is not None:
    #                 final_chunks.append(article.strip())
    #                 print("\n------"+str(count)+"----")
    #                 print(article.strip())
    #                 count = count+1
    # print(len(final_chunks))
    # # 返回分割後的 chunk 數量
    return len(chunks)

print("star hw2")
hw02_2(q2_pdf)