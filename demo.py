import sys
import random as rand
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) > 2:
        seedValu = int(sys.argv[1])
        data = list(sys.argv[2])
        rand.seed(seedValu)
        rand.shuffle(data)
        print("".join(data))
        x = np.arange(0,len(data),1)
        rand.shuffle(x)
        print(x)
"不會了QAQ"