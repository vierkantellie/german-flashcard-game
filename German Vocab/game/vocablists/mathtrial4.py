def trial():
    vocabArray = []
    with open("kapital1vocab.txt", "r") as f:
            content = f.readlines()
            for line in content:
                a = [x.strip() for x in line.split(";")]
                a.extend("0")
                vocabArray.append(a)
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
    if len(yellowList) == 0 and len(greenList) == 0:
        listChoice = redList
    else:
        randval = 4
        for choice, weight in weights:
            if randval <= weight and len(choice) != 0 :
                listChoice = choice
            else:
                randval -= weight

    index1 = 5
    vocabArrayVersion = vocabArray.index(listChoice[index1])
    print(len(listChoice))
    print("yellowlist", yellowList)
    print("redList", redList)
    print("greenList", greenList)
    print(vocabArrayVersion)
    print(listChoice[index1])
    print(vocabArray[vocabArrayVersion])
    scored = 0
    scored += 1
    vocabArray[vocabArrayVersion][2] = scored
    print(vocabArray[vocabArrayVersion])
    return greenList
