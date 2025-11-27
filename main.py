#!/usr/bin/env python

import time
import random
import subprocess

def say(message, language="en"):
    # print(message, language)
    if language == "fr":
        cmd = ["say", "--voice", "Thomas"]
    elif language == "en":
        cmd = ["say"]
    else:
        print("Language is not correct")
        exit(2)
    
    result = subprocess.run([*cmd, f"{message}"], capture_output=True, text=True)
    return result.stdout
    


words = ["hill", "puff", "toss", "buzz", "fizz", "smell", "sniff", "grass", "press", "still"]
# words = ["fraise", "balai", "vrai", "jamais", "lait", "beige", "neige", "pleine", "reine", "seize"]


random.shuffle(words)

for word in words:
    msg = f"Please spell {word}"
    say(msg, "en")

    result = input("Type answer here: ")
    if result == word:
        say("That is correct!")
    else:
        say("That is not quite correct")
    
    time.sleep(1)
