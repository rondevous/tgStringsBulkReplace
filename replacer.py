# EDIT THIS
replace_dictionary = {
	"groups":"baskets",
	"members":"onions",
	"Forever":"STFU",
}
# Remember: lowercase is not UPPERCASE 

#!TODO: implement a non-exact replace log
#!TODO: create an imperfect log with [\w] only ? 
#!TODO: create an [OFFLINE-USE].xml
#!TODO: Use folders?

# DO NOT EDIT THE CODE BELOW (unless you know Python and RegEx)

keylist = list(replace_dictionary)
# Imports
import xml.etree.ElementTree as ET
import re
import argparse

# Unicode Alphabet ranges

class Unicode_Range:
	### Unicode Scripts
	armenian = r'\u0530-\u058f'
	armenian_ligatures = r'\ufb13-\ufb17'
	carian = r'\u102a0-\u102df'
	caucasian_albanian = r'\u10530-\u1056f'
	cypriot_syllabary = r'\u10800-\u1083f'
	cyrillic = r'\u0400-\u04ff'
	cyrillic_supplement = r'\u0500-\u052f'
	cyrillic_extended_a = r'\u2de0-\u2dff'
	cyrillic_extended_b = r'\ua640-\ua69f'
	cyrillic_extended_c = r'\u1c80-\u1c8f'
	elbasan = r'\u10500-\u1052f'
	georgian = r'\u10a0-\u10ff'
	georgian_extended = r'\u1c90-\u1cbf'
	georgian_supplement = r'\u2d00-\u2d2f'
	glagolitic = r'\u2c00-\u2c5f'
	glagolitic_supplement = r'\u1e000-\u1e02f'
	gothic = r'\u10330-\u1034f'
	greek = r'\u0370-\u03ff'
	greek_extended = r'\u1f00-\u1fff'
	ancient_greek_numbers = r'\u10140-\u1018f'
	latin_1_supplement = r'\u0080-\u00ff'
	latin_extended_a = r'\u0100-\u017f'
	latin_extended_b = r'\u0180-\u024f'
	latin_extended_c = r'\u2c60-\u2c7f'
	latin_extended_d = r'\ua720-\ua7ff'
	latin_extended_e = r'\uab30-\uab6f'
	latin_extended_additional = r'\u1e00-\u1eff'
	latin_ligatures = r'\ufb00-\ufb06'
	fullwidth_latin_letters = r'\uff00-\uff5e'
	ipa_extensions = r'\u0250-\u02af'
	phonetic_extensions = r'\u1d00-\u1d7f'
	phonetic_extensions_supplement = r'\u1d80-\u1dbf'
	linear_a = r'\u10600-\u1077f'
	linear_b_syllabary = r'\u10000-\u1007f'
	linear_b_ideograms = r'\u10080-\u100ff'
	aegean_numbers = r'\u10100-\u1013f'
	lycian = r'\u10280-\u1029f'
	lydian = r'\u10920-\u1093f'
	ogham = r'\u1680-\u169f'
	old_hungarian = r'\u10c80-\u10cff'
	old_italic = r'\u10300-\u1032f'
	old_permic = r'\u10350-\u1037f'
	phaistos_disc = r'\u101d0-\u101ff'
	runic = r'\u16a0-\u16ff'
	shavian = r'\u10450-\u1047f'
	modifier_tone_letters = r'\ua700-\ua71f'
	spacing_modifier_letters = r'\u02b0-\u02ff'
	superscripts_and_subscripts = r'\u2070-\u209f'
	combining_diacritical_marks = r'\u0300-\u036f'
	combining_diacritical_marks_extended = r'\u1ab0-\u1aff'
	combining_diacritical_marks_supplement = r'\u1dc0-\u1dff'
	combining_diacritical_marks_for_symbols = r'\u20d0-\u20ff'
	combining_half_marks = r'\ufe20-\ufe2f'
	adlam = r'\u1e900-\u1e95f'
	bamum = r'\ua6a0-\ua6ff'
	bamum_supplement = r'\u16800-\u16a3f'
	bassa_vah = r'\u16ad0-\u16aff'
	coptic = r'\u2c80-\u2cff'
	coptic_in_greek_block = r'\u03e2-\u03ef'
	coptic_epact_numbers = r'\u102e0-\u102ff'
	egyptian_hieroglyphs = r'\u13000-\u1342f'
	egyptian_hieroglyph_format_controls = r'\u13430-\u1343f'
	ethiopic = r'\u1200-\u137f'
	ethiopic_supplement = r'\u1380-\u139f'
	ethiopic_extended = r'\u2d80-\u2ddf'
	ethiopic_extended_a = r'\uab00-\uab2f'
	medefaidrin = r'\u16e40-\u16e9f'
	mende_kikakui = r'\u1e800-\u1e8df'
	meroitic_cursive = r'\u109a0-\u109ff'
	meroitic_hieroglyphs = r'\u10980-\u1099f'
	n_ko = r'\u07c0-\u07ff'
	osmanya = r'\u10480-\u104af'
	tifinagh = r'\u2d30-\u2d7f'
	vai = r'\ua500-\ua63f'
	anatolian_hieroglyphs = r'\u14400-\u1467f'
	arabic = r'\u0600-\u06ff'
	arabic_supplement = r'\u0750-\u077f'
	arabic_extended_a = r'\u08a0-\u08ff'
	arabic_presentation_forms_a = r'\ufb50-\ufdff'
	arabic_presentation_forms_b = r'\ufe70-\ufeff'
	aramaic_imperial = r'\u10840-\u1085f'
	avestan = r'\u10b00-\u10b3f'
	chorasmian = r'\u10fb0-\u10fdf'
	cuneiform = r'\u12000-\u123ff'
	cuneiform_numbers_and_punctuation = r'\u12400-\u1247f'
	early_dynastic_cuneiform = r'\u12480-\u1254f'
	old_persian = r'\u103a0-\u103df'
	ugaritic = r'\u10380-\u1039f'
	elymaic = r'\u10fe0-\u10fff'
	hatran = r'\u108e0-\u108ff'
	hebrew = r'\u0590-\u05ff'
	hebrew_presentation_forms = r'\ufb1d-\ufb4f'
	mandaic = r'\u0840-\u085f'
	nabataean = r'\u10880-\u108af'
	old_north_arabian = r'\u10a80-\u10a9f'
	old_south_arabian = r'\u10a60-\u10a7f'
	pahlavi_inscriptional = r'\u10b60-\u10b7f'
	pahlavi_psalter = r'\u10b80-\u10baf'
	palmyrene = r'\u10860-\u1087f'
	parthian_inscriptional = r'\u10b40-\u10b5f'
	phoenician = r'\u10900-\u1091f'
	samaritan = r'\u0800-\u083f'
	syriac = r'\u0700-\u074f'
	syriac_supplement = r'\u0860-\u086f'
	yezidi = r'\u10e80-\u10ebf'
	manichaean = r'\u10ac0-\u10aff'
	marchen = r'\u11c70-\u11cbf'
	mongolian = r'\u1800-\u18af'
	mongolian_supplement = r'\u11660-\u1167f'
	old_sogdian = r'\u10f00-\u10f2f'
	old_turkic = r'\u10c00-\u10c4f'
	phags_pa = r'\ua840-\ua87f'
	sogdian = r'\u10f30-\u10f6f'
	soyombo = r'\u11a50-\u11aaf'
	tibetan = r'\u0f00-\u0fff'
	zanabazar_square = r'\u11a00-\u11a4f'
	ahom = r'\u11700-\u1173f'
	bengali_and_assamese = r'\u0980-\u09ff'
	bhaiksuki = r'\u11c00-\u11c6f'
	brahmi = r'\u11000-\u1107f'
	chakma = r'\u11100-\u1114f'
	devanagari = r'\u0900-\u097f'
	devanagari_extended = r'\ua8e0-\ua8ff'
	dives_akuru = r'\u11900-\u1195f'
	dogra = r'\u11800-\u1184f'
	grantha = r'\u11300-\u1137f'
	gujarati = r'\u0a80-\u0aff'
	gunjala_gondi = r'\u11d60-\u11daf'
	gurmukhi = r'\u0a00-\u0a7f'
	kaithi = r'\u11080-\u110cf'
	kannada = r'\u0c80-\u0cff'
	kharoshthi = r'\u10a00-\u10a5f'
	khojki = r'\u11200-\u1124f'
	khudawadi = r'\u112b0-\u112ff'
	lepcha = r'\u1c00-\u1c4f'
	limbu = r'\u1900-\u194f'
	mahajani = r'\u11150-\u1117f'
	malayalam = r'\u0d00-\u0d7f'
	masaram_gondi = r'\u11d00-\u11d5f'
	meetei_mayek = r'\uabc0-\uabff'
	meetei_mayek_extensions = r'\uaae0-\uaaff'
	modi = r'\u11600-\u1165f'
	mro = r'\u16a40-\u16a6f'
	multani = r'\u11280-\u112af'
	nandinagari = r'\u119a0-\u119ff'
	newa = r'\u11400-\u1147f'
	ol_chiki = r'\u1c50-\u1c7f'
	oriya_odia = r'\u0b00-\u0b7f'
	saurashtra = r'\ua880-\ua8df'
	sharada = r'\u11180-\u111df'
	siddham = r'\u11580-\u115ff'
	sinhala = r'\u0d80-\u0dff'
	sinhala_archaic_numbers = r'\u111e0-\u111ff'
	sora_sompeng = r'\u110d0-\u110ff'
	syloti_nagri = r'\ua800-\ua82f'
	takri = r'\u11680-\u116cf'
	tamil = r'\u0b80-\u0bff'
	tamil_supplement = r'\u11fc0-\u11fff'
	telugu = r'\u0c00-\u0c7f'
	thaana = r'\u0780-\u07bf'
	tirhuta = r'\u11480-\u114df'
	vedic_extensions = r'\u1cd0-\u1cff'
	wancho = r'\u1e2c0-\u1e2ff'
	warang_citi = r'\u118a0-\u118ff'
	cham = r'\uaa00-\uaa5f'
	hanifi_rohingya = r'\u10d00-\u10d3f'
	kayah_li = r'\ua900-\ua92f'
	khmer = r'\u1780-\u17ff'
	khmer_symbols = r'\u19e0-\u19ff'
	lao = r'\u0e80-\u0eff'
	myanmar = r'\u1000-\u109f'
	myanmar_extended_a = r'\uaa60-\uaa7f'
	myanmar_extended_b = r'\ua9e0-\ua9ff'
	new_tai_lue = r'\u1980-\u19df'
	nyiakeng_puachue_hmong = r'\u1e100-\u1e14f'
	pahawh_hmong = r'\u16b00-\u16b8f'
	pau_cin_hau = r'\u11ac0-\u11aff'
	tai_le = r'\u1950-\u197f'
	tai_tham = r'\u1a20-\u1aaf'
	tai_viet = r'\uaa80-\uaadf'
	thai = r'\u0e00-\u0e7f'
	balinese = r'\u1b00-\u1b7f'
	batak = r'\u1bc0-\u1bff'
	buginese = r'\u1a00-\u1a1f'
	buhid = r'\u1740-\u175f'
	hanunoo = r'\u1720-\u173f'
	javanese = r'\ua980-\ua9df'
	makasar = r'\u11ee0-\u11eff'
	rejang = r'\ua930-\ua95f'
	sundanese = r'\u1b80-\u1bbf'
	sundanese_supplement = r'\u1cc0-\u1ccf'
	tagalog = r'\u1700-\u171f'
	tagbanwa = r'\u1760-\u177f'
	bopomofo = r'\u3100-\u312f'
	bopomofo_extended = r'\u31a0-\u31bf'
	cjk_unified_ideographs_han = r'\u4e00-\u9fff'
	cjk_extension_a = r'\u3400-\u4dbf'
	cjk_extension_b = r'\u20000-\u2a6df'
	cjk_extension_c = r'\u2a700-\u2b73f'
	cjk_extension_d = r'\u2b740-\u2b81f'
	cjk_extension_e = r'\u2b820-\u2ceaf'
	cjk_extension_f = r'\u2ceb0-\u2ebe0'
	cjk_extension_g = r'\u30000-\u3134a'
	cjk_compatibility_ideographs = r'\uf900-\ufaff'
	cjk_compatibility_ideographs_supplement = r'\u2f800-\u2fa1f'
	cjk_radicals_kangxi_radicals = r'\u2f00-\u2fdf'
	cjk_radicals_supplement = r'\u2e80-\u2eff'
	cjk_strokes = r'\u31c0-\u31ef'
	ideographic_description_characters = r'\u2ff0-\u2fff'
	hangul_jamo = r'\u1100-\u11ff'
	hangul_jamo_extended_a = r'\ua960-\ua97f'
	hangul_jamo_extended_b = r'\ud7b0-\ud7ff'
	hangul_compatibility_jamo = r'\u3130-\u318f'
	halfwidth_jamo = r'\uffa0-\uffdc'
	hangul_syllables = r'\uac00-\ud7af'
	hiragana = r'\u3040-\u309f'
	kana_extended_a = r'\u1b100-\u1b12f'
	kana_supplement = r'\u1b000-\u1b0ff'
	small_kana_extension = r'\u1b130-\u1b16f'
	kanbun = r'\u3190-\u319f'
	katakana = r'\u30a0-\u30ff'
	katakana_phonetic_extensions = r'\u31f0-\u31ff'
	halfwidth_katakana = r'\uff65-\uff9f'
	khitan_small_script = r'\u18b00-\u18cff'
	lisu = r'\ua4d0-\ua4ff'
	lisu_supplement = r'\u11fb0-\u11fbf'
	miao = r'\u16f00-\u16f9f'
	nushu = r'\u1b170-\u1b2ff'
	tangut = r'\u17000-\u187ff'
	tangut_components = r'\u18800-\u18aff'
	tangut_supplement = r'\u18d00-\u18d08'
	yi_syllables = r'\ua000-\ua48f'
	yi_radicals = r'\ua490-\ua4cf'
	cherokee = r'\u13a0-\u13ff'
	cherokee_supplement = r'\uab70-\uabbf'
	deseret = r'\u10400-\u1044f'
	osage = r'\u104b0-\u104ff'
	unified_canadian_aboriginal_syllabics = r'\u1400-\u167f'
	ucas_extended = r'\u18b0-\u18ff'
	alphabetic_presentation_forms = r'\ufb00-\ufb4f'
	halfwidth_and_fullwidth_forms = r'\uff00-\uffef'

	# return a set of all ranges
	def all(self):
		ur_dict = vars(self)
		ur_vars = list(ur_dict)
		temp = str()
		for i in range(0, len(ur_vars)):
			# exclude non-strings
			if(str(ur_dict[ur_vars[i]].__class__).find('str') != -1):
				# exclude built-in vars
				if(ur_vars[i] == '__module__' or ur_vars[i] == '__dict__' or ur_vars[i] == '__weakref__' or ur_vars[i] == '__doc__'):
					continue
				else:
					temp += ur_dict[ur_vars[i]]
		return temp
