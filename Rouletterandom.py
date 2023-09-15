print("Welkom bij Roulette")
import random

def generate_random_number(min_value, max_value):
	return random.randint(min_value, max_value)
min_value = 0
max_value = 36
random_number = generate_random_number(min_value, max_value)
def get_color(nummer):
	if nummer == 0:
		return "groen"
	elif (nummer >= 1 and nummer <= 10) or (nummer >= 19 and nummer <= 28):
		if nummer % 2 == 1:
			return "zwart"
		else:
			return "rood"
	elif (nummer >= 11 and nummer <= 18) or (nummer >= 29 and nummer <= 36):
		if nummer % 2 == 1:
			return "zwart"
		else:
			return "rood"

def main():
	try:
		if 0 <= random_number <= 36:
			color = get_color(random_number)
			print(f"De kleur van het nummer {random_number} is {color}.")
		else:
			print("Ongeldige invoer. Voer een getal tussen 0 en 36 in.")
	except ValueError:
		print("Ongeldige invoer")
			
if __name__ == "__main__":
    main()
