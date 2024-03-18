def provideAccess(user):
	return {
		"username": user,
		"password": "admin"
	}


def runMatch():
	user = str(input("Write your username -: "))

	# match statement starts here .
	match user:
		case "Om":
			print("Om does not have access to the database \
			only for the api code.")
		case "Vishal":
			print(
				"Vishal does not have access to the database , \
				only for the frontend code.")

		case "Rishabh":
			print("Rishabh has the access to the database")
			print(provideAccess("Rishabh"))

		case _:
			print("You do not have any access to the code")


if __name__ == "__main__":
	for _ in range(3):
		runMatch()
