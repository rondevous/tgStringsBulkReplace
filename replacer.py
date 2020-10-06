# EDIT THIS
REPLACE_DICTIONARY = {
	"groups":"baskets",
	"members":"onions",
	"Forever":"STFU",
}
# Remember: lowercase is not UPPERCASE is not WeIrDcAse


# DO NOT EDIT THE CODE BELOW (unless you know Python and RegEx)


#!TODO: create an [OFFLINE-USE].xml
#!TODO: Save inside folders?

KEYLIST = list(REPLACE_DICTIONARY)
# Imports
import xml.etree.ElementTree as ET
import re
import argparse

unicode_custom_alphabet_set = {
	### Unicode Scripts
	"armenian":r"\U00000530-\U0000058f",
	"armenian_ligatures":r"\U0000fb13-\U0000fb17",
	"carian":r"\U000102a0-\U000102df",
	"caucasian_albanian":r"\U00010530-\U0001056f",
	"cypriot_syllabary":r"\U00010800-\U0001083f",
	#In Alphabetics
	# CYRILLIC_CAPITAL_LETTER_SHORT_I_WITH_TAIL = '0000048A-0000052F'
	#~Within_range(cyrillic to cyrillic_supplement)
	"cyrillic":r"\U00000400-\U000004ff",
	"cyrillic_supplement":r"\U00000500-\U0000052f",
	"cyrillic_extended_a":r"\U00002de0-\U00002dff",
	"cyrillic_extended_b":r"\U0000a640-\U0000a69f",
	"cyrillic_extended_c":r"\U00001c80-\U00001c8f",
	"elbasan":r"\U00010500-\U0001052f",
	"georgian":r"\U000010a0-\U000010ff",
	"georgian_extended":r"\U00001c90-\U00001cbf",
	"georgian_supplement":r"\U00002d00-\U00002d2f",
	"glagolitic":r"\U00002c00-\U00002c5f",
	"glagolitic_supplement":r"\U0001e000-\U0001e02f",
	"gothic":r"\U00010330-\U0001034f",
	#In Alphabetics
	#	GREEK_CAPITAL_LETTER_SHO = '000003F7-00000481'
	#~Within_range(greek to cyrillic)
	"greek":r"\U00000370-\U000003ff",
	"greek_extended":r"\U00001f00-\U00001fff",
	"ancient_greek_numbers":r"\U00010140-\U0001018f",
	#In Alphabetics
	#	LATIN_SMALL_LETTER_O_WITH_STROKE = '000000F8-000001BA'
	#~Within_range(latin_1_supplement to latin_extended_b)
	"latin_1_supplement":r"\U00000080-\U000000ff",
	"latin_extended_a":r"\U00000100-\U0000017f",
	#In Alphabetics
	# LATIN_CAPITAL_LETTER_DZ_WITH_CARON = '000001C4-00000293'
	#~Within_range(latin_extended_b to ipa_extensions)
	"latin_extended_b":r"\U00000180-\U0000024f",
	#In Alphabetics
	# LATIN_CAPITAL_LETTER_S_WITH_SWASH_TAIL = '00002C7E-00002CE4'
	#~Within_range(latin_extended_c to coptic)
	"latin_extended_c":r"\U00002c60-\U00002c7f",
	#In Alphabetics
	# LATIN_EPIGRAPHIC_LETTER_REVERSED_F = '0000A7FB-0000A801'
	#~Within_range(latin_extended_d to syloti_nagri)
	"latin_extended_d":r"\U0000a720-\U0000a7ff",
	"latin_extended_e":r"\U0000ab30-\U0000ab6f",
	#In Alphabetic
	# LATIN_CAPITAL_LETTER_A_WITH_RING_BELOW = '00001E00-00001F15'
	#~Within_range(latin_extended_additional to greek_extended)
	"latin_extended_additional":r"\U00001e00-\U00001eff",
	"latin_ligatures":r"\U0000fb00-\U0000fb06",
	"fullwidth_latin_letters":r"\U0000ff00-\U0000ff5e",
	"ipa_extensions":r"\U00000250-\U000002af",
	#In Alphbetics
	# LATIN_SMALL_LETTER_INSULAR_G = '00001D79-00001D9A'
	#~Within_range(phonetic_extensions to phonetic_extensions_supplement)
	"phonetic_extensions":r"\U00001d00-\U00001d7f",
	"phonetic_extensions_supplement":r"\U00001d80-\U00001dbf",
	"linear_a":r"\U00010600-\U0001077f",
	"linear_b_syllabary":r"\U00010000-\U0001007f",
	"linear_b_ideograms":r"\U00010080-\U000100ff",
	"aegean_numbers":r"\U00010100-\U0001013f",
	"lycian":r"\U00010280-\U0001029f",
	"lydian":r"\U00010920-\U0001093f",
	"ogham":r"\U00001680-\U0000169f",
	"old_hungarian":r"\U00010c80-\U00010cff",
	#In Alphabetics
	# OLD_ITALIC_LETTER_YE = '0001032D-00010340'
	#~Within_range(old_italic to gothic)
	"old_italic":r"\U00010300-\U0001032f",
	"old_permic":r"\U00010350-\U0001037f",
	"phaistos_disc":r"\U000101d0-\U000101ff",
	"runic":r"\U000016a0-\U000016ff",
	"shavian":r"\U00010450-\U0001047f",
	"modifier_tone_letters":r"\U0000a700-\U0000a71f",
	"spacing_modifier_letters":r"\U000002b0-\U000002ff",
	"superscripts_and_subscripts":r"\U00002070-\U0000209f",
	"combining_diacritical_marks":r"\U00000300-\U0000036f",
	"combining_diacritical_marks_extended":r"\U00001ab0-\U00001aff",
	"combining_diacritical_marks_supplement":r"\U00001dc0-\U00001dff",
	"combining_diacritical_marks_for_symbols":r"\U000020d0-\U000020ff",
	"combining_half_marks":r"\U0000fe20-\U0000fe2f",
	"adlam":r"\U0001e900-\U0001e95f",
	"bamum":r"\U0000a6a0-\U0000a6ff",
	"bamum_supplement":r"\U00016800-\U00016a3f",
	"bassa_vah":r"\U00016ad0-\U00016aff",
	"coptic":r"\U00002c80-\U00002cff",
	"coptic_in_greek_block":r"\U000003e2-\U000003ef",
	"coptic_epact_numbers":r"\U000102e0-\U000102ff",
	"egyptian_hieroglyphs":r"\U00013000-\U0001342f",
	"egyptian_hieroglyph_format_controls":r"\U00013430-\U0001343f",
	"ethiopic":r"\U00001200-\U0000137f",
	"ethiopic_supplement":r"\U00001380-\U0000139f",
	"ethiopic_extended":r"\U00002d80-\U00002ddf",
	"ethiopic_extended_a":r"\U0000ab00-\U0000ab2f",
	"medefaidrin":r"\U00016e40-\U00016e9f",
	"mende_kikakui":r"\U0001e800-\U0001e8df",
	#In Alphabetics
	# MEROITIC_HIEROGLYPHIC_LETTER_A = '00010980-000109B7'
	#~Within_range(meroitic_hieroglyphs to meroitic_cursive)
	"meroitic_cursive":r"\U000109a0-\U000109ff",
	"meroitic_hieroglyphs":r"\U00010980-\U0001099f",
	"n_ko":r"\U000007c0-\U000007ff",
	#From Alphabetics
	#	SHAVIAN_LETTER_PEEP = '00010450-0001049D'
	"SHAVIAN_LETTER_PEEP_modified":r"\U00010450-\U0001047F",
	"osmanya":r"\U00010480-\U000104af",
	"tifinagh":r"\U00002d30-\U00002d7f",
	"vai":r"\U0000a500-\U0000a63f",
	"anatolian_hieroglyphs":r"\U00014400-\U0001467f",
	"arabic":r"\U00000600-\U000006ff",
	"arabic_supplement":r"\U00000750-\U0000077f", #requireAll
	#In Alphabetics
	# ARABIC_OPEN_FATHATAN = '000008F0-00000902'
	#~Within_range(arabic_extended_a to devanagari)
	"arabic_extended_a":r"\U000008a0-\U000008ff",
	"arabic_presentation_forms_a":r"\U0000fb50-\U0000fdff",
	"arabic_presentation_forms_b":r"\U0000fe70-\U0000feff",
	#In Alphabetics
	# CYPRIOT_SYLLABLE_ZO = '0001083F-00010855'
	#~Within_range(cypriot_syllabary to aramaic_imperial)
	"aramaic_imperial":r"\U00010840-\U0001085f",
	"avestan":r"\U00010b00-\U00010b3f",
	"chorasmian":r"\U00010fb0-\U00010fdf",
	"cuneiform":r"\U00012000-\U000123ff",
	"cuneiform_numbers_and_punctuation":r"\U00012400-\U0001247f",
	"early_dynastic_cuneiform":r"\U00012480-\U0001254f",
	"old_persian":r"\U000103a0-\U000103df",
	"ugaritic":r"\U00010380-\U0001039f",
	"elymaic":r"\U00010fe0-\U00010fff",
	"hatran":r"\U000108e0-\U000108ff",
	"hebrew":r"\U00000590-\U000005ff",
	#In Alphabetics
	#	HEBREW_LETTER_TSADI_WITH_DAGESH = '0000FB46-0000FBB1'
	#~Within_range(hebrew_presentation_forms to arabic_presentation_forms_a)
	"hebrew_presentation_forms":r"\U0000fb1d-\U0000fb4f",
	"mandaic":r"\U00000840-\U0000085f",
	"nabataean":r"\U00010880-\U000108af",
	"old_north_arabian":r"\U00010a80-\U00010a9f",
	"old_south_arabian":r"\U00010a60-\U00010a7f",
	"pahlavi_inscriptional":r"\U00010b60-\U00010b7f",
	"pahlavi_psalter":r"\U00010b80-\U00010baf",
	"palmyrene":r"\U00010860-\U0001087f",
	"parthian_inscriptional":r"\U00010b40-\U00010b5f",
	"phoenician":r"\U00010900-\U0001091f",
	"samaritan":r"\U00000800-\U0000083f",
	#In Alphabetics
	# SYRIAC_LETTER_SOGDIAN_ZHAIN = '0000074D-000007A5'
	#~Within_range(syriac --to-- arabic_supplement --to-- thaana)
	"syriac":r"\U00000700-\U0000074f",
	"syriac_supplement":r"\U00000860-\U0000086f",
	"yezidi":r"\U00010e80-\U00010ebf",
	"manichaean":r"\U00010ac0-\U00010aff",
	"marchen":r"\U00011c70-\U00011cbf",
	"mongolian":r"\U00001800-\U000018af",
	"mongolian_supplement":r"\U00011660-\U0001167f",
	"old_sogdian":r"\U00010f00-\U00010f2f",
	"old_turkic":r"\U00010c00-\U00010c4f",
	"phags_pa":r"\U0000a840-\U0000a87f",
	"sogdian":r"\U00010f30-\U00010f6f",
	"soyombo":r"\U00011a50-\U00011aaf",
	"tibetan":r"\U00000f00-\U00000fff",
	"zanabazar_square":r"\U00011a00-\U00011a4f",
	"ahom":r"\U00011700-\U0001173f",
	"bengali_and_assamese":r"\U00000980-\U000009ff",
	"bhaiksuki":r"\U00011c00-\U00011c6f",
	"brahmi":r"\U00011000-\U0001107f",
	"chakma":r"\U00011100-\U0001114f",
	#In Alphabetics
	# DEVANAGARI_LETTER_CANDRA_A = '00000972-00000980'
	#~Within_range(devanagari to bengali_and_assamese)
	"devanagari":r"\U00000900-\U0000097f",
	"devanagari_extended":r"\U0000a8e0-\U0000a8ff",
	#In Alphabetics
	# WARANG_CITI_OM = '000118FF-00011906'
	#~WITHIN_RANGE(warang_citi to dives_akuru)
	"dives_akuru":r"\U00011900-\U0001195f",
	"dogra":r"\U00011800-\U0001184f",
	"grantha":r"\U00011300-\U0001137f",
	"gujarati":r"\U00000a80-\U00000aff",
	"gunjala_gondi":r"\U00011d60-\U00011daf",
	"gurmukhi":r"\U00000a00-\U00000a7f",
	"kaithi":r"\U00011080-\U000110cf",
	"kannada":r"\U00000c80-\U00000cff",
	"kharoshthi":r"\U00010a00-\U00010a5f",
	"khojki":r"\U00011200-\U0001124f",
	"khudawadi":r"\U000112b0-\U000112ff",
	"lepcha":r"\U00001c00-\U00001c4f",
	"limbu":r"\U00001900-\U0000194f",
	"mahajani":r"\U00011150-\U0001117f",
	"malayalam":r"\U00000d00-\U00000d7f",
	"masaram_gondi":r"\U00011d00-\U00011d5f",
	"meetei_mayek":r"\U0000abc0-\U0000abff",
	"meetei_mayek_extensions":r"\U0000aae0-\U0000aaff",
	"modi":r"\U00011600-\U0001165f",
	"mro":r"\U00016a40-\U00016a6f",
	"multani":r"\U00011280-\U000112af",
	"nandinagari":r"\U000119a0-\U000119ff",
	"newa":r"\U00011400-\U0001147f",
	"ol_chiki":r"\U00001c50-\U00001c7f",
	"oriya_odia":r"\U00000b00-\U00000b7f",
	"saurashtra":r"\U0000a880-\U0000a8df",
	"sharada":r"\U00011180-\U000111df",
	"siddham":r"\U00011580-\U000115ff",
	"sinhala":r"\U00000d80-\U00000dff",
	"sinhala_archaic_numbers":r"\U000111e0-\U000111ff",
	"sora_sompeng":r"\U000110d0-\U000110ff",
	"syloti_nagri":r"\U0000a800-\U0000a82f",
	"takri":r"\U00011680-\U000116cf",
	"tamil":r"\U00000b80-\U00000bff",
	"tamil_supplement":r"\U00011fc0-\U00011fff",
	"telugu":r"\U00000c00-\U00000c7f",
	"thaana":r"\U00000780-\U000007bf",
	"tirhuta":r"\U00011480-\U000114df",
	"vedic_extensions":r"\U00001cd0-\U00001cff",
	"wancho":r"\U0001e2c0-\U0001e2ff",
	"warang_citi":r"\U000118a0-\U000118ff",
	"cham":r"\U0000aa00-\U0000aa5f",
	"hanifi_rohingya":r"\U00010d00-\U00010d3f",
	"kayah_li":r"\U0000a900-\U0000a92f",
	"khmer":r"\U00001780-\U000017ff",
	"khmer_symbols":r"\U000019e0-\U000019ff",
	"lao":r"\U00000e80-\U00000eff",
	"myanmar":r"\U00001000-\U0000109f",
	#In Alphabetics
	# MYANMAR_LETTER_SHWE_PALAUNG_CHA = '0000AA7E-0000AAAF'
	#~Within_range(myanmar_extended_a to tai_viet)
	"myanmar_extended_a":r"\U0000aa60-\U0000aa7f",
	"myanmar_extended_b":r"\U0000a9e0-\U0000a9ff",
	"new_tai_lue":r"\U00001980-\U000019df",
	"nyiakeng_puachue_hmong":r"\U0001e100-\U0001e14f",
	"pahawh_hmong":r"\U00016b00-\U00016b8f",
	"pau_cin_hau":r"\U00011ac0-\U00011aff",
	"tai_le":r"\U00001950-\U0000197f",
	"tai_tham":r"\U00001a20-\U00001aaf",
	"tai_viet":r"\U0000aa80-\U0000aadf",
	"thai":r"\U00000e00-\U00000e7f",
	"balinese":r"\U00001b00-\U00001b7f",
	"batak":r"\U00001bc0-\U00001bff",
	"buginese":r"\U00001a00-\U00001a1f",
	"buhid":r"\U00001740-\U0000175f",
	"hanunoo":r"\U00001720-\U0000173f",
	"javanese":r"\U0000a980-\U0000a9df",
	"makasar":r"\U00011ee0-\U00011eff",
	"rejang":r"\U0000a930-\U0000a95f",
	#In Alphabetics
	# SUNDANESE_AVAGRAHA = '00001BBA-00001BE5'
	#~Within_range(sundanese to batak)
	"sundanese":r"\U00001b80-\U00001bbf",
	"sundanese_supplement":r"\U00001cc0-\U00001ccf",
	"tagalog":r"\U00001700-\U0000171f",
	"tagbanwa":r"\U00001760-\U0000177f",
	"bopomofo":r"\U00003100-\U0000312f",
	"bopomofo_extended":r"\U000031a0-\U000031bf",
	"cjk_unified_ideographs_han":r"\U00004e00-\U00009fff",
	"cjk_extension_a":r"\U00003400-\U00004dbf",
	"cjk_extension_b":r"\U00020000-\U0002a6df",
	"cjk_extension_c":r"\U0002a700-\U0002b73f",
	"cjk_extension_d":r"\U0002b740-\U0002b81f",
	"cjk_extension_e":r"\U0002b820-\U0002ceaf",
	"cjk_extension_f":r"\U0002ceb0-\U0002ebe0",
	"cjk_extension_g":r"\U00030000-\U0003134a",
	"cjk_compatibility_ideographs":r"\U0000f900-\U0000faff",
	"cjk_compatibility_ideographs_supplement":r"\U0002f800-\U0002fa1f",
	"cjk_radicals_kangxi_radicals":r"\U00002f00-\U00002fdf",
	"cjk_radicals_supplement":r"\U00002e80-\U00002eff",
	"cjk_strokes":r"\U000031c0-\U000031ef",
	"ideographic_description_characters":r"\U00002ff0-\U00002fff",
	#In Alphabetics
	# HANGUL_CHOSEONG_KIYEOK = '00001100-00001248'
	#~Within_range(hangul_jamo to ethiopic)
	"hangul_jamo":r"\U00001100-\U000011ff",
	"hangul_jamo_extended_a":r"\U0000a960-\U0000a97f",
	"hangul_jamo_extended_b":r"\U0000d7b0-\U0000d7ff",
	"hangul_compatibility_jamo":r"\U00003130-\U0000318f",
	"halfwidth_jamo":r"\U0000ffa0-\U0000ffdc",
	"hangul_syllables":r"\U0000ac00-\U0000d7af",
	"hiragana":r"\U00003040-\U0000309f",
	# Borrowed from Alphabetic
	"KATAKANA_LETTER_ARCHAIC_E":r"\U0001b000-\U0001b11e", #bonus +256
	# kana_extended_a = '0001b100-0001b12f' #empty=17
	"kana_supplement":r"\U0001b000-\U0001b0ff",
	"small_kana_extension":r"\U0001b130-\U0001b16f",
	"kanbun":r"\U00003190-\U0000319f",
	"katakana":r"\U000030a0-\U000030ff",
	"katakana_phonetic_extensions":r"\U000031f0-\U000031ff",
	"halfwidth_katakana":r"\U0000ff65-\U0000ff9f",
	"khitan_small_script":r"\U00018b00-\U00018cff",
	"lisu":r"\U0000a4d0-\U0000a4ff",
	"lisu_supplement":r"\U00011fb0-\U00011fbf",
	"miao":r"\U00016f00-\U00016f9f",
	"nushu":r"\U0001b170-\U0001b2ff",
	"tangut":r"\U00017000-\U000187ff",
	# Borrowed from Alphabetic
	"TANGUT_COMPONENT_001":r"\U00018800-\U00018CD5", #bonus +470
	# tangut_components = '00018800-00018aff'
	"tangut_supplement":r"\U00018d00-\U00018d08",
	"yi_syllables":r"\U0000a000-\U0000a48f",
	"yi_radicals":r"\U0000a490-\U0000a4cf",
	"cherokee":r"\U000013a0-\U000013ff",
	"cherokee_supplement":r"\U0000ab70-\U0000abbf",
	"deseret":r"\U00010400-\U0001044f",
	"osage":r"\U000104b0-\U000104ff",
	#!MOD: omit symbols
	# unified_canadian_aboriginal_syllabics = r'\U00001400-\U0000167f'
	"unified_canadian_aboriginal_syllabics_SYLLABLES":r"\U00001401-\U0000166c",
	"unified_canadian_aboriginal_syllabics_SYLLABLES_MORE":r"\U0000166f-\U0000167f",
	"ucas_extended":r"\U000018b0-\U000018ff",
	"alphabetic_presentation_forms":r"\U0000fb00-\U0000fb4f",
	#!MOD: omit symbols
	# halfwidth_and_fullwidth_forms = r'\U0000ff00-\U0000ffef'
	"halfwidth_and_fullwidth_forms_NUMBERS_LATIN":r"\U0000ff10-\U0000ff19",
	"halfwidth_and_fullwidth_forms_BIG_LATIN":r"\U0000ff21-\U0000ff3a",
	"halfwidth_and_fullwidth_forms_SMALL_LATIN":r"\U0000ff41-\U0000ff5a",
	"halfwidth_and_fullwidth_forms_KATAKANA":r"\U0000ff65-\U0000ffdc",
	# BORROWED from Alphabetic:
	"LATIN_CAPITAL_LETTER_A":r"\U00000041-\U0000005A",
	"LATIN_SMALL_LETTER_A":r"\U00000061-\U0000007A",
	"ARABIC_LETTER_HEH_WITH_INVERTED_V":r"\U000006FF",
	"DOUBLE_STRUCK_CAPITAL_C":r'\U00002102',
	"EULER_CONSTANT":r"\U00002107",
	"SCRIPT_SMALL_G":r"\U0000210A-\U00002113",
	"DOUBLE_STRUCK_CAPITAL_N":r"\U00002115",
	"DOUBLE_STRUCK_CAPITAL_P":r"\U00002119-\U0000211D",
	"DOUBLE_STRUCK_CAPITAL_Z":r"\U00002124",
	"OHM_SIGN":r"\U00002126",
	"BLACK_LETTER_CAPITAL_Z":r"\U00002128",
	"KELVIN_SIGN":r"\U0000212A-\U0000212D",
	"SCRIPT_SMALL_E":r"\U0000212F-\U00002134",
	"ALEF_SYMBOL":r"\U00002135-\U00002138",
	"INFORMATION_SOURCE":r"\U00002139",
	"DOUBLE_STRUCK_SMALL_PI":r"\U0000213C-\U0000213F",
	"DOUBLE_STRUCK_ITALIC_CAPITAL_D":r"\U00002145-\U00002149",
	"TURNED_SMALL_F":r"\U0000214E",
	"ROMAN_NUMERAL_ONE":r"\U00002160-\U00002182",
	"ROMAN_NUMERAL_REVERSED_ONE_HUNDRED":r"\U00002183-\U00002184",
	"ROMAN_NUMERAL_SIX_LATE_FORM":r"\U00002185-\U00002188",
	"CIRCLED_LATIN_CAPITAL_LETTER_A":r"\U000024B6-\U000024E9",
	"VERTICAL_TILDE":r"\U00002E2F",
	"IDEOGRAPHIC_ITERATION_MARK":r"\U00003005",
	"IDEOGRAPHIC_CLOSING_MARK":r"\U00003006",
	"IDEOGRAPHIC_NUMBER_ZERO":r"\U00003007",
	"HANGZHOU_NUMERAL_ONE":r"\U00003021-\U00003029",
	"VERTICAL_KANA_REPEAT_MARK":r"\U00003031-\U00003035",
	"HANGZHOU_NUMERAL_TEN":r"\U00003038-\U0000303A",
	"VERTICAL_IDEOGRAPHIC_ITERATION_MARK":r"\U0000303B",
	"MASU_MARK":r"\U0000303C",
	"HIRAGANA_DIGRAPH_YORI":r"\U0000309F",
	"KATAKANA_DIGRAPH_KOTO":r"\U000030FF",
	"DEVANAGARI_VOWEL_SIGN_AY":r"\U0000A8FF",
	"TANGUT_ITERATION_MARK":r"\U00016FE0-\U00016FE1",
	"OLD_CHINESE_ITERATION_MARK":r"\U00016FE3",
	"VIETNAMESE_ALTERNATE_READING_MARK_CA":r"\U00016FF0-\U00016FF1",
	"DUPLOYAN_LETTER_H":r"\U0001BC00-\U0001BC6A",
	"DUPLOYAN_AFFIX_LEFT_HORIZONTAL_SECANT":r"\U0001BC70-\U0001BC7C",
	"DUPLOYAN_AFFIX_HIGH_ACUTE":r"\U0001BC80-\U0001BC88",
	"DUPLOYAN_AFFIX_LOW_ACUTE":r"\U0001BC90-\U0001BC99",
	"DUPLOYAN_DOUBLE_MARK":r"\U0001BC9E",
	"MATHEMATICAL_BOLD_CAPITAL_A":r"\U0001D400-\U0001D454",
	"MATHEMATICAL_ITALIC_SMALL_I":r"\U0001D456-\U0001D49C",
	"MATHEMATICAL_SCRIPT_CAPITAL_C":r"\U0001D49E-\U0001D49F",
	"MATHEMATICAL_SCRIPT_CAPITAL_G":r"\U0001D4A2",
	"MATHEMATICAL_SCRIPT_CAPITAL_J":r"\U0001D4A5-\U0001D4A6",
	"MATHEMATICAL_SCRIPT_CAPITAL_N":r"\U0001D4A9-\U0001D4AC",
	"MATHEMATICAL_SCRIPT_CAPITAL_S":r"\U0001D4AE-\U0001D4B9",
	"MATHEMATICAL_SCRIPT_SMALL_F":r"\U0001D4BB",
	"MATHEMATICAL_SCRIPT_SMALL_H":r"\U0001D4BD-\U0001D4C3",
	"MATHEMATICAL_SCRIPT_SMALL_P":r"\U0001D4C5-\U0001D505",
	"MATHEMATICAL_FRAKTUR_CAPITAL_D":r"\U0001D507-\U0001D50A",
	"MATHEMATICAL_FRAKTUR_CAPITAL_J":r"\U0001D50D-\U0001D514",
	"MATHEMATICAL_FRAKTUR_CAPITAL_S":r"\U0001D516-\U0001D51C",
	"MATHEMATICAL_FRAKTUR_SMALL_A":r"\U0001D51E-\U0001D539",
	"MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_D":r"\U0001D53B-\U0001D53E",
	"MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_I":r"\U0001D540-\U0001D544",
	"MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_O":r"\U0001D546",
	"MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_S":r"\U0001D54A-\U0001D550",
	"MATHEMATICAL_DOUBLE_STRUCK_SMALL_A":r"\U0001D552-\U0001D6A5",
	"MATHEMATICAL_BOLD_CAPITAL_ALPHA":r"\U0001D6A8-\U0001D6C0",
	"MATHEMATICAL_BOLD_SMALL_ALPHA":r"\U0001D6C2-\U0001D6DA",
	"MATHEMATICAL_BOLD_EPSILON_SYMBOL":r"\U0001D6DC-\U0001D6FA",
	"MATHEMATICAL_ITALIC_SMALL_ALPHA":r"\U0001D6FC-\U0001D714",
	"MATHEMATICAL_ITALIC_EPSILON_SYMBOL":r"\U0001D716-\U0001D734",
	"MATHEMATICAL_BOLD_ITALIC_SMALL_ALPHA":r"\U0001D736-\U0001D74E",
	"MATHEMATICAL_BOLD_ITALIC_EPSILON_SYMBOL":r"\U0001D750-\U0001D76E",
	"MATHEMATICAL_SANS_SERIF_BOLD_SMALL_ALPHA":r"\U0001D770-\U0001D788",
	"MATHEMATICAL_SANS_SERIF_BOLD_EPSILON_SYMBOL":r"\U0001D78A-\U0001D7A8",
	"MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_SMALL_ALPHA":r"\U0001D7AA-\U0001D7C2",
	"MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_EPSILON_SYMBOL":r"\U0001D7C4-\U0001D7CB",
	"ARABIC_MATHEMATICAL_ALEF":r"\U0001EE00-\U0001EE03",
	"ARABIC_MATHEMATICAL_WAW":r"\U0001EE05-\U0001EE1F",
	"ARABIC_MATHEMATICAL_INITIAL_BEH":r"\U0001EE21-\U0001EE22",
	"ARABIC_MATHEMATICAL_INITIAL_HEH":r"\U0001EE24",
	"ARABIC_MATHEMATICAL_INITIAL_HAH":r"\U0001EE27",
	"ARABIC_MATHEMATICAL_INITIAL_YEH":r"\U0001EE29-\U0001EE32",
	"ARABIC_MATHEMATICAL_INITIAL_SHEEN":r"\U0001EE34-\U0001EE37",
	"ARABIC_MATHEMATICAL_INITIAL_DAD":r"\U0001EE39",
	"ARABIC_MATHEMATICAL_INITIAL_GHAIN":r"\U0001EE3B",
	"ARABIC_MATHEMATICAL_TAILED_JEEM":r"\U0001EE42",
	"ARABIC_MATHEMATICAL_TAILED_HAH":r"\U0001EE47",
	"ARABIC_MATHEMATICAL_TAILED_YEH":r"\U0001EE49",
	"ARABIC_MATHEMATICAL_TAILED_LAM":r"\U0001EE4B",
	"ARABIC_MATHEMATICAL_TAILED_NOON":r"\U0001EE4D-\U0001EE4F",
	"ARABIC_MATHEMATICAL_TAILED_SAD":r"\U0001EE51-\U0001EE52",
	"ARABIC_MATHEMATICAL_TAILED_SHEEN":r"\U0001EE54",
	"ARABIC_MATHEMATICAL_TAILED_KHAH":r"\U0001EE57",
	"ARABIC_MATHEMATICAL_TAILED_DAD":r"\U0001EE59",
	"ARABIC_MATHEMATICAL_TAILED_GHAIN":r"\U0001EE5B",
	"ARABIC_MATHEMATICAL_TAILED_DOTLESS_NOON":r"\U0001EE5D",
	"ARABIC_MATHEMATICAL_TAILED_DOTLESS_QAF":r"\U0001EE5F",
	"ARABIC_MATHEMATICAL_STRETCHED_BEH":r"\U0001EE61-\U0001EE62",
	"ARABIC_MATHEMATICAL_STRETCHED_HEH":r"\U0001EE64",
	"ARABIC_MATHEMATICAL_STRETCHED_HAH":r"\U0001EE67-\U0001EE6A",
	"ARABIC_MATHEMATICAL_STRETCHED_MEEM":r"\U0001EE6C-\U0001EE72",
	"ARABIC_MATHEMATICAL_STRETCHED_SHEEN":r"\U0001EE74-\U0001EE77",
	"ARABIC_MATHEMATICAL_STRETCHED_DAD":r"\U0001EE79-\U0001EE7C",
	"ARABIC_MATHEMATICAL_STRETCHED_DOTLESS_FEH":r"\U0001EE7E",
	"ARABIC_MATHEMATICAL_LOOPED_ALEF":r"\U0001EE80-\U0001EE89",
	"ARABIC_MATHEMATICAL_LOOPED_LAM":r"\U0001EE8B-\U0001EE9B",
	"ARABIC_MATHEMATICAL_DOUBLE_STRUCK_BEH":r"\U0001EEA1-\U0001EEA3",
	"ARABIC_MATHEMATICAL_DOUBLE_STRUCK_WAW":r"\U0001EEA5-\U0001EEA9",
	"ARABIC_MATHEMATICAL_DOUBLE_STRUCK_LAM":r"\U0001EEAB-\U0001EEBB",
	"SQUARED_LATIN_CAPITAL_LETTER_A":r"\U0001F130-\U0001F149",
	"NEGATIVE_CIRCLED_LATIN_CAPITAL_LETTER_A":r"\U0001F150-\U0001F169",
	"NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_A":r"\U0001F170-\U0001F189",
}

