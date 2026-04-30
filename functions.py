# All functions here will be connected to a button 
import subprocess
import json

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


mcpProcess = None

def startDieServer():
    global mcpProcess
    if mcpProcess is None:
        mcpProcess = subprocess.Popen(["python", "-m", "mcp_dice_roller"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Die server started.")
    else:
        print("Die server is already running.")
# ATTEMPTING TO INSTALL AN MCP TOOL TO GET HER TO USE DICE ROLLERS
# WISH ME LUCK WITH THIS ONE BOI, I HOPE IT WORKS

# EVERYTHING IS ON FIRE

# Manula call, just in case I blow everything up
def roll_dice(notation="1d20"):
    import random
    # TEMP fallback so you don’t go insane debugging MCP yet
    print(f"(Fallback dice) Rolling {notation}")
    return f"🎲 You rolled {random.randint(1,20)}"

# Random basic tool to test MCP integration
def notAPrank():
    return "This is a prank"