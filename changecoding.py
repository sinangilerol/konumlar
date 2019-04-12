from os import listdir
from os.path import isfile, join

def change_encoding(file_path,folder_path):
    content=""
    with open(join(folder_path,file_path), 'r') as content_file:
        content = content_file.read()
    #print(content)
    with open(join(folder_path,file_path), mode="w", encoding="utf8") as f:
        print(content, file=f)

def read_files(folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

def start(folder_path):
    files=read_files(folder_path)
    for i in files:
        change_encoding(i,folder_path)
        print(i,"finished")

if __name__ == "__main__":
    folder_path=r"folder path..."
    start(folder_path)
