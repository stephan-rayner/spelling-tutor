#!/usr/bin/env python

import time
import random
import subprocess
from language import TEXT

# WORDS, LANGUAGE = ["hill", "puff", "toss", "buzz", "fizz", "smell", "sniff", "grass", "press", "still"], "en"
WORDS, LANGUAGE = ["fraise", "balai", "vrai", "jamais", "lait", "beige", "neige", "pleine", "reine", "seize"], "fr"

def say(message, language="en"):
    # print(message, language)
    if language == "fr":
        cmd = ["say", "--voice", "Amélie (Premium)"]
    elif language == "en":
        cmd = ["say"]
    else:
        print("Language is not correct")
        exit(2)
    
    result = subprocess.run([*cmd, f"{message}"], capture_output=True, text=True)
    return result.stdout

def main(words: list[str], messages: dict[str, str]):
    
    words = [w.lower() for w in WORDS]

    for word in WORDS:
        request =  messages["request_template"].format(word)
        say(request, LANGUAGE)

        result = input("Type answer here: ").lower()
        if result == word:
            say(messages["correct"], LANGUAGE)
        else:
            say(messages["incorrect"], LANGUAGE)

        time.sleep(1)

if __name__ == "__main__":
    random.shuffle(WORDS)
    messages = TEXT[LANGUAGE]
    main(WORDS, messages)
