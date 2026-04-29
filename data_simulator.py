import pandas as pd
import random

data = []

for i in range(100):
    flow = random.randint(2, 10)

    if random.random() < 0.1:
        flow = random.randint(15, 25)

    data.append(flow)

df = pd.DataFrame(data, columns=["Flow Rate"])
df.to_csv("water_data.csv", index=False)

print("Dataset generated: water_data.csv")