# return a custom set of unicode characters
def CustomAlphabets():
	custom_values = list(unicode_custom_alphabet_set.values())
	result = str()
	for i in range(0, len(custom_values)):
		result += custom_values[i]
	return result
# end of Unicode Scripts

CUSTOM_ALPHABETS = CustomAlphabets()

# Command-line info and argument parsing
arg_parser = argparse.ArgumentParser(
	description='Make bulk-replacements to your Telegram language. The find:replace pairs should be edited in replacer.py')
arg_parser.add_argument(
	'--lang', metavar='  ', type=str, required=True,
	help='exported language file (.strings or .xml)')
# arg_parser.add_argument(
# 	'-l','--list', metavar='Replace_list.txt', type=str, required=True,
#	help='File containing list of replacements to be make')
arg_parser.add_argument(
	'-v', '--verbose', action="store_true",
	help='show the replaced strings')

args = arg_parser.parse_args()
lang_file = str(args.lang)  # 'android_lang_v1234567.xml'
print("\n\nUsing File:\n\t"+lang_file)

# logs
uncasedlog = open("uncased.log", 'w')
Non_Exact_Log = open("non-exact.log", 'w')
imperfectlog = open("imperfect.log", 'w')

# Variables
global tree, dot_strings, total_cased, total_imperfect, total_uncased, total_nonexact, skipped

