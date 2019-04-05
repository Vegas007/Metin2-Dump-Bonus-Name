# Metin2-Dump-Bonus-Name
Get bonus name from tooltip affect dictionary as string, ignore the %value% and function SA, SNA etc.

```python
import localeInfo
import item

# FormatBonusNameString
print localeInfo.FormatBonusNameString(item.APPLY_RESIST_SWORD)

# FormatBonusNameDict
for bonusIndex, bonusName in localeInfo.FormatBonusNameString().iteritems():
	print '{:d}: {:s}'.format(bonusIndex, bonusName)
```
