#1) Search for:
def GetLetterCloseImageName():
	return "season1/icon/scroll_close.tga"
#2) Add after:
import re
import uiToolTip
def FormatBonusNameString(bonusIndex):
	''' Return name of bonus (string) by a specific bonus index.
		param-ex: item.APPLY_RESIST_FIRE
		return-ex: 'Fire Resistance'
	'''
	AFFECT_DICT = uiToolTip.ItemToolTip().AFFECT_DICT
	if bonusIndex in AFFECT_DICT:
		return ' '.join(re.findall(pattern='[a-zA-Z]+', string=AFFECT_DICT[bonusIndex](0), flags=0))
	return 'UNKNOWN_TYPE'
	
def FormatBonusNameDict():
	''' Return a dict (key=int, value=string) with all bonuses from dictionary.
		param-ex: None
		return-ex: {61: 'Strong against Sura', 100: 'Power of Fire', 108: 'Sword Defence Break'}
	'''
	result = {}
	for bonusIndex in uiToolTip.ItemToolTip().AFFECT_DICT.keys():
		result.update({bonusIndex: FormatBonusNameString(bonusIndex)})
	return result