# Set to 0
total_nonexact = total_uncased = total_imperfect = total_cased = 0

skipped = list()
# match_text = 'dummy'
# replace_text = 'XXdummyXX'

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

class Loop_Replacements:
	def replace(self, tr_string):
		# global REPLACE_DICTIONARY, KEYLIST, ALPHABETS
		global total_cased, total_imperfect, total_uncased, total_nonexact
		# Reset stats & strings
		self.non_exact_now = self.uncased_now = self.imperfect_now = self.exact_now = 0
		self.imperfect_tr = self.non_exact_tr = self.uncased_tr = self.translation = (tr_string, 0)
		for key in KEYLIST:
			match_text = re.escape(str(key))
			replace_text = str(REPLACE_DICTIONARY[key])
			# Replacements
			self.translation = re.subn(r'(?<!['+CUSTOM_ALPHABETS+r'])'+match_text+r'(?!['+CUSTOM_ALPHABETS+r'])', replace_text, self.translation[0], flags=re.U)
			self.imperfect_tr = re.subn(r'(?<![\w])'+match_text+r'(?![\w])', replace_text, self.imperfect_tr[0], flags=re.U) # old replacer
			self.uncased_tr = re.subn(r'(?<!['+CUSTOM_ALPHABETS+r'])'+match_text+r'(?!['+CUSTOM_ALPHABETS+r'])', 'UNCASED', self.uncased_tr[0], flags=re.U+re.I) # Use re.DOTALL & re.MULTILINE? #  flags=re.U|S|I|M
			self.non_exact_tr = re.subn(match_text, replace_text, self.non_exact_tr[0], flags=re.U)
			# Current Stats
			self.exact_now += self.translation[1]
			self.imperfect_now += self.imperfect_tr[1]
			self.uncased_now += self.uncased_tr[1]
			self.non_exact_now += self.non_exact_tr[1]
		# End replacements for this string
		# Total Stats and Logs
		total_cased += self.exact_now
		temp = self.imperfect_now - self.exact_now
		if(temp > 0): #!TODO: make an xml instead?
			total_imperfect += temp
			imperfectlog.write(str(self.imperfect_tr[0])+'\n') # Log imperfect replacements
		#
		temp = self.uncased_now - self.exact_now
		if(temp > 0):
			total_uncased += temp
			uncasedlog.write(str(self.translation[0])+'\n') # Log uncased
		#
		temp = self.non_exact_now - self.exact_now
		if(temp > 0):
			total_nonexact += temp
			Non_Exact_Log.write(str(self.non_exact_tr[0])+'\n') # Log non-exact replacements
		#
		return self.translation[0]
	#

