# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")
image reddot = "reddot.png" #zoom 0.5
image greendot = "greendot.png"
image yellowdot = "yellowdot.png"
default loadedFromSave = False
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    menu:
        "Do you have a save?"
        "Yes":
            jump saveYesFirst
        "No":
            jump saveNoFirst


label saveYesFirst:
    python:
        loadedFromSave = True
        vocabArray = []
        import os
        fileNames = os.listdir(config.basedir + "/game/gameSaves")
        fileChoice = renpy.display_menu([(name, name) for name in fileNames])
        fileChoiceUpdated = "/game/gameSaves/" + fileChoice

        with open(config.basedir + fileChoiceUpdated, "r") as f:
            content = f.readlines()
            for line in content:
                a = [x.strip() for x in line.split(";")]
                vocabArray.append(a)
    jump mainGame

label saveNoFirst:

    init python:
        loadedFromSave = False
        vocabArray = []
        with open(config.basedir + "/game/vocablists/kapital1vocab.txt", "r") as f:
            content = f.readlines()
            for line in content:
                a = [x.strip() for x in line.split(";")]
                a.extend("0")
                vocabArray.append(a)

    jump mainGame

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
label mainGame:
    python:
        gameLength = renpy.input("How many rounds would you like to play?", length=2)
        gameLength = gameLength.strip()

        if not gameLength:
            gameLength = 10

        roundsPlayed = 0
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
    menu:
        "Which unit would you like to practice?"
        "Kapital 1":
            jump Kapital1
        # "Kapital 2":
        #     jump Kapital2
        # "Kapital 3":
        #     jump Kapital3
        # "Kapital 4":
        #     jump Kapital4
        # "Kapital 5":
        #     jump Kapital5
        # "Kapital 6":
        #     jump Kapital6
        # "Kapital 7":
        #     jump Kapital7
        # "Kapital 8":
        #     jump Kapital8
        # "Kapital 9":
        #     jump Kapital9

label Kapital1:
    python:
        redList = []
        yellowList = []
        greenList = []
        weights = [("yellowList", 70), ("redList", 25), ("greenList", 5)]
        for thingy in range(0, (len(vocabArray)-1)):
            if int(vocabArray[thingy][2]) < 4:
                redList.append(vocabArray[thingy])
            elif int(vocabArray[thingy][2]) > 3 and int(vocabArray[thingy][2]) < 10:
                yellowList.append(vocabArray[thingy])
            else:
                greenList.append(vocabArray[thingy])

        randval = renpy.random.random() * 100
        for choice, weight in weights:
            if randval <= weight:
                listChoice = choice
            else:
                randval -= weight



        index1 = renpy.random.randint(1, len(listChoice)) - 1
        index2 = renpy.random.randint(1, len(vocabArray)) - 1
        index3 = renpy.random.randint(1, len(vocabArray)) - 1
        index4 = renpy.random.randint(1, len(vocabArray)) - 1
        vocabArrayVersion = vocabArray.index(listChoice[index1])
        answerList = [(listChoice[index1][1]), (vocabArray[index2][1]), (vocabArray[index3][1]), (vocabArray[index4][1])]
        # orderList = [0,1,2,3]
        # renpy.random.shuffle(orderList)
        # item1 = orderList[0]
        # item2 = orderList[1]
        # item3 = orderList[2]
        # item4 = orderList[3]
        # e((vocabArray[index1][0]), interact=False)
        # choices = renpy.display_menu([((answerList[item1]), correct), ((answerList[item2]), "false"), ((answerList[item3]), "false") , ((answerList[item4]), "false")])
        vocabQuestion = listChoice[index1][0]
        correctAnswer = listChoice[index1][1]
        vocabCurrentScore = listChoice[index1][2]
        renpy.random.shuffle(answerList)
        firstOption = answerList[0]
        secondOption = answerList[1]
        thirdOption = answerList[2]
        fourthOption = answerList[3]
        #if 0 < 3:
        if int(vocabCurrentScore) < 4:
            indicatorColor = "images/reddot.png"
        elif int(vocabCurrentScore) > 3 and int(vocabCurrentScore) < 10:
            indicatorColor = "images/yellowdot.png"
        else:
            indicatorColor = "images/greendot.png"


        # if int(vocabCurrentScore) > 9:
        #     indicatorColor = "images/greendot.png"
        # if int(vocabCurrentScore) < 10 and int(vocabCurrentScore) > 2:
        #     indicatorColor = "images/yellowdot.png"
        # else:
        #     indicatorColor = "images/reddot.png"
        # # firstOptionScore = vocabArray[]
        # secondOptionScore
        # thirdOptionScore
        # fourthOptionScore
        # choice = renpy.display_menu([(vocab[0], vocab[1]) for vocab in answerList])
    menu:
        "[vocabCurrentScore]"
        #"{image=[indicatorColor]} [vocabQuestion]"
        "[indicatorColor] [vocabQuestion]"
        "[firstOption]":
            if firstOption == correctAnswer:
                jump correct
            else:
                jump false
        "[secondOption]":
            if secondOption == correctAnswer:
                jump correct
            else:
                jump false
        "[thirdOption]":
            if thirdOption == correctAnswer:
                jump correct
            else:
                jump false
        "[fourthOption]":
            if fourthOption == correctAnswer:
                jump correct
            else:
                jump false
label Broken:
    e "you found the issue"
    return
label correct:
    python:
        scored = int(vocabCurrentScore)
        scored += 1
        vocabArray[vocabArrayVersion][2] = scored
        roundsPlayed += 1
    e "Correct!"
    python:
        if roundsPlayed < int(gameLength):
            renpy.jump("Kapital1")
        else:
            renpy.jump("EndGame")

label EndGame:
    menu:
        "You have finished the game. Would you like to save?"
        "Yes":
            if loadedFromSave == True:
                python:
                    with open(config.basedir + fileChoiceUpdated, "r+") as g:
                        for chunk in range(0, (len(vocabArray)-1)):
                            f.write((vocabArray[chunk][0]) + ";" + (vocabArray[chunk][1]) + ";" + (vocabArray[chunk][2]) + "\n")
                return
            else:
                python:
                    saveName = renpy.input("What would you like to name this save?")
                    saveNameUpdated = "/game/gameSaves/" + saveName
                    import os

                    with open(config.basedir + saveNameUpdated, "w") as h:
                        for chunk in range(0, (len(vocabArray)-1)):
                            f.write((vocabArray[chunk][0]) + ";" + (vocabArray[chunk][1]) + ";" + (vocabArray[chunk][2]) + "\n")
                return

        "No":
            return

label false:
    python:
        correctAnswer = listChoice[index1][1]
    e "Incorrect. The answer was [correctAnswer]."
    python:
        roundsPlayed += 1
        if roundsPlayed < int(gameLength):
            renpy.jump("Kapital1")
        else:
            renpy.jump("EndGame")

    # This ends the game.
    #THe game does not choose the false condition. fuck.
