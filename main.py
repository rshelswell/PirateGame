import random, re
from itertools import product

def get_input(been_here):
	inp = input("Choose square and/or enter to get next: ").lower()
	x = re.match(r"^(quit|[a-g][1-7])$", inp)
	if x != None and inp not in been_here :
		return inp
	elif len(inp) == 0:
		return "next"
	else:
		print("invalid square chosen, use format a1, with columns a-g and rows 1-7")
		return get_input(been_here)

def finished(end_type="complete"):
	return "Game "+end_type+", you have used these squares in order:"

def pirates():
	cols = ["a", "b", "c", "d", "e", "f", "g"]
	rows = [str(r) for r in range(1, 8)]
	avail = [i + j for i, j in product(cols, rows)] #all available squares : a1 to g7
	used = []  # squares that have been selected
	pos = "next"
	turn = 1
	while len(avail) > 0:  #only use the available grid squares
		if pos == "next":
			pos = avail.pop(random.randint(0,len(avail)-1))
			print("Turn:",turn,pos, flush=True)
		turn += 1
		used.append(pos)  #add it to the list of places we've been
		# while user input isn't useful keep trying.
		if len(avail) : 
			pos = get_input(used) # only ask for more input if we haven't finished.
		else :
			print(finished(), used)
			return
		if pos == "quit":
			while True:
				kp = input("Exiting game, are you sure? [Y/N]")
				if kp == "Y":
					print(finished("quit"), used)
					return
				elif kp == "N":
					pos = "next"
					break
				else:
					continue
		elif pos != "next":
			avail.remove(pos)

if __name__ == '__main__':
	pirates()
