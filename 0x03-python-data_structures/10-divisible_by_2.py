#!/usr/bin/python3
def divisible_by_2(my_list=[]):
	"""This to check the dvisible of 2 in list """
	multiple_of_2 =[]
	for num in range(len(my_list)):
		if my_list[num] % 2 == 0:
			multiple_of_2.append(True)
		else:
			multiple_of_2.append(False)

	return (multiple_of_2)