# Prints summary
def printSummary():
	print('\nSkipped:')
	for i in range(0, len(skipped)):
		print('\t<'+skipped[i]+'>')
	#
	print("\nLOGS:")
	if total_imperfect != 0:
		print('\t'+str(total_imperfect)+' imperfect replacements ignored')
		print("\t(Refer 'imperfect.log', for possible replacements)")
	if total_nonexact != 0:
		print('\n\t'+str(total_nonexact)+' non-exact replacements ignored')
		print("\t(Refer 'non-exact.log', for non-whole-word replacements)")
	print('\nSUMMARY:')
	print('\t'+str(len(skipped)),'skipped/overlooked')
	print('\t'+str(total_cased),'replaced in',(rplStrCount),'strings.')
	if total_uncased != 0:
		print('\t'+str(total_uncased)+' uncased replacements ignored')
		print("(See 'uncased.log' and add them to the dictionary)")
	print("\nImport File:\n\t"+edited_file_name)
	print("\nPlease double check when importing.\n")
	#

# Algo for XML replacer
if(isXML()):
	# tree = ET.parse(lang_file)
	global tree
	root = tree.getroot()	# <Element 'resources'>
	if(args.verbose):
		print('\n\nThese strings have been edited:\n')
	strCount = 1
	rplStrCount = 0
	LR = Loop_Replacements
	for string in root.findall('string'):
		string_name = string.get('name')
		if(string_name == 'language_code' or string_name == 'LanguageCode'): # skip
			strCount += 1
			skipped.append(string_name)
			continue
		current_string = str(string.text)
		#
		# LR.replace(LR, current_string)
		string.text = LR.replace(LR, current_string)
		#
		if(LR().exact_now == 0):
			strCount += 1
			root.remove(string)
			continue
		elif(args.verbose):
			# print('\n'+str(strCount)+'. '+string_name+'')
			print(f"[{strCount}]", string.text)
		# string.text = LR().translation[0]
		rplStrCount += 1
		strCount += 1
	#end replacing strings
	imperfectlog.close()
	uncasedlog.close()
	Non_Exact_Log.close()
	#
	edited_file_name = str(re.sub(r'(android_x|android)_(.*)[_.].*xml', r'\1_\2_[IMPORT-READY].xml', lang_file))
	tree.write(edited_file_name, xml_declaration=True, encoding='Unicode')
	#
	printSummary()
	# Cleanup Memory
	re.purge()
	del root, tree, ET # xml memory cleanup
	#
