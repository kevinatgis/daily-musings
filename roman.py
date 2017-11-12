'''Decodes and encodes integers from 1-4999 in Roman numerals'''

# import sys
# if sys.version_info[0] < 3:
#	print('This requires Python 3.')
#	quit()


roman_numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
roman_numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]


def roman_numeral_encode(number):
	'''Encodes int to roman numeral (str)

	Keyword arguments:
	numeral -- int has to be between 0-4999

	Returns: str

	'''
	try:
		if number > 4999 or number < 1:
			raise ValueError('Accepts only values from 1-4999.')
		elif number == 0:
			return 'nulla' #romans didn't have a 0 numeral, rather the word nulla/null

		output = ''
		roman_encode = dict(zip(roman_numbers,roman_numerals))

		for x in roman_numbers:
			if number >= x:
				multiple = number//x #int division (no remainder)
				output+=roman_encode[x]*multiple #outputs numeral X-times
				number%=x #modulo->remainder

		return(output)

	except TypeError as e:
		print('Accepts only integers.')


def roman_numeral_decode(numeral):
	'''Decodes numeral to int

	Keyword arguments:
	numeral -- str

	Returns: int

	'''
	try:
		roman_decode = dict(zip(roman_numerals,roman_numbers))

		output = 0 #returned output
		start_pos = 0

		for letters in roman_numerals:	
			while(numeral[start_pos:start_pos+len(letters)]) == letters: # iterates through letters in numeral based on length
				output += roman_decode[letters] # adds to output
				start_pos += len(letters) # changes next starting position after iterating

		return(output)
	except TypeError:
		print('Accepts only strings.')

