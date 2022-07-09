import numpy as np
score = np.random.randint(50, 101, (3, 40))  # 3行为3科目成绩
print(score)
score.sort(axis=1)
print(score)

p20 = np.percentile(score, 20, axis=1)   # 求各科目的p20
print(p20)
Chinese = score[0]
Match = score[1]
English = score[2]
print(Chinese <= p20[0])
print(Match <= p20[1])
print(English[English <= p20[2]])


Max = np.max(score, axis=1)
print(Max)
Min = np.min(score, axis=1)
print(Min)
Mean = np.mean(score, axis=1)
print(Mean)
S = score[0] + score[1] +score[2]
S.sort()
print(S)
print(S[-3:])  # 前三
