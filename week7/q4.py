def ScoreList():
    List=[]
    for x in range(5):
        List.append(int(input('Enter Score= ')))
    return List

def TotalScore(Scores):
    Total=0
    for score in Scores:
        Total += score
    return Total

print(f"Total Score= {TotalScore(ScoreList())}")