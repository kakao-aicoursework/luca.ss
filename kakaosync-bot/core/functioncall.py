from vectordb import VDBController

def search_db(text:str):

    db = VDBController()
    docs = db.search(text)

    str_format = ""
    for doc in docs:
        str_format += f"{doc.page_content}\n"

    return str_format


if __name__=="__main__":
    print(search_DB('카카오싱크 회원가입 어떻게 해?'))