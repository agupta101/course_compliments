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

values = list(zip(students,profs,emails))
print(values)

end_of_week_date = "March 11, 2019"
end_of_term_date = "June 14, 2019"

# email_out = ""
for elem in values:
	specific_vals = list(elem)
	stud_email = specific_vals.pop()
	specific_vals.append(end_of_week_date)
	specific_vals.append(end_of_term_date)
	print(specific_vals)
	print(email_content)

	print("Number of values needed: ", email_content.count('{}'))
	print("Number of values acquired: ", len(specific_vals), " - ", specific_vals)

	email_out = email_content.format(*elem)
	print(email_out)


with open("emailOut.txt", "w") as file:
	file.write(email_out)