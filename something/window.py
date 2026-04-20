# This file will be repsonisble for the UI / UX features
# Will be using customtkinter for the UI
# pip install customtkinter
# Installed correctly

import customtkinter

app = customtkinter.CTk()
app.title("Talk to Gemma")
app.geometry("1600x900")

# add the chatbox and input fields
inputBox = customtkinter.CTkEntry(app, width=1000, height=40)
inputBox.pack(pady=20)

# Need to implement functionality but looks good

textbox = customtkinter.CTkTextbox(app, width=1000, height=400, state="disabled", wrap="word")
textbox.insert("0.0", "Welcome to the Gemma chat! Ask me anything!")
textbox.configure(state="disabled")
textbox.pack(pady=20)


app.mainloop()