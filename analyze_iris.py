import panda as pd

iris = pd.read_csv("data/iris.scv")
print(iris.columns)
print(iris.sample(10).sort_index())
