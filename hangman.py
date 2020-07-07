#Martin Ivanov
#May 8, 2018
#Allow the user to play a game of hangman.
import random
from time import sleep

art = [
    ' _________     \n|         |    \n|         0    \n|        /|\  \n|        / \  \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|        /|\  \n|        /    \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|        /|\  \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|        /|   \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|         |   \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|             \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|              \n|             \n|             \n|              \n|              \n',
]

colors = ['31m', '32m', '33m', '34m', '35m', '36m', '37m']

artColored = [
    ' _________     \n|         |    \n|         0    \n|        /|\  \n|        / \  \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|        /|\  \n|        /    \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|        /|\  \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|        /|   \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|         |   \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|         0    \n|             \n|             \n|              \n|              \n',
    ' _________     \n|         |    \n|              \n|             \n|             \n|              \n|              \n',
]

animals = [
    'stallion', 'cheetah', 'beaver', 'giraffe', 'gazelle', 'goat', 'wasp',
    'bull', 'mongoose', 'groundhog', 'camel', 'orangutan', 'llama', 'jackal',
    'chimpanzee', 'crow', 'monkey', 'lynx', 'walrus', 'snake', 'panther'
]

teams = [
    'celtics', 'trailblazers', 'magic', 'hornets', 'mavericks', 'spurs',
    'nets', 'hawks', 'thunder', 'grizzlies', 'wizards', 'clippers', 'bulls',
    'raptors', 'heat', 'pelicans', 'warriors', 'jazz', 'rockets', 'nuggets'
]

cities = [
    'bangalore', 'santiago', 'ottawa', 'rome', 'mumbai', 'casablanca',
    'manila', 'moscow', 'dubai', 'busan', 'berlin', 'london', 'cairo',
    'toronto', 'alexandria', 'beijing', 'tokyo', 'yokohama', 'paris', 'nairobi'
]

food = [
    'butter', 'mushrooms', 'duck', 'cherries', 'broth', 'grouper', 'mushrooms',
    'avocados', 'parsley', 'melons', 'nectarines', 'sardines', 'beets',
    'grapefruits', 'olives', 'sauerkraut', 'catfish', 'marmalade',
    'cauliflower', 'chives'
]

movies = [
    'gladiator', 'titanic', 'dunkirk', 'goodfellas', 'rocky', 'terminator',
    'inception', 'braveheart', 'scarface', 'shrek', 'transformers',
    'ratatouille', 'scream', 'zootopia', 'predator', 'zombieland', 'halloween',
    'memento', 'beetlejuice'
]

music = [
    'prince', 'elvis', 'kanye', 'madonna', 'adele', 'eminem', 'shakira',
    'beyonce', 'rihanna', 'tupac', 'kendrick', 'drake', 'usher', 'ludacris',
    'sting', 'bono', 'biggie', 'chance', 'gambino', 'bowie', 'hendrix',
    'sinatra'
]

categories = [animals, food, cities, teams, movies, music]

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

wins = 0
losses = 0

print("Welcome to Python Hangman!" + "\n")
sleep(1)
mode = input("N. Normal\nH. Hard \n\nSelect a difficulty:").upper()
if mode == "N":
	guessesTotal = 6
elif mode == "H":
	guessesTotal = 3
else:
	guessesTotal = 6
sleep(1)

def play():
	global artColored
	global wins
	global losses
	colorRnd = random.choice(colors)
	for i in range(7):
		artColored[i] = str("\033[" + colorRnd + art[i] + "\033[0m")
	categoryRnd = random.choice(categories)
	lettersGuessed = []
	print(
	    "\nA. Movies \nB. Music \nC. World Cities \nD. Food \nE. NBA Teams \nF. Animals\nOther. Random\n"
	)
	category = input("Please choose a category\033[5m:\033[0m").upper()
	if category == "A":
		word = random.choice(movies)
	elif category == "B":
		word = random.choice(music)
	elif category == "C":
		word = random.choice(cities)
	elif category == "D":
		word = random.choice(food)
	elif category == "E":
		word = random.choice(teams)
	elif category == "F":
		word = random.choice(animals)
	else:
		word = random.choice(categoryRnd)
	guessesLeft = guessesTotal
	letters = ["_" for i in range(len(word))]
	sleep(1)
	while "_" in letters:
		if guessesTotal == 6:
			print(artColored[guessesLeft])
		elif guessesTotal == 3:
			print(artColored[guessesLeft * 2])
		sleep(0.5)
		print("\n", letters, "\n")
		sleep(0.5)
		guess = input("Guess a letter\033[5m:\033[0m").lower()
		if guess in alphabet:
			if guess in lettersGuessed:
				print("You've already guessed '" + guess + "'.")
			else:
				lettersGuessed.append(guess)
				if guess in word:
					i = 0
					for char in word:
						if char == guess:
							letters[i] = guess
						i += 1
				else:
					guessesLeft -= 1
					print("'" + guess + "' is not in the word.")
					if guessesLeft > 0:
						print("You only have", guessesLeft, "guess(es) left.")
		else:
			print("Your guess is invalid.")
		if guessesLeft == 0:
			sleep(1.5)
			print("\n" + artColored[guessesLeft])
			print("You ran out of guesses!")
			losses += 1
			sleep(0.5)
			print("The word was", word + ".")
			sleep(0.5)
			print('Total wins:', wins)
			print('Total losses:', losses)
			sleep(0.5)
			done = input("Do you want to play again?\033[5m(Y/N)\033[0m")
			if done.upper() == "Y":
				print(
				    '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
				)
				play()
			elif done.upper() == "N":
				exit(0)
			else:
				exit(0)
	sleep(1.5)
	if guessesTotal == 6:
			print(artColored[guessesLeft])
	elif guessesTotal == 3:
			print(artColored[guessesLeft * 2])
	sleep(0.5)
	print("\n", letters, "\n")
	print("Congratulations! You won!")
	wins += 1
	sleep(0.5)
	print("You used", guessesTotal - guessesLeft, "out of", guessesTotal,
	      "guesses.")
	sleep(0.5)
	print("Total wins:", wins)
	print("Total losses:", losses)
	sleep(0.5)
	done = input("Do you want to play again?\033[5m(Y/N)\033[0m")
	if done.upper() == "Y":
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
		    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		play()
	elif done.upper() == "N":
		exit(0)
	else:
		exit(0)


play()
