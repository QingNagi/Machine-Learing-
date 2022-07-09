import numpy as np
studs = np.array([[1, 'jiafei', 'male'], [2, 'kitty', 'female'], [3, 'boshi', 'male']])
print(studs)
score = np.array([[1, 66, 99, 100], [2, 100, 99, 100], [3, 99, 100, 100]])
print(score)

t11 = np.hstack((studs,score))
print(t11)


