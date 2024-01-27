import pandas as pd

s1 : pd.Series = pd.Series([1,2,3,4], name="student id")
s2 : pd.Series = pd.Series([10,20,30,40], name="score")
s3 : pd.Series = pd.Series(["John","Robert","David","Micheal"], name="student name")


df1 : pd.DataFrame = pd.DataFrame({"student id":s1, "score":s2, "student name":s3})
print(df1)