# This file will be repsonisble for the UI / UX features
# Will be using customtkinter for the UI
# pip install customtkinter
# Installed correctly

import customtkinter
import threading
from conversation import sendQuery
from functions import saveAnswer, saveAnswer

response = ""

app = customtkinter.CTk()
app.title("Talk to Gemma")
app.geometry("1600x900")

# add the chatbox and input fields
inputBox = customtkinter.CTkEntry(app, width=1000, height=40)
inputBox.pack(pady=20)

# Hit enter to send the message
inputBox.bind("<Return>", lambda event: sendMessage())

def handoff(query):
    # Sends the query to the conversation handler and gets the response
    # Outlining this so I can run this on a separate thread to avoid freezing the UI
    response = sendQuery(query)
    textbox.configure(state="normal")
    textbox.insert("end", f"\nYou: {query}\nGemma: {response}\n")
    textbox.configure(state="normal")

    # re-enable the text box you moron

    inputBox.configure(state="normal")
    textbox.configure(state="disabled")

# Send the input to the conversation handler and get the response, then display it in the chatbox
def sendMessage():
    # Should probably add a thread here to avoid UI freezing

    # Get query before resetting the input box you donut
    query = inputBox.get()

    # Reset and disable the inputbox
    inputBox.delete(0, "end")
    inputBox.configure(state="disabled")


    # Send off the request
    threading.Thread(target=handoff, args=(query,)).start()
    # Now how do I get the response now? I could declare a global variable, it screwed the threading, a queue is being suggsted here
    # Perhaps if I move a few lines


# Need to implement functionality but looks good

textbox = customtkinter.CTkTextbox(app, width=1000, height=400, state="disabled", wrap="word")
textbox.insert("0.0", "Welcome to the Gemma chat! Ask me anything!")
textbox.configure(state="disabled")
textbox.pack(pady=20)

# Or click a button to send the message
sendButton = customtkinter.CTkButton(app, text="Send", command=sendMessage)
sendButton.pack(pady=10)

# Save the answer button fucntionality, doesn't get full answer, fuckk
# Maybe I can use the global variable, please do not implode everything
saveButton = customtkinter.CTkButton(app, text="Save Answer", command=lambda: saveAnswer())
saveButton.pack(pady=10)

app.mainloop()