import random, re


def get_input(inp=""):
	if inp == "quit":
		return inp
	inp = input("Choose square and/or get next: ")
	if len(inp) == 0:
		return "next"
	x = re.search(r"[a-g][1-7]", inp)
	if x != None:
		return inp
	else:
		print("invalid square chosen, use format a1")
		return get_input()


def pirates():
	cols = ["a", "b", "c", "d", "e", "f", "g"]
	rows = [r for r in range(1, 8)]
	used = []

	while len(used) < 49:  #only 49 grid squares available
		l = random.randint(0, 6)  #choose a letter position
		n = random.randint(0, 6)  #choose a number position
		pos = cols[l] + str(rows[n])  #create grid ref
		if (pos not in used):
			#check we haven't already been there
			print(pos)
			used.append(pos)  #add it to the list of places we've been

			# while user input isn't useful keep trying.
