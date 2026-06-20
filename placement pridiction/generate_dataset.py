import pandas as pd
import random

data = []

for i in range(100000):

    cgpa = round(random.uniform(4.0, 10.0), 2)

    aptitude = random.randint(0, 3)
    communication = random.randint(0, 3)
    internship = random.randint(0, 1)
    training = random.randint(0, 1)
    coding = random.randint(0, 3)
    projects = random.randint(0, 3)

    # REALISTIC placement logic (important 🔥)
    score = (
        cgpa * 2 +
        aptitude * 1.5 +
        communication * 1.2 +
        coding * 1.5 +
        projects * 1.3 +
        internship * 1.5 +
        training * 1.0
    )

    # threshold based placement (real-world style)
    if score > 18:
        placed = 1
    else:
        placed = 0

    data.append([
        cgpa,
        aptitude,
        communication,
        internship,
        training,
        coding,
        projects,
        placed
    ])

df = pd.DataFrame(data, columns=[
    "cgpa",
    "aptitude",
    "communication",
    "internship",
    "training",
    "coding",
    "projects",
    "placed"
])

df.to_csv("dataset.csv", index=False)

print("✅ 100000 dataset.csv created successfully!")