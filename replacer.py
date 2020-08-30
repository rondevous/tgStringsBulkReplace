# EDIT THIS (case-sensitive)
replace_dictionary = {
	"groups":"baskets",
	"members":"onions",
	"Forever":"STFU",
}
# Remember that lowercase is not UPPERCASE 
# Please check possibilities.log after running the script

# DO NOT EDIT THE CODE BELOW (unless you know Python and RegEx)

keylist = list(replace_dictionary)
# Imports
import xml.etree.ElementTree as ET
import re
import argparse

# Command-line info and argument parsing
arg_parser = argparse.ArgumentParser(
	description='Makes bulk-replacements to your Telegram language file. The find-replace pairs should be edited in replacer.py')
arg_parser.add_argument(
	'--file', metavar='Langfile[.xml|.strings]', type=str, required=True,
	help='Your language file (.xml or .strings) export from the translations platform')
# arg_parser.add_argument(
# 	'-l','--list', metavar='Replace_list.txt', type=str, required=True,
#	help='File containing list of replacements to be make')
arg_parser.add_argument(
	'-p', action="store_true",
	help='Display the replaced translations.')

args = arg_parser.parse_args()
lang_file = str(args.file)  # str('android_lang_v1234567.xml')
print("\n\nUsing File:\n\t"+lang_file)

# log possibilites
possibilites = open("possibilites.log","w")

# Initialise Variables
global tree, total_cased, total_uncased, skipped
total_cased = 0
total_uncased = 0
skipped = list()
match_text = 'dummy'
replace_text = 'XXdummyXX'

# Checks if lang_file is in XML format
def isXML():
	# return (re.search(r'.*\.xml$', lang_file, re.UNICODE) is not None)
	try:
		global tree
		tree = ET.parse(lang_file)
	except:
		return False
	else:
		return True

# Checks if lang_file is in .strings format
def isStrings ():
	global dot_strings
	try:
		dot_strings = open(lang_file, 'r').read()
	except FileNotFoundError:
		print("\nError:\n\tThe file \'"+lang_file+"' does not exist.\n")
		exit()
	result = (len(re.findall(r'".*"\s=\s".*";', dot_strings)) > 0)
	return result

# Prints summary
def printSummary():
	print('\nSkipped:')
	for i in range(0, len(skipped)):
		print('\t<'+skipped[i]+'>')
	#
	print('\nSummary:')
	print('\t'+str(len(skipped)),'skipped/overlooked')
	print('\t'+str(total_cased),'replaced in',(rplStrCount),'strings.')
	if total_uncased != 0:
		print('\t'+str(total_uncased)+' possible replacements ignored.')
		print("(See 'possibilites.log' and add them to the dictionary)")
	print("\nImport this:\n\t"+edited_file_name)
	print("\nPlease double check when importing.\n")
	#

# Algo for XML replacer
if(isXML()):
	global tree
	# tree = ET.parse(lang_file)
	root = tree.getroot()	# <Element 'resources'>
	#
	if(args.p):
		print('\n\nThese strings have been edited:\n')
	#
	strCount = 1
	rplStrCount = 0
	for string in root.findall('string'):
		string_name = string.get('name')
		if(string_name == 'language_code' or string_name == 'LanguageCode'): # skip
			strCount += 1
			skipped.append(string_name)
			continue
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
			uncased_translation = re.subn(r'(?<!\w)'+match_text.casefold()+r'(?!\w)', 'DUMMY', translation[0], flags =re.U+re.I) # Use re.DOTALL & re.MULTILINE? #  flags = re.U|S|I|M
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
			strCount += 1
			root.remove(string)
			continue
		if(args.p):
			# print('\n'+str(strCount)+'. '+string_name+'')
			print(str(strCount)+".", translation[0])
		string.text = translation[0]
		rplStrCount += 1
		strCount += 1
	#end replacing strings
	possibilites.close()
	#
	edited_file_name = str(re.sub(r'(android_x|android)_(.*)[_.].*xml', r'\1_\2_[EDITED].xml', lang_file))
	tree.write(edited_file_name, xml_declaration=True, encoding='Unicode')
	#
	printSummary()
	del root, tree, ET # xml memory cleanup
	#
# Algo for .strings replacer
elif(isStrings()):
	global dot_strings
	# open file, copy all data, iterate and write out to a new file
	dot_strings = open(lang_file, 'r').read()
	edited_file_name = re.sub(r'(tdesktop|macos|ios)_(.*)[_.].*strings', r'\1_\2_[EDITED].strings', lang_file)
	new_strings = open(edited_file_name, 'w', encoding='UTF-8')
	#
	if(args.p):
		print('\n\nThese strings have been edited:\n')
	#
	strCount = 0
	rplStrCount = 0
	for match in re.finditer(r'(?<!.)"(.*)"\s=\s"(.*)";\n', dot_strings):
		strName = match.groups()[0]
		strValue = match.groups()[1]
		translation = strValue
		exact_subn = 0
		uncased_subn = 0
		for key in keylist:
			if key is keylist[0]:
				translation = (translation,0)
			match_text = str(key)
			replace_text = str(replace_dictionary[key])
			# To learn about the regex used below, type in the Python Console: 	help('re')
			translation = re.subn(r'(?<!\w)'+match_text+r'(?!\w)', replace_text, translation[0], re.UNICODE)
			uncased_translation = re.subn(r'(?<!\w)'+match_text.casefold()+r'(?!\w)', 'DUMMY', translation[0], flags =re.U+re.I) # Use re.DOTALL & re.MULTILINE? #  flags = re.U|S|I|M
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
			dot_strings = re.sub(match, '', dot_strings, re.U+re.M)
			strCount += 1
			continue
		if(args.p):
			# print('\n'+str(strCount)+'. '+string_name+'')
			print(str(strCount)+".", translation[0])
		match.groups()[1] = strValue = translation[0]
		#
		new_strings.write("\""+strName+"\" = \""+strValue+"\";\n")
		rplStrCount += 1
		if(args.p):
			print('\n'+str(strCount)+'. '+strValue+'')
		strCount += 1
	new_strings.close()
	#
	printSummary()
	# CLEANUP MEMORY
	re.purge()
	del dot_strings, strCount, new_strings, isStrings
	#
else: # if not either types of file
	print("\nERROR: '"+lang_file+"' is neither an XML nor a proper .strings file.")
	print("\nPlease export a translation file from your language")
	print('How to export --> https://t.me/TranslationsTalk/1759)\n') #FIXME


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