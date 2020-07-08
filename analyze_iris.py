import panda as pd

iris = pd.read_csv("data/iris.scv")

print(iris.sample(10))
