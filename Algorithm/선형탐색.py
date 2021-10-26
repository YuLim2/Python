import random

numList =(1, 5, 7, 13, 50, 120, 300, 320, 400, 700)

for k in range(10):
    cntSum = 0
    for i in range(10000):
        rndNum = numList[random.randint(0,9)]
        for n in numList:
            cntSum += 1
            if n == rndNum:
                break
    print(cntSum/10000)