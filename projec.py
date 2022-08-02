import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/c-129-project/main/Processed_data/star_with_gravity.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].tolist()
distance = df["Distance"].tolist()
gravity = df["Gravity"].tolist()
mass.sort()
radius.sort()
distance.sort()
gravity.sort()

plt.plot(radius,mass)
plt.title("radius and mass of star")
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()

plt.plot(mass,gravity)
plt.title("gravity and mass of star")
plt.xlabel("mass")
plt.ylabel("gravity")
plt.show()

plt.scatter(mass,radius)
plt.title("radius and mass of star")
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()