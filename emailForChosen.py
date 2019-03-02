# Daniel Neamati
# ARC Ruddock Representative
# 27 Feb. 2019

import pandas as pd

with open("email_in.txt", "r") as file:
	email_content = file.read()

dfChosen = pd.read_csv("chosen.csv")
students = list(dfChosen.loc[:,"Student"])
profs =  list(dfChosen.loc[:,"Instructor"])
emails =  list(dfChosen.loc[:,"Student Email"])

print(list(zip(students,profs,emails)))

# email_out = email_content.format(*values)
email_out = ""
print(email_out)


with open("emailOut.txt", "w") as file:
	file.write(email_out)