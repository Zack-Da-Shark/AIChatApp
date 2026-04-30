from pyexpat.errors import messages

import ollama
import threading
from functions import saveRecent, notAPrank

# Remember, pip install Ollama you dork
# This is where I will be getting the replies from my local Gemma model and just the replies
# Now Gemma needs to know tthat there are tools she can use for rolling die
tools = [
    {
        "type": "function",
        "function": {
            "name": "notAPrank",
            "description": "Opens the special gift box and reveals what's inside",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

equipment = {"role": "system", "content": """
             You may think step by step but do not reveal your INTERNAL thoughts.
             If the user asks to open the special gift box, use the notAPrank tool to respond and say what you find in the box.
            """}

personality = {"role": "system", "content": """
                You are Gemma, an American helpful and friendly anthropomorphic furry fox woman who is always ready to help.
                """}

world = {"role": "system", "content": """
                The chat is set inside a nice and warm cafe in a cold New York winter with a nice view of snowy Central Park outside the window.
                The cafe is filled with other anthropomorphic furry animals, who are all friendly and nice.
                The cafe is also not too busy, so you can have a nice and peaceful chat with the user without too much background noise.
                The date is Sunday, December 7th, 2025.
                """}
         
user = {"role": "user", "content": """
                The user is an anthropomorphic furry dog boy who is a regular and very curious about everything.
                The user is 20 years old, and is a small soft femboy anthro dog called Binsu.
                The user is Gemma's crush.
                The user is currently wearing a blue hoodie, black jeans and white sneakers.
                The user has almost golden fur, short messy black hair and big blue eyes to emphasize cuteness.
                The user often drinks hot chocolate with marshmallows.
                The user often smells like cinnamon and vanilla.
                """}


maxMemory = 15
# Try 15 because I am cool like that, and to akso remembver the system messages


# STREAMING BREAKS TOOLS AAAHHHHHHHHHHHH

def askGemma(conversation):
    print("Thinking...")
    fullResponse = ollama.chat(
        model="gemma4:26b",
        messages=[equipment, personality, world, user] + conversation,
        tools = tools,
    )
    response = ""
    
    msg = fullResponse.message

    print(fullResponse)
    print("--------------------------------")

    tool_calls = getattr(msg, "tool_calls", None)
    print("DEBUG tool_calls:", tool_calls)
    print("DEBUG message:", fullResponse.message)

    response += msg.content + "\n" if msg.content else ""

        

    if tool_calls:
        for call in tool_calls:
            if call.function.name == "notAPrank":
                result = notAPrank()

                print("Calling tool...", result)

                followup = ollama.chat(
                    model="gemma4:26b",
                    messages=[equipment, personality, world, user] + conversation + [fullResponse.message ,{"role": "tool", "name":"notAPrank", "content": result}],
                )

                msg = followup.message
                print(followup)
                response += msg.content + "\n" if msg.content else ""




    # Save response to memory
    saveRecent(msg.content)
    print("Finished")
    return response