# end of class

ur = Unicode_Range
alphabets = ur.all(ur)

# Command-line info and argument parsing
arg_parser = argparse.ArgumentParser(
	description='Make bulk-replacements to your Telegram language. The find:replace pairs should be edited in replacer.py')
arg_parser.add_argument(
	'--lang', metavar='langfile.xml', type=str, required=True,
	help='Your language file (.xml or .strings) exported from the translations platform')
# arg_parser.add_argument(
# 	'-l','--list', metavar='Replace_list.txt', type=str, required=True,
#	help='File containing list of replacements to be make')
arg_parser.add_argument(
	'-p', action="store_true",
	help='Display the replaced translations.')

args = arg_parser.parse_args()
lang_file = str(args.lang)  # str('android_lang_v1234567.xml')
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
			translation = re.subn(r'(?<![\w'+alphabets+r'])'+match_text+r'(?![\w'+alphabets+r'])', replace_text, translation[0], flags=re.U)
			uncased_translation = re.subn(r'(?<![\w'+alphabets+r'])'+match_text+r'(?![\w'+alphabets+r'])', 'UNCASED', translation[0], flags=re.U+re.I) # Use re.DOTALL & re.MULTILINE? #  flags=re.U|S|I|M
			
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
	edited_file_name = str(re.sub(r'(android_x|android)_(.*)[_.].*xml', r'\1_\2_[IMPORT-READY].xml', lang_file))
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
	edited_file_name = re.sub(r'(tdesktop|macos|ios)_(.*)[_.].*strings', r'\1_\2_[IMPORT-READY].strings', lang_file)
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
			translation = re.subn(r'(?<![\w'+alphabets+r'])'+match_text+r'(?![\w'+alphabets+r'])', replace_text, translation[0], flags=re.U)
			uncased_translation = re.subn(r'(?<![\w'+alphabets+r'])'+match_text+r'(?![\w'+alphabets+r'])', 'UNCASED', translation[0], flags =re.U+re.I) # Use re.DOTALL & re.MULTILINE? #  flags = re.U|S|I|M
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
