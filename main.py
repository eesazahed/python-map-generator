from random import randint

colors = {
		1: "🟦",
		2: "🟩",
		3: "⬛️",
		4: "🟥",
}

def print_map(map):
		print("\n")
		for line in map:
				print("".join(colors[char] for char in line))
		print("\n")

def generate_map(size):
		scale_factor = 3
		diameter = size * scale_factor
		bordered_diameter = diameter + 2

		random_x = randint(1, diameter - 2)
		random_y = randint(1, diameter - 2)

		def generate_block(line, char):
				if line == 0 or line == bordered_diameter - 1 or char == 0 or char == bordered_diameter - 1:
						return 3 
				if line - 1 == random_y and char - 1 == random_x:
						return 4
				if ((line - 1 < size and char - 1 + (line - 1) >= size and char - 1 < size * 2 + (line - 1)) or 
						(size <= line - 1 < size * 2) or 
						(line - 1 >= size * 2 and line - 1 - (char - 1) + 1 <= size * 2 and char - 1 < size * 2 + diameter - (line - 1) - 1)):
						return randint(1, 2)
				return 3 

		new_map = [
				[generate_block(line, char) for char in range(bordered_diameter)]
				for line in range(bordered_diameter)
		]

		return new_map

print_map(generate_map(int(input("Select size for a map: "))))
