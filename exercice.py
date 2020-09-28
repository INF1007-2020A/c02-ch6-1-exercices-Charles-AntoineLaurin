#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	#max = []
	#for sous_liste in numbers:
	#	max.append(max(sous_liste))
	#return max
	return [max(elem) for elem in numbers]


def join_integers(numbers):
	return (int("".join(numbers)))

def generate_prime_numbers(limit):
	premiers = []
	nombres = [i for i in range (2, limit+1, 1)]
	while len(nombre) != 0 :
		premier.append(nombres[0])
		nombres = [elem for elem in nombres if elem % nombres[0] != 0 ]
		#nombres_mod = []
		#for  elem in nombres:
		#	if elem % nombres[0] != 0:
		#		nombres_mod.append(elem)
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	lettre_combine = []

	
	for i in range(1, num_combinations +1):
		#lettre_combine = [lettre.join(str(i)) for string in strings if excluded_multiples is None or i % excluded_multiples != 0]
			for lettre in strings:
				if excluded_multiples is None or i % excluded_multiples != 0:
					lettre_combine.append(lettre.join(str(i)))

	#return [string + str(i) for i in range(1, num_combinations+1) if excluded_multiples is None or i % excluded_multiples != 0 for string in strings]

	return lettre_combine

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
