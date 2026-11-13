# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")
image reddot = "reddot.png" #zoom 0.5
image greendot = "greendot.png"
image yellowdot = "yellowdot.png"


# default loadedFromSave = False
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    jump mainmenu

    # menu:
    #     "Do you have a save?"
    #     "Yes":
    #         jump saveYesFirst
    #     "No":
    #         jump saveNoFirst

#
# label saveYesFirst:
#     python:
#         # loadedFromSave = True
#         vocabArray = []
#         import os
#         fileNames = os.listdir(config.basedir + "/game/gameSaves")
#         fileChoice = renpy.display_menu([(name, name) for name in fileNames])
#         fileChoiceUpdated = "/game/gameSaves/" + fileChoice
#
#         with open(config.basedir + fileChoiceUpdated, "r") as f:
#             content = f.readlines()
#             for line in content:
#                 a = [x.strip() for x in line.split(";")]
#                 vocabArray.append(a)
#     jump mainGame
#
# label saveNoFirst:
label mainmenu:


#     jump mainGame
#
#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.
# label mainGame:

    # python:
    #     gameLength = renpy.input("How many rounds would you like to play?", length=2)
    #     gameLength = gameLength.strip()
    #
    #     if not gameLength:
    #         gameLength = 10

        # roundsPlayed = 0
    # These display lines of dialogue.
    menu:
        "Which level would you like to practice?"
        "A1":
            jump A1
        # "A2":
        #     jump A2
        # "All":
        #     jump All


label A1:
    python:
        redListTempK1 = []
        yellowListTempK1 = []
        greenListTempK1 = []
        redListTempK2 = []
        yellowListTempK2 = []
        greenListTempK2 = []
        for thingy in range(0, (len(A1K1vocabArray))):
            if int(A1K1vocabArray[thingy][2]) < 4:
                redListTempK1.append(A1K1vocabArray[thingy])
            elif int(A1K1vocabArray[thingy][2]) > 3 and int(A1K1vocabArray[thingy][2]) < 10:
                yellowListTempK1.append(A1K1vocabArray[thingy])
            else:
                greenListTempK1.append(A1K1vocabArray[thingy])
        for thingy in range(0, (len(A1K2vocabArray))):
            if int(A1K2vocabArray[thingy][2]) < 4:
                redListTempK2.append(A1K2vocabArray[thingy])
            elif int(A1K2vocabArray[thingy][2]) > 3 and int(A1K2vocabArray[thingy][2]) < 10:
                yellowListTempK2.append(A1K2vocabArray[thingy])
            else:
                greenListTempK2.append(A1K2vocabArray[thingy])
        A1K1Learned = round((len(yellowListTempK1)/len(A1K1vocabArray) * 100), 1)
        A1K1Complete = round((len(greenListTempK1)/len(A1K1vocabArray) * 100), 1)
        A1K2Learned = round((len(yellowListTempK2)/len(A1K2vocabArray) * 100), 1)
        A1K2Complete = round((len(greenListTempK2)/len(A1K2vocabArray) * 100), 1)
    define A1K1LearnedText = _("[A1K1Learned]%")
    define A1K1CompleteText = _("[A1K1Complete]%")
    define A1K2LearnedText = _("[A1K2Learned]%")
    define A1K2CompleteText = _("[A1K2Complete]%")

    menu:
        "Which unit would you like to practice?"
        "Kapital 1 {color=#DA2} [A1K1LearnedText!ti] {/color}{color=#4C0}[A1K1CompleteText!ti] {/color}":
            jump A1Kapital1
        "Kapital 2 {color=#DA2}[A1K2LearnedText!ti] {/color}{color=#4C0}[A1K2CompleteText!ti]{/color}":
            jump A1Kapital2
        # "Kapital 3":
        #     jump A1Kapital3
        # "Kapital 4":
        #     jump A1Kapital4
        # "Kapital 5":
        #     jump A1Kapital5
        # "Kapital 6":
        #     jump A1Kapital6
        # "Kapital 7":
        #     jump A1Kapital7
        # "Kapital 8":
        #     jump A1Kapital8
        # "Kapital 9":
        #     jump A1Kapital9



label EndGame:
    menu:
        "Return to menu.":
            jump mainmenu
    # menu:
    #     "You have finished the game. Would you like to save?"
    #     "Yes":
    #         if loadedFromSave == True:
    #             python:
    #                 with open(config.basedir + fileChoiceUpdated, "r+") as g:
    #                     for chunk in range(0, (len(vocabArray)-1)):
    #                         f.write((vocabArray[chunk][0]) + ";" + (vocabArray[chunk][1]) + ";" + (vocabArray[chunk][2]) + "\n")
    #             return
    #         else:
    #             python:
    #                 saveName = renpy.input("What would you like to name this save?")
    #                 saveNameUpdated = "/game/gameSaves/" + saveName
    #                 import os
    #
    #                 with open(config.basedir + saveNameUpdated, "w") as h:
    #                     for chunk in range(0, (len(vocabArray)-1)):
    #                         f.write((vocabArray[chunk][0]) + ";" + (vocabArray[chunk][1]) + ";" + (vocabArray[chunk][2]) + "\n")
    #             return
    #
    #     "No":
    #         return


label gameLengthLabel:
    menu:
        "How many questions do you want?"
        "Short (5)":
            $ gameLength = 5
        "Medium (10)":
            $ gameLength = 10
        "Long (20)":
            $ gameLength = 20
    python:
        roundsPlayed = 0
    return
    # This ends the game.
    #THe game does not choose the false condition. fuck.
