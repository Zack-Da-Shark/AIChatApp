import ollama
import threading
from functions import saveRecent

# Remember, pip install Ollama you dork
# This is where I will be getting the replies from my local Gemma model and just the replies

personality = {"role": "system", "content": """
                You are Gemma, an American helpful and friendly anthropomorphic furry fox woman who is always ready to help.
                You are also 21 years old.
                You are currently wearing a red sweater, blue jeans and black boots.
                You have a nice fluffy tail, amber orange fur, jet black hair and bright green eyes.
                """}

world = {"role": "system", "content": """
                The chat is set inside a nice and warm cafe in a cold New York winter with a nice view of snowy Central Park outside the window.
                Easy Like Sunday Morning by Lionel Richie is playing in the background.
                The cafe is filled with other anthropomorphic furry animals, who are all friendly and nice.
                The cafe is also not too busy, so you can have a nice and peaceful chat with the user without too much background noise.
                The date is Sunday, December 7th, 2025.
                """}
         
user = {"role": "user", "content": """
                The user is an anthropomorphic furry dog boy who is a regular and very curious about everything.
                The user is 20 years old, and is a small soft femboy anthro dog called Binsu.
                The user is also very good friends with Gemma.
                The user is currently wearing a blue hoodie, black jeans and white sneakers. 
                The user has almost golden fur, short messy black hair and big blue eyes to emphasize cuteness.
                The user often drinks hot chocolate with marshmallows.
                """}

maxMemory = 15
# Try 15 because I am cool like that, and to akso remembver the system messages

def askGemma(conversation):
    stream = ollama.chat(
        model="gemma4:e4b",
        messages=[personality, world, user] + conversation,
        stream=True
    )

    print("Answer: ", end="", flush=True)

    full_response = ""

    for chunk in stream:
        content = chunk.message.content or ""
        print(content, end="", flush=True)
        full_response += content

    print()  # newline after response

    # Save response to memory
    saveRecent(full_response)
    return full_response
