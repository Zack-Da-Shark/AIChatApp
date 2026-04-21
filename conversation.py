# This script will handle the conversation betwwen the user and the AI
from gemma import askGemma

# Initialise conversation memory, system messages already in the gemma.py file
conversation = []
maxMemory = 12
# 12 because I am cool like that B)

def sendQuery(query):
    # Sending a query to Gemma and gettting the response
    # But first, append query tto conversation memory
    conversation.append({"role": "user", "content": query})
    # Send the entire conversation
    response = askGemma(conversation)

    # Append response
    conversation.append({"role": "assistant", "content": response})

    # Manage memory size
    if len(conversation) > maxMemory:
        conversation.pop(0)
        conversation.pop(0)
        # Remove both the query and response

    # Return the response to be displayed on the UI
    return response