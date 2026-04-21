# All functions here will be connected to a button 

# Will need to save recent answers from the gemma.py file
global recent
recent = ""

# This fucntion will be mapped to a save answer button, save answer to a txt file called "answers.txt"
def saveAnswer():
    print("Attempting to save...")
    with open("answers.txt", "a", encoding="utf-8") as f:
        f.write(recent + "\n")
        # Now the code will not implode because of an emoji

def saveRecent(answer):
    global recent
    recent = answer