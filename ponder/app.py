#app script

import random 

philosophers = ("Aristotle", "Plato", "Confucius", "Marcus Aurelius", "Diogenes", "Sisyphus")
topics = ("Pessimistic views", "Optimistic views", "Morals", "What they stood for", "Relation to hardship", "Relation to the modern man")

def pick_story_objects():
    # Pick random Philosopher
    todays_philosopher = random.choice(philosophers)
    
    # Pick random Topic
    todays_topic = random.choice(topics)
    
    return todays_philosopher, todays_topic

import os

# Get Context
def get_context():
    try:
        root_dir = os.getcwd()  # Get current working directory (usually the root directory)
        file_path = os.path.join(root_dir, 'context', 'context.txt')
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File 'context.txt' not found in context directory.")
        return "File 'context.txt' not found in context directory."
    except Exception as e:
        print(f"Error reading context file: {e}")
        return f"An error occurred: {e}"

# Get style to write in
def get_style():
    try:
        root_dir = os.getcwd()  # Get current working directory (usually the root directory)
        file_path = os.path.join(root_dir, 'context', 'style.txt')
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File 'style.txt' not found in context directory.")
        return "File 'style.txt' not found in context directory."
    except Exception as e:
        print(f"Error reading style file: {e}")
        return f"An error occurred: {e}"