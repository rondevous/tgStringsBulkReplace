# Replacing inside .strings file is currently not supported
replace_dictionary = {
	"groups":"potatoes",
	"members":"chips",
	"Restart bot":"Restart life",
}

# IMPORTANT!!! Do not change the code below

keylist = list(replace_dictionary)
# Imports
import xml.etree.ElementTree as ET
import re
import argparse

# Command-line info and argument parsing
arg_parser = argparse.ArgumentParser(
	description='Make a bulk rename to your languagePack.xml file')
arg_parser.add_argument(
	'--file', '-f', metavar='LANGFILE.XML', type=str, required=True,
	help='The exported language file (.xml) from the translations.telegram.org platform')
# arg_parser.add_argument(
# 	'-l','--list', metavar='Replace_list.txt', type=str, required=True,
#	help='File containing list of replacements to be make')
arg_parser.add_argument(
	'-p','--preview', action="store_true",
	help='Show a preview of the results, but do not modify the language file.')

args = arg_parser.parse_args()
lang_file = str(args.file)  # str('android_lang_v1234567.xml')
print("\nEditing file: '"+lang_file+"'")

# log possibilites
possibilites = open("possibilites.log","w")

# Sample
match_text = str('Admin')
replace_text = str('Alpha')

global tree, total_cased, total_uncased
# Initialise Variables
total_cased = 0
total_uncased = 0

#
# Checks if lang_file is in XML format
#
def isXML():
	# return (re.search(r'.*\.xml$', lang_file, re.UNICODE) is not None)
	try:
		global tree
		tree = ET.parse(lang_file)
	except:
		return False
	else:
		return True

#
# Algo for XML file
#
if(isXML()):
	global tree
	# tree = ET.parse(lang_file)
	root = tree.getroot()	# <Element 'resources'>
	#
	if(args.preview):
		print('\n\nThese strings have been edited:\n')
	#
	strCount=1
	for string in root.findall('string'):
		string_name = string.get('name')
		translation = str(string.text)
		exact_subn = 0
		uncased_subn = 0
		for key in keylist:
			if key is keylist[0]:
				translation = (translation,0)
			match_text = str(key)
			replace_text = str(replace_dictionary[key])
			# To learn about the regex used below, type in the Python Console: 	help('re')
			translation = re.subn(r'(?<!\w)'+match_text+r'(?!\w)', replace_text, translation[0], re.UNICODE)
			uncased_translation = re.subn(r'(?<!\w)'+match_text.casefold()+r'(?!\w)', 'DUMMY', translation[0], re.UNICODE, re.IGNORECASE)
			uncased_subn += uncased_translation[1]
			exact_subn += translation[1]
		#end looping replacements
		#
		# Useful info
		total_cased += exact_subn
		if(uncased_subn - exact_subn > 0):
			total_uncased += uncased_subn - exact_subn
			possibilites.write(str(translation[0])+'\n') # Log
		#
		if(exact_subn == 0):
			root.remove(string)
			continue
		if(args.preview):
			# print('\n'+str(strCount)+'. {'+string_name+'}')
			print(translation[0])
		string.text = translation[0]
		strCount+=1
	#end looping strings
	possibilites.close()
	#
	newfile = str(re.sub(r'(.*)\.xml', r'[EDITED]_\1.xml', lang_file))
	tree.write(newfile, xml_declaration=True, encoding='Unicode')
	#
	print('\nMade a total of',total_cased,'replacements in',(strCount-1),'strings.')
	print("Here's the new file:\n\t'"+newfile+"'")
	print("\nPlease check before importing it on the Translations Platform.")
	#
	if total_uncased != 0:
		print('\nIgnored '+str(total_uncased)+' possible replacements (uncased).')
		print('Check \'possibilites.log\', add them to the dictionary and re-run the script.')
	#
	del root, tree, ET # free some memory (XML)
else:
	print("\nERROR: '"+lang_file+"' is not an XML file.")
	print("\nPlease use an XML file which is exported from translations.telegram.org")
	print('How to export --> https://t.me/TranslationsTalk/1759)') #FIXME


# ************* SOME THOUGHTS *************
# List of parsers to pick for parsing the replacement list:
""" https://tomassetti.me/parsing-in-python/ """

# Some topics to think about:
"""
Lexer and Parser (using ply?)
re
enumerate
"""
# **************************