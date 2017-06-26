__all__ = ['sources_list', 'newsApi_API', 'further_read_newsApi', 'invalid', 'thankyou', 'notready']

#functions

import json
from pprint import pprint
from urllib.request import urlopen

def sources_list():
	print("Possible news sources:\n\
	\t1: NewsApi.org\n\
	\t2: aa\n\
	\t0: Exit\n")
	x = int(input("Enter your choice: "))
	return x

def newsApi_API():
	url = "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=631086356f124f4d82bd059ea5fccc88"
	print()
	json_string = urlopen(url).read()

	#with open('jsondata.txt') as data_file:    
	data = json.loads(json_string)
	names = [d['title'] for d in data['articles']]
	#pprint(names)
	i = 1
	for name in names:
		print("{}: {}".format(i, name))
		i += 1
	print("\n")
	resp1 = "y"
	while (resp1 == "y" or resp1 == "Y"):
		resp1 = input("Would you like to read more of any of these articles? (y/n) ")
		if resp1 == "y" or resp1 == "Y":
			further_read_newsApi(data)
		else:
			print("Exiting newsApi... \n")

def further_read_newsApi(data):
	resp2 = int(input("Which one? "))-1
	s = data['articles'][resp2]
	print("\nTitle: {}\n\
		Author: {}\n\
		Description: {}\n\n\
		To read more, go to {} \n".format(s['title'], s['author'], s['description'], s['url']))

def invalid():
	print()
	print("Invalid option, try again!")
	print("\n")

def thankyou():
	print()
	print("Thank you for using our news app!")
	print("\n")

def notready():
	print()
	print("Not ready yet, check back later!")
	print("\n")