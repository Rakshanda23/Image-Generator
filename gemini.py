import os
import threading

import pathlib
import textwrap
from colorama import Fore

import google.generativeai as genai 
import sys
import requests
from time import sleep


current_string = ""
enter_pressed = False
gen_text = ""


# add your api key if below code does not work
# GOOGLE_API_KEY =


genai.configure(api_key="AIzaSyAq-BdbamaxVmvyz3R4IQ01-VEH8ahELLQ")

model = genai.GenerativeModel("gemini-pro")


def getting_data(text):
    gen_text=""
    if text != "":
        print(f"Processing string:   {text}")
        res = f' According to paragraph attached below, tell me paragraph is related with which type of programming data structure and be little biased towards array or trees and give me just data structure name nothing else, paragraph"{ text }"'
        print(res)
        response = model.generate_content(res)
        gen_text = ""
        for chunk in response:
            # print(chunk.text)
            gen_text += chunk.text
    return gen_text

# print(getting_data("In the vast landscape of computational structures, there exists a paradigm that embodies both organization and connectivity: the binary tree. Picture a network of nodes, intricately linked in a hierarchical fashion, resembling the branching pattern of a tree. Each node serves as a junction point, branching out into two subtrees, one on the left and one on the right. This binary arrangement facilitates efficient search and traversal algorithms, reminiscent of navigating through the branches of a tree. However, within this structured hierarchy lies a dynamic interplay of nodes, where each node holds a key value and points to two child nodes, akin to a family lineage stretching across generations. Despite its seemingly simple structure, the binary tree harbors complexity and versatility, offering solutions to a wide array of computational challenges, from searching and sorting to optimization and decision-making algorithms."))