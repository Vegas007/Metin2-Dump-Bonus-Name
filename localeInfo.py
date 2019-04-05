#1) Search for:
def GetLetterCloseImageName():
	return "season1/icon/scroll_close.tga"
#2) Add after:
import re
import uiToolTip
def FormatBonusNameString(affectType):
	''' Return name of bonus (string) by a specific affect type.
		param-ex: item.APPLY_RESIST_FIRE
		return-ex: 'Defence chance against shaman attacks'
	'''
	AFFECT_DICT = uiToolTip.ItemToolTip().AFFECT_DICT
	if affectType in AFFECT_DICT:
		return ' '.join(re.findall(pattern='[a-zA-Z]+', string=AFFECT_DICT[affectType](0), flags=0)) if affectType in AFFECT_DICT else 'UNKNOWN_TYPE'

	return 'UNKNOWN_TYPE'
	
def FormatBonusNameDict():
	''' Return a dict (key=int, value=string) with all bonuses from dictionary.
		param-ex: None
		return-ex: {61: 'Strong against Sura', 100: 'Power of Fire', 108: 'Sword Defence Break'}
	'''
	result = {}
	for affectType in uiToolTip.ItemToolTip().AFFECT_DICT.keys():
		result.update({affectType: FormatBonusNameByAffectType(affectType)})
	return result