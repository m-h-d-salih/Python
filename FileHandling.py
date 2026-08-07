# Lesson 9 - File Handling

def save_chunks(chunks):
    with open('filetest1','w') as file:
        for i in chunks:
            file.write(i+"\n")
def load_chunks():
    with  open('filetest1','r') as file:
        data=file.readlines()
        result=[]
        for  i in data:
           result.append(i.strip())
        return result
save_chunks([
    "Python",
    "RAG",
    "FastAPI"
])
print(load_chunks())


