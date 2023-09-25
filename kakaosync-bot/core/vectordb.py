import os
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma



class VDBController:

    CHROMA_DB_DIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'vectorDB') 
    CHROMA_COLLECTION_NAME = "kakao-guide"

    DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'documents') 
    
    def __init__(self):
        
    
        if not os.path.exists(self.CHROMA_DB_DIR):
            self.init_db()

        self.db = Chroma(
            embedding_function=OpenAIEmbeddings(),
            collection_name=self.CHROMA_COLLECTION_NAME,
            persist_directory=self.CHROMA_DB_DIR
        )


    def read_docs(self, filename: str):
        return TextLoader(filename).load()

    def init_db(self):

        # text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=100)
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=20)
        for root, dirs, files in os.walk(self.DATA_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                documents = self.read_docs(file_path)
                docs = text_splitter.split_documents(documents)
                self.add_docs(docs)

    def add_docs(self, docs):
        return Chroma.from_documents(docs, embedding=OpenAIEmbeddings(), collection_name=self.CHROMA_COLLECTION_NAME, persist_directory=self.CHROMA_DB_DIR)
    
    def add_texts(self, docs):
        return Chroma.from_texts(docs, embedding=OpenAIEmbeddings(), collection_name=self.CHROMA_COLLECTION_NAME, persist_directory=self.CHROMA_DB_DIR)

    def del_docs(self, ids):
        return self.db.delete(ids=ids)

    def search(self, text: str):
        return self.db.similarity_search(text)
        # return list(map(lambda x : x.page_content, ))
        

if __name__ == '__main__':
    t = VDBController()
    print(t.db.similarity_search('카카오싱크 회원가입 어떻게 해?', k=5))
    # print(t.db.similarity_search_by_vector(OpenAIEmbeddings().embed_documents('카카오싱크')))