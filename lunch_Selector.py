import pandas as pd 
import numpy as np
import random
import sys

# Read in the datafram
df = pd.read_csv("full_compliments_list.csv", encoding = "ISO-8859-1")

# Student List stores the names of the students and by the data structure,
# also the row of the entry
studentList =  df.loc[:,"Your FIRST Name (Optional)"]

# Out list stores the names of the students that have been picked to avoid
# rewarding the same student in a given cycle
studentOut = []
studentOutEmail = []
profTitle = []
profOut = []
chosenList = []

print(df.head())
print(set(studentList))

# We allow the user to select the number they want to pick
if len(sys.argv) > 1:
	numSelect = int(sys.argv[1])
else:
	numSelect = 3
	print(" ################# ")
	print(" The number of students is {}".format(numSelect))
	print(" This can be changed via a command line argument.")
	print(" ################# ")

# Now we select the students.
while numSelect > 0:
	# Choose any value
	choosenOne = random.choice(list(enumerate(studentList)))

	# We first want to make sure the the student's name is list (i.e. not nan)
	# We also want to ensure that the student is not already in this cycle
	if type(choosenOne[1]) != float and studentOut.count(choosenOne[1]) == 0:
		print()
		print(df.loc[choosenOne[0], :])
		print()
		print(df.loc[choosenOne[0], "Write your compliment here!"])
		print("By: ", df.loc[choosenOne[0], "Your FIRST Name (Optional)"])

		# Allow the user to check the content of the comment
		check = input("Is this a good comment? [y/n]")

		if check.lower() == 'y':
			print("Student added")
			# Add the student to the picked list.
			chosenReceiver = df.loc[choosenOne[0], "Who's the lucky person?"]
			title = df.loc[choosenOne[0], "Professor, TA, or Deans' Tutor?"]
			email = df.loc[choosenOne[0], "Email (Optional)"]

			studentOut.append(choosenOne[1])
			studentOutEmail.append(email)
			profOut.append(title + ' ' + chosenReceiver)
			chosenList.append(df.loc[choosenOne[0], :])

			numSelect -= 1


			# Now we need to check if other students also complimented this
			# person.
			
			for index, receiver in \
						enumerate(df.loc[:,"Who's the lucky person?"]):

				newChosen = df.loc[index, "Your FIRST Name (Optional)"]
				if receiver == chosenReceiver and newChosen != choosenOne[1]:
					# Potentially add this student

					print()
					print("Another eligible student found!")
					print(df.loc[index, "Write your compliment here!"])
					print("By: ", df.loc[index, "Your FIRST Name (Optional)"])

					# Allow the user to check the content of the comment
					check = input("Is this a good comment? [y/n]")

					if check.lower() == 'y':
						print("Student added")
						# Add the student to the picked list.
						studentOut.append(newChosen)
						profOut.append(chosenReceiver)
						chosenList.append(df.loc[index, :])

						numSelect -= 1


		else:
			print("Student not added")

print(studentOut)
print(profOut)

outList = list(zip(studentOut, studentOutEmail, profOut))
print(outList)

df = pd.DataFrame(outList, columns=["Student", "Student Email", "Instructor"]) 
df.to_csv('chosen.csv', index=False)




	