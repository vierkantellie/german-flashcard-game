label A1Kapital1:
    call gameLengthLabel
    init python:
        # loadedFromSave = False
        A1K1vocabArray = []
        with open(config.basedir + "/game/vocablists/A1Kapital1.txt", "r") as f:

#        with open(config.basedir + "/game/vocablists/kapital1vocab.txt", "r") as f:
            content = f.readlines()
            for line in content:
                a = [x.strip() for x in line.split(";")]
                a.extend("0")
                A1K1vocabArray.append(a)
    jump A1Kapital1Game

label A1Kapital1Game:
    python:
        redList = []
        yellowList = []
        greenList = []
        weights = [(yellowList, 70), (redList, 25), (greenList, 5)]


        for thingy in range(0, (len(A1K1vocabArray))):
            if int(A1K1vocabArray[thingy][2]) < 4:
                redList.append(A1K1vocabArray[thingy])
            elif int(A1K1vocabArray[thingy][2]) > 3 and int(A1K1vocabArray[thingy][2]) < 10:
                yellowList.append(A1K1vocabArray[thingy])
            else:
                greenList.append(A1K1vocabArray[thingy])
        weightsIterable = []
        for member in range(0, len(weights)):
            if len(weights[member][0]) > 0:
                weightsIterable.append(weights[member])
        # if len(yellowList) == 0 and len(greenList) == 0:
        #     listChoice = redList
        # else:
        totalWeight = 0
        for choice, weight in weightsIterable:
            totalWeight += weight
        randval = renpy.random.random() * totalWeight
        for choice, weight in weightsIterable:
            if randval <= weight:
                listChoice = choice
            else:
                randval -= weight



        index1 = renpy.random.randint(0, len(listChoice)-1)
        index2 = renpy.random.randint(0, len(A1K1vocabArray)-1)
        index3 = renpy.random.randint(0, len(A1K1vocabArray)-1)
        index4 = renpy.random.randint(0, len(A1K1vocabArray)-1)
        print("loop")
        print(listChoice)
        print("yellow", yellowList)
        print("red", redList)
        print("full", A1K1vocabArray)
        A1K1vocabArrayVersion = A1K1vocabArray.index(listChoice[index1])
        answerList = [(listChoice[index1][1]), (A1K1vocabArray[index2][1]), (A1K1vocabArray[index3][1]), (A1K1vocabArray[index4][1])]
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
        vocabCurrentScore = A1K1vocabArray[A1K1vocabArrayVersion][2]
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
        "{image=[indicatorColor]} [vocabQuestion]"
        #"[indicatorColor] [vocabQuestion]"
        "[firstOption]":
            if firstOption == correctAnswer:
                jump .correct
            else:
                jump .false
        "[secondOption]":
            if secondOption == correctAnswer:
                jump .correct
            else:
                jump .false
        "[thirdOption]":
            if thirdOption == correctAnswer:
                jump .correct
            else:
                jump .false
        "[fourthOption]":
            if fourthOption == correctAnswer:
                jump .correct
            else:
                jump .false
# label Broken:
#     e "you found the issue"
#     return
label A1Kapital1Game.correct:
    python:
        scored = int(vocabCurrentScore)
        scored += 1
        A1K1vocabArray[A1K1vocabArrayVersion][2] = scored
        roundsPlayed += 1
    e "Correct!"
    python:
        if roundsPlayed < int(gameLength):
            renpy.jump("A1Kapital1Game")
        else:
            renpy.jump("EndGame")

label A1Kapital1Game.false:
    python:
        correctAnswer = listChoice[index1][1]
    e "Incorrect. The answer was [correctAnswer]."
    python:
        roundsPlayed += 1
        if roundsPlayed < int(gameLength):
            renpy.jump("A1Kapital1Game")
        else:
            renpy.jump("EndGame")
