import re
import functools

LOCALE_GAME_TUPLE =\
(
	'TOOLTIP_ANTI_CRITICAL_PCT	Resistance against critical hits +%d%%	SAA',
	'TOOLTIP_APPLY_ATTBONUS_ORC	Strong against Orcs +%d%%	SAA',
	'TOOLTIP_APPLY_EXP_DOUBLE_BONUS	%d%% Chance for EXP Bonus	SAA',
	'TOOLTIP_ATT_GRADE	Attack Value +%d	SAA',
	'TOOLTIP_AFFECT_MOUNT_FALL	Fall from mount	SNAA',
	'TOOLTIP_APPLY_ENCHANT_EARTH	Power of Earth +%d%%	SAA',
	'TOOLTIP_APPLY_ENCHANT_DARK	Power of Darkness +%d%%	SAA',
)

def __LoadLocaleGameFile(localeDict):
	def SA(text):
		def f(x):
			return text % x
		return f
		
	def SNA(text):
		def f(x):
			return text
		return f

	for line in LOCALE_GAME_TUPLE:
		tokens = line[:-1].split('\t')
		localeDict[tokens[0]] = {2 : tokens[1], 3 : {'SA': SA, 'SNA': SNA}[tokens[2]](tokens[1])}[len(tokens)]

__LoadLocaleGameFile(locals())

def Print():
	'''
	functools.reduce:
		Apply function of two arguments cumulatively to the items of sequence, from left to right, so as to reduce the sequence to a single value;
	re.findall:
		Return all non-overlapping matches of pattern in string, as a list of strings; 
		The string is scanned left-to-right, and matches are returned in the order found;
		If one or more groups are present in the pattern, return a list of groups;
		This will be a list of tuples if the pattern has more than one group;
		Empty matches are included in the result;
		[a-zA-Z] - any single character in the range a-z or A-Z;
	eval:
		Parses the expression passed to this method and runs python expression (code) within the program.
	'''
	for line in LOCALE_GAME_TUPLE:
		try:
			print functools.reduce(lambda *args: '{0} {1}'.format(*args), re.findall(pattern='[a-zA-Z]+', string=eval(line.split('\t')[0])(0), flags=0))
		except (SyntaxError, NameError, TypeError, ZeroDivisionError):
			print SyntaxError
			
if __name__ == '__main__':
	Print()