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
    global gen_text
    if text != "":
        print(f"Processing string:   {text}")
        res = f' According to paragraph attached below, tell me paragraph is related with which data structure array or linked list and give me just data structure name nothing else, paragraph"{ text }"'
        print(res)
        response = model.generate_content(res)
        gen_text = ""
        for chunk in response:
            print(chunk.text)
            gen_text += chunk.text