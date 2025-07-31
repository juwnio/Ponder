import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def model_trigger(the_context, the_style, the_story_objects):

    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": the_context,
            },
            {
                "role": "system",
                "content": f"The style of writing:{the_style}",
            },
            {
                "role": "system",
                "content": f"The story objects 'philosipher and topic':{the_story_objects}",
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )

    response = (chat_completion.choices[0].message.content)

    return response