# Algo for .strings replacer
elif(isStrings()):
	global dot_strings
	# open file -> copy all data -> iterate -> write out new file
	# dot_strings = open(lang_file, 'r').read()
	edited_file_name = re.sub(r'(tdesktop|macos|ios)_(.*)[_.].*strings', r'\1_\2_[IMPORT-READY].strings', lang_file)
	new_strings = open(edited_file_name, 'w', encoding='UTF-8')
	#
	if(args.verbose):
		print('\n\nThese strings have been replaced:\n')
	#
	strCount = 1
	rplStrCount = 0
	LR = Loop_Replacements
	for match in re.finditer(r'(?<!.)"(.*)"\s=\s"(.*)";\n', dot_strings):
		strName = match.groups()[0]
		strValue = match.groups()[1]
		current_string = str(string.text)
		#
		LR.replace(LR, current_string)
		#
		if(LR().exact_now == 0):
			# remove string
			dot_strings = re.sub(match, '', dot_strings, re.U+re.M)
			strCount += 1
			continue
		elif(args.verbose):
			# print('\n'+str(strCount)+'. '+string_name+'')
			print(f"[{strCount}]", LR().translation[0])
		# match.groups()[1] = strValue = LR().translation[0]
		strValue = LR().translation[0]
		#
		new_strings.write("\""+strName+"\" = \""+strValue+"\";\n")
		rplStrCount += 1
		if(args.verbose):
			print('\n'+str(strCount)+'. '+strValue+'')
		strCount += 1
	#end replacing strings
	imperfectlog.close()
	uncasedlog.close()
	Non_Exact_Log.close()
	#
	new_strings.close()
	#
	printSummary()
	# CLEANUP MEMORY
	re.purge()
	del dot_strings, strCount, new_strings, isStrings
	#
else: # if neither types of file
	print("\nERROR: '"+lang_file+"' is neither an .XML nor a .strings file.")
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
