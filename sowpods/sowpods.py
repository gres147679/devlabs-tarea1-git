#!/usr/bin/python
# -*- coding: utf-8 -*-
"""First homework for DevLabs"""
import argparse
from string import ascii_uppercase

"""
	SOWPODS
	Given a file which contains a dictionary of words, this program constructs 
	a list of letters, which contains the letters NOT repeated twice or more 
	in any word of the dictionary. The documentation can be generated with

	pydoc sowpods

	Aditionally, HTML documentation can be generated with

	pydoc -w sowpods
"""
__author__ = "Gustavo El Khoury <gustavoelkhoury@gmail.com>"

__version__ = '1.0'

def generateListOfEnglishCharacters():
	"""Generates the list of English Characters, and returns it as a set"""
	return ascii_uppercase

def generateDuplicatedChars(charSet):
	"""Given a charSet, it returns a list of strings of the form CC for
	each C in charSet"""
	mylist = []
	for i in charSet:
		tempString = ""+i+i
		mylist.insert(0,tempString)
	return mylist

def checkForSubstrings(word,checkList):
	"""Given a word, it checks if it contains any string in checkList.
	If it finds it, it removes it from checkList"""
	index = 0
	listSize = len(checkList)
	while index<listSize:
		if checkList[index] in word:
			checkList.pop(index)
			listSize = len(checkList)
		index = index + 1

def analyzeDictionary(inputFile,charSet):
	""" Given an inputFile, it proccesses every line, and obtains a
	set of non-repeated letters, based on a charSet"""
	myList = generateDuplicatedChars(charSet)

	for word in inputFile:
		checkForSubstrings(word,myList)
	for i in myList:
		print i[0]

def main():
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument('-f','--file=',default='sowpods.txt',
    	type=argparse.FileType("r"),help='the file to be read',dest='file')
    arguments = argumentParser.parse_args()

    # # Process the file, with a given charset
    charSet = generateListOfEnglishCharacters()
    setOfNonRepeatedLetters = analyzeDictionary(arguments.file,charSet)

if __name__ == "__main__":
    main()