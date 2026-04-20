# This file will be repsonisble for the UI / UX features
# Will be using customtkinter for the UI
# pip install customtkinter
# Installed correctly

import customtkinter
import threading
from conversation import sendQuery

app = customtkinter.CTk()
app.title("Talk to Gemma")
app.geometry("1600x900")

# add the chatbox and input fields
inputBox = customtkinter.CTkEntry(app, width=1000, height=40)
inputBox.pack(pady=20)

# Hit enter to send the message
inputBox.bind("<Return>", lambda event: sendMessage())

# Send the input to the conversation handler and get the response, then display it in the chatbox
def sendMessage():
    # Should probably add a thread here to avoid UI freezing

    query = inputBox.get()

    # It might help if you IMPORT THE CONVERSATION MODULE YOU ABSOLUTE POTATO
    # *ahem* so smart yet so dumb
    response = sendQuery(query)

    # Reset the inputbox
    inputBox.delete(0, "end")
    
    # Display the query to the chatbox
    textbox.configure(state="normal")
    textbox.insert("end", f"\nYou: {query}\nGemma: {response}\n")
    textbox.configure(state="disabled")
    inputBox.delete(0, "end")

# Need to implement functionality but looks good

textbox = customtkinter.CTkTextbox(app, width=1000, height=400, state="disabled", wrap="word")
textbox.insert("0.0", "Welcome to the Gemma chat! Ask me anything!")
textbox.configure(state="disabled")
textbox.pack(pady=20)

# Or click a button to send the message
sendButton = customtkinter.CTkButton(app, text="Send", command=sendMessage)
sendButton.pack(pady=10)

app.mainloop()