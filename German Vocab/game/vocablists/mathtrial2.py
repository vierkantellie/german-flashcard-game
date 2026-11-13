def trial():
    vocabArray = []
    with open("testlisttest.txt", "r") as f:
        content = f.readlines()
        for line in content:
            a = [x.strip() for x in line.split(";")]
            vocabArray.append(a)
    redList = []
    yellowList = []
    greenList = []
    for thingy in range(0, (len(vocabArray)-1)):
        if int(vocabArray[thingy][2]) < 4:
            redList.append(vocabArray[thingy])
        elif int(vocabArray[thingy][2]) > 3 and int(vocabArray[thingy][2]) < 10:
            yellowList.append(vocabArray[thingy])
        else:
            greenList.append(vocabArray[thingy])
    print(redList)
    print(yellowList)
    print(greenList)
    return
