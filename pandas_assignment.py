import pandas as pd

df = pd.read_csv("iris.csv")
#print(df)
#print(df.head(10))
#print(df.dtypes)

#print(df.describe())
#print(df.describe(include=["object"]))

#print(df.groupby("Species")[["Sepal.Length"]].mean())

#print(df.isnull())
#a = df["Petal.Width"].mean()
#print(a)
#print(df.fillna(a))

#print(df.loc[(df.SepalLength > 5.0) & (df.Species=="setosa")])

#print(df.groupby("Species").agg({"SepalLength":["mean","median","std"]}))

#df.groupby("Species").count())

#print(df["Petal.Width"].agg(["max","min"]))

#print(df["Petal.Width"].mean().max())
#print(df.groupby("Species")[[df.loc[df["Petal.Width"] > df["Petal.Width"].agg(["max","min"]) ]]])

#data = df.assign(ratio s= (df.SepalLength/df["Petal.Width"]))
#print(data)

#a=df.groupby("Species")["Petal.Length"].max()
#b=df.groupby("Species")["Petal.Length"].min()
#print("difference",a-b)

#def add_column(row):
#    if row.Species == "setosa":
#        return "Grass Land"
#    if row.Species == "versicolor":
#        return "its a color"
#    if row.Species == "virginica":
#        return "flower"
#df["Typical.Habitat"] = df.apply(add_column,axis=1)
#print(df)


#def add_column(row):
#    if row["Petal.Length"] <= 1.0:
#        return "small"
#    elif row["Petal.Length"] > 1.0 and row["Petal.Length"] <= 2.0:
#        return "medium"
#    else:
#        return "large"
#df["size"] = df.apply(add_column,axis=1)
#print(df)

#df["Typical.Habitat"] =df.Species.map({"setosa": "Grass Land","versicolor":"its a color","virginica":"flower"})
























