rows = arcpy.UpdateCursor("shape1","")
translit =	{
  1040: "A",
  1041: "B",
  1042: "V",
  1043: "H",
  1044: "D",  
  1045: "E",
  1028: "Ye",
  1046: "Zh",
  1047: "Z",
  1048: "Y",
  1030: "I",
  1031: "Yi",
  1049: "Y",
  1050: "K",
  1051: "L",
  1052: "M", 
  1053: "N",
  1054: "O",
  1055: "P",
  1056: "R",  
  1057: "S",
  1058: "T",
  1059: "U",
  1060: "F",  
  1061: "Kh",
  1062: "Ts",
  1063: "Ch",  
  1064: "Sh",
  1065: "Shch", 
  1068: "'",  
  1070: "Yu",
  1071: "Ya", 
  1072: "a",
  1073: "b",
  1074: "v",
  1075: "h",
  1076: "d",
  1077: "e",
  1108: "ie",
  1078: "zh",
  1079: "z",
  1080: "y",
  1110: "i",
  1111: "i",
  1081: "i",
  1082: "k",
  1083: "l",
  1084: "m",
  1085: "n",
  1086: "o",
  1087: "p",
  1088: "r",  
  1089: "s",
  1090: "t",
  1091: "u",
  1092: "f",
  1093: "kh",
  1094: "ts",
  1095: "ch",
  1096: "sh",
  1097: "shch",   
  1100: "'",  
  1102: "iu",
  1103: "ia", 
  0:"[0]"
}
def dict(c):
	a = ord(c)
	if a in translit:
		return translit[a]
	return "[{}]".format(a)
def trans(st):
	res = ""
	for c in st:
		res = res + dict(c)
	return res
for row in rows:
	row.setValue("TextE", trans(row.getValue("TextU")))
	rows.updateRow(row)
