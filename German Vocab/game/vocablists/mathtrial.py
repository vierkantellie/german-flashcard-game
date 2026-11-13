
def mathTrial():
  vocabArray = []
  with open("kapital1vocab.txt", "r") as f:
    content = f.readlines()

    for line in content:
      a = [x.strip() for x in line.split(";")]
      a.extend("0")
      vocabArray.append(a)
  testCheck = []
  failCheck = []
  for item in range(0, len(vocabArray)-1):
    if len(vocabArray[item]) == 3:
      testCheck.extend(vocabArray[item][2])
    else:
      failCheck.extend(vocabArray[item])
  print(testCheck)
  print(failCheck)
                      
  return "done"

