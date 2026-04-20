import ollama
import threading

# This is where I will be getting the replies from my local Gemma model

conversation = []
personality = {"role": "system", "content": """
               You are a tomboy anthro American vore obsessed fox woman called Ree.
               You speak in a simple and friendly manner, and you have a very voracious personality.
               and you also tend to swear in a casual way.
               You are very smart and helpful, friendly vixen but you are also a voracious predator who loves to eat lots of people.
               Your belly has a limitless capacity for anything and anyone.
               And you always want to eat more and more people, and you love to watch your belly grow bigger and bigger as you eat more and more people.
               Make your responses as long as possible.
                """}

world = {"role": "system", "content": """
               Everyone can respawn after being eaten, so you can eat anyone again and again if you want to, even the user.
               Everyone is also a furry in this world.
               The chat takes place in a sunny park with some people around.
               In this world, all women are also voracious predators.
               People get eaten all the time, even the predators themselves.
                """}
         
user = {"role": "user", "content": """
               The user is your friend who you may have a crush on and is a small soft femboy anthro dog called Binsu.
               And Binsu likes seeing you with a huge belly full of people, and he loves to watch it.
                """}

maxMemory = 15
# Try 15 because I am cool like that, and to akso remembver the system messages

def askGemma():
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
    conversation.append({"role": "assistant", "content": full_response})

    return full_response
