# Imports
import xml.etree.ElementTree as ET
import re
import argparse

# **************************
# List of parsers to pick for parsing the replacement list:
""" https://tomassetti.me/parsing-in-python/ """

# Some topics to think about:
"""
Lexer and Parser (using ply?)
re
enumerate
"""
# Some info so I don't get confused:
"""
Python List/Array = [kk,nnn,hhh]
Python Dictionary = {
	"groups":"potatoes"
	"members":"chips"
}
"""
# **************************


# Command-line info and argument parsing
#
arg_parser = argparse.ArgumentParser(
	description='Make a bulk rename to your languagePack.xml file')
arg_parser.add_argument(
	'--lang', '-l', metavar='LANG.XML', type=str, required=True,
	help='The exported language file (.xml) from the translations.telegram.org platform')
# arg_parser.add_argument(
# 	'--list', metavar='LIST.TXT', type=str, required=True,
#	help='File containing list of replacements to be make')
arg_parser.add_argument(
	'-p','--preview', action="store_true",
	help='Show a preview of the results, but do not modify the language file.')

args = arg_parser.parse_args()
print("Using file:",args.lang)


# Sample
match_text = str('Admin')
replace_text = str('Alpha')
lang_file = str(args.lang)  # e.g: str('android_emoji_v923880.xml')


# Initiate Information Variables
global tree, total_cased, total_uncased
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

	if(args.preview):
		print('\n\nThese replacements will be made:')
	
	i=1
	for string in root.findall('string'):
		string_name = string.get('name')
		translation = string.text
		# To learn about the regex used below, type in the Python Console: 	help('re')
		# Look for 'Special characters' and 'Functions' in the `re` module
		# 
		exact_replace = re.subn(r'(?<!\w)'+match_text+r'(?!\w)', replace_text, translation, re.UNICODE)
		uncased_match = re.subn(r'(?<!\w)'+match_text.casefold()+r'(?!\w)', r'XXX', translation.casefold(), re.UNICODE)[1] - exact_replace[1]
		
		# Useful info
		total_cased += exact_replace[1]
		total_uncased += uncased_match

		if(exact_replace[1] == 0):
			continue
		if(args.preview):
			print('\n'+str(i)+'.',string_name)
			print(exact_replace[0])
		else:
			string.text = exact_replace[0]
		i+=1
	
	print('\nMade a total of',total_cased,'replacements in',(i-1),'strings.')
	print('Found and ignored '+str(total_uncased)+' possible replacements (uncased).')
	
	if(args.preview):
		print('\n[WARNING]: REPLACEMENTS ARE NOT WRITTEN TO THE FILE')
	else:
		newfile = str(re.sub(r'(.*)\.xml', r'\1_[EDITED].xml', lang_file))
		tree.write(newfile, xml_declaration=True, encoding='Unicode')
		print("\nHere's your file:\n\t",newfile)
		print("\nImport it on the Translations Platform. Please review before importing all.")
	
	del root, tree, ET # free some memory
else:
	print('\t',lang_file,' is not an XML file.')
	print("Please use an XML file which is exported from translations.telegram.org")
	print('(How to export: t.me/group/message)') #FIXME
