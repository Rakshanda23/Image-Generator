import sys
import os 
import sqlite3 as sql3
from PIL import Image
from gemini import getting_data

def main(img_path, prompt):
    
    dict = {'':''}
    prompt  =prompt.lower()
    # print(os.path.exists(img_path)) 



    for dir, dirpath, files in os.walk(img_path):
        for file in files:
            filename = file.split(".")[0]
            filename = filename.split(" (")[0]
            # print(filename)
            if filename in dict:
                dict.get(filename).append(file)
            else:
                dict[filename] = list([file, ])

    s = set()

    tokens = prompt.split(" ")

    for token in tokens:
        for key in dict:
            k = key.split(" ")
            if token in k:
                if key in prompt:
                    for file in dict[key]:
                        s.add(file)

    for a in s :
        img = Image.open('dataset/' + a)
        img.show()
        
    print(s)

if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
        print(data)
        res = getting_data(data)
        print(res)
        main("dataset", res)

