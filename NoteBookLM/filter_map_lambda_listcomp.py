class EasyDifficulty:

	def filter_vowels(string):

		vowels = "aeiouAEIOU"
		return list(filter(lambda x: x in vowels, string))

	string = "hello world divine is a stupid dickhead"
	print(filter_vowels(string))
	print()



	def cubes():

		return list(map(lambda x: (x, x **3), range(1,5)))

	print(cubes())
	print()



	def multiplesof3():

		return list(filter(lambda x: x % 3 == 0, range(3, 31)))

	print(multiplesof3())
	print()



class MediumDifficulty:

	def sum_thru_2_lists(list1, list2):

		return list(map(lambda x: sum(x), zip(list1, list2)))

	list1 = [1,2,3,4,5,6,7,8,9]
	list2 = [9,8,7,6,5,4,3,2,1]

	print(sum_thru_2_lists(list1, list2))
	print()



class AdvancedDifficulty:

	def unique_and_sorted(example):

		return list(set(example))


	example_list = [65,9,3,3,-2,88,55,5,4,6,63,55,0,9,"hello","nice","hello","nice","birthday","bless","yellow","nice"]
	print(unique_and_sorted(example_list))



	def filter_primes(integer):

		return [
			value
			for value in range(2, integer)
			if all(value % divider !=0 for divider in range(2, value)) and value >= 2
			]
			

	print(filter_primes(1000))


	

	