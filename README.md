# Metin2-Dump-Bonus-Name
Get bonus name from tooltip affect dictionary as string, ignore the %value% and function SA, SNA etc.

Ignore the dump.txt & dump_test.py, is just to test how function works.
___
>Just follow tutorial from [localeInfo.py](https://github.com/Vegas007/Metin2-Dump-Bonus-Name/blob/master/localeInfo.py).

```python
import localeInfo
import item

# FormatBonusNameString
print localeInfo.FormatBonusNameString(item.APPLY_RESIST_SWORD)

# FormatBonusNameDict
for bonusIndex, bonusName in localeInfo.FormatBonusNameDict().iteritems():
	print '{:d}: {:s}'.format(bonusIndex, bonusName)
```
