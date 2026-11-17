# def germanWords():
#     German = []
#     with open("vocabToBeCompiledGerman.txt", "r") as G:
#         words = G.readlines()
#         for line in words:
#             German.append(line.strip())
#     return German
#
#
# def englishWords():
#     English = []
#     with open("germanWordsTranslated.txt", "r") as E:
#         words = E.readlines()
#         for line in words:
#             English.append(line.strip())
#     return English

def runCompiler():
    German = []
    English = []
    with open("vocabToBeCompiledGerman.txt", "r") as G:
        words = G.readlines()
        for line in words:
            German.append(line.strip())
    with open("germanWordsTranslated.txt", "r") as E:
        translated = E.readlines()
        for line in translated:
            English.append(line.strip())
    with open("vocabCompiled.txt", "w") as V:
        for item in range(0, len(German)):
            V.write(f"{German[item]} ; {English[item]}\n")
    return
