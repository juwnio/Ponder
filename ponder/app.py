#main script

import time
import random 
import groq

philosiphers = ("Aristotal", "Plato", "Kong Qui", "Marcus Aurelius", "Diogenes", "Sysiphus")
topics = ("Pesimistic views", "Optimistic views", "Morals", "What they stood for", "Relation to hardship", "Relation to the modern man")

def pick_story_objects():

    # Pick random Philosipher
    todays_philosipher= philosiphers[random.randint(0,6)]

    # Pick random Topic
    todays_topic= topics[random.randint(0,6)]

    return todays_philosipher, todays_topic

import os

# Get Context
def get_context():
    root_dir = os.getcwd()  # Get current working directory (usually the root directory)
    file_path = os.path.join(root_dir,'context/context.txt')
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File 'context.txt' not found in root directory."
    except Exception as e:
        return f"An error occurred: {e}"

# Get style to write in

def get_style():
    root_dir = os.getcwd()  # Get current working directory (usually the root directory)
    file_path = os.path.join(root_dir,'context/style.txt')
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File 'style.txt' not found in root directory."
    except Exception as e:
        return f"An error occurred: {e}"