import random, re


def get_input(been_here):
	
	inp = input("Choose square and/or enter to get next: ").lower()
	if inp == "quit":
		return inp
	if len(inp) == 0:
		return "next"
	x = re.match(r"^[a-g][1-7]$", inp)
	if x != None and inp not in been_here :
		return inp
	else:
		print("invalid square chosen, use format a1, with columns a-g and rows 1-7")
		return get_input(been_here)


def pirates():
	cols = ["a", "b", "c", "d", "e", "f", "g"]
	rows = [r for r in range(1, 8)]
	used = []
	pos = "next"
	while len(used) < 49:  #only 49 grid squares available
		if pos == "next":
			l = random.randint(0, 6)  #choose a letter position
			n = random.randint(0, 6)  #choose a number position
			pos = cols[l] + str(rows[n])  #create grid ref
		if (pos not in used):
			#check we haven't already been there
			print(pos)
			used.append(pos)  #add it to the list of places we've been

			# while user input isn't useful keep trying.
			pos = get_input(used)
			if pos == "quit":
				while true:
					kp = input("Exiting game, are you sure? [Y/N]")
					if kp == "Y":
						exit
					elif kp == "N":
						break
					else:
						continue
				

if __name__ == '__main__':
	pirates()
	
