import webbrowser
import pyttsx3
import urllib.parse
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import json
from urllib.request import urlopen
import wolframalpha
import subprocess
import shutil
import tkinter
import random
import requests
import operator
import feedparser
import ctypes
from bs4 import BeautifulSoup
from urllib.request import urlopen
import win32com.client as wincl
import time
from countryinfo import CountryInfo
from googletrans import Translator

import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning ")
        speak("How can i Help you today")

    elif 12 <= hour < 18:
        speak("Good Afternoon")
        speak("How can i Help you today")
    else:
        speak("Good Evening")
        speak("How can i Help you today")
def open_google_translate(text):
    base_url = 'https://translate.google.com/'
    params = {'text': text, 'tl': 'en', 'langpair': 'auto|en', 'tbb': '1'}
    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"
    webbrowser.open(url)



def search_wikipedia():
    query = input("What do you want to search for on Wikipedia? ")
    try:
        results = wikipedia.search(query)
        print("Here are the top search results on Wikipedia:")
        for i, result in enumerate(results):
            print(f"{i+1}. {result}")

        selection = input("Please enter the number of the desired result: ")
        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(results):
            print("Invalid selection.")
            return None

        selected_page = wikipedia.page(results[int(selection) - 1])
        summary = selected_page.summary
        speak("According to Wikipedia")
        print(summary)
        option1 = input("Do you want me to speak the result (y/n)")
        if option1.lower() == 'y':
            speak(summary)
        option2 = input("Do you want to translate (y/n)")
        if option2.lower() == 'y':
            open_google_translate(summary)
        else:
            print("Ok, pleasure to help you.")
        return summary

    except wikipedia.exceptions.WikipediaException:
        print("Sorry, an error occurred while searching Wikipedia.")
        return None

    
def find_link():


	search_query = input("Enter your search query: ")

	url = f"https://www.bing.com/search?q={search_query}&count=10"

	headers = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
	    "Accept-Language": "en-US,en;q=0.9",
	    "Accept-Encoding": "gzip, deflate, br",
	    "DNT": "1",
	    "Connection": "keep-alive",
	    "Upgrade-Insecure-Requests": "1"
	}

	response = requests.get(url, headers=headers)

	soup = BeautifulSoup(response.content, "html.parser")

	search_results = soup.select(".b_algo h2 a")

	for result in search_results:
	    link = result["href"]
	    print(link)

def takeCommand():
    try:
        x = input("Do you want to type(t)/ Speak(s)? ")
        if x == 's':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in').lower()
            print(f"User said: {query}\n")
            if query == 'search':
                search_wikipedia()
            elif query == 'find link':
                find_link()
        else:
            if x == 't':
                query = input("Enter your query: ").lower()
                if query == 'search':
                    search_wikipedia()
                elif query == 'find link':
                    find_link()
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    print(query)
    return query

options = {
    "1": takeCommand,
    "2": search_wikipedia,
    "3": find_link,
    "4": None,
    "5": None,
    "6": exit
}

menu_text = """What would you like to do?
1. take Command
2. Search Wikipedia
3. Find Link 
4. [Option 4]
5. [Option 5]
6. Exit
"""

	
if __name__ == '__main__':
	wishme()
	while True:
	    # Display the menu
	    print(menu_text)
	    
	    # Get the user's choice
	    choice = input("Enter the number of your choice: ")
	    
	    # Look up the function corresponding to the user's choice
	    function = options.get(choice)
	    
	    # Call the function, or exit if the choice was invalid or the user chose to exit
	    if function is None:
	        print("Invalid choice. Please try again.")
	    elif function == exit:
	        break
	    else:
	        function()
