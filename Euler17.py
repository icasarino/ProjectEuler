def n2wlen(argument):
    return {
    	0 : len(""),
		1 : len("one"),
		2 : len("two"),
		3 : len("three"),
		4 : len("four"),
		5 : len("five"),
		6 : len("six"),
		7 : len("seven"),
		8 : len("eight"),
		9 : len("nine"),
		10 : len("ten"),
		11 : len("eleven"),
		12 : len("twelve"),
		13 : len("thirteen"),
		14 : len("fourteen"),
		15 : len("fifteen"),
		16 : len("sixteen"),
		17 : len("seventeen"),
		18 : len("eighteen"),
		19 : len("nineteen"),
		20 : len("twenty"),
		30 : len("thirty"),
		40 : len("forty"),
		50 : len("fifty"),
		60 : len("sixty"),
		70 : len("seventy"),
		80 : len("eighty"),
		90 : len("ninety"),
		100 : len("hundred"),
		1000 : len("onethousand"),
		9999 : len("and")
    }[argument]

def getUnit(value):
	return value - int(value / 10) * 10
def getTens(value):
	return int(value / 10)
def getHund(value):
	return int(value / 100)


res = 0
i = 1
maxx = 1000
while i <= maxx:

	if 1 <= i <= 20 or i == 1000:
		res += n2wlen(i)
	elif 20 < i <= 99:
		tens = int(getTens(i)) * 10
		unit = int(getUnit(i))
		res += n2wlen(tens) + n2wlen(unit)
	else:
		hund = int(getHund(i))
		tens = int(getUnit(getTens(i))) * 10
		unit = int(getUnit(i))
		res += n2wlen(hund) + n2wlen(100) + n2wlen(tens) + n2wlen(unit)
		
		if i % 100 != 0:
			res += n2wlen(9999)
	i += 1

print(res)

"""
i = 941
hund = int(getHund(i))
tens = int(getUnit(getTens(i))) * 10
unit = int(getUnit(i))

print(hund)
print(tens)
print(unit)
print("mod ", i % 100)




res = 0
i = 100
maxx = 999
while i <= maxx:
	if i < 21 or i == 1000:
		res += n2wlen(i)
	elif i <= 99:	
		tens = getTens(i)
		unit = getUnit(i)
		res += n2wlen(tens) + n2wlen(unit)
	elif i <= 999:
		hund = int(getHund(i) / 100)
		tens = tens = int(getUnit(getTens(i) / 10)) * 10
		unit = int(getUnit(i))
		res += n2wlen(hund) + n2wlen(100) + n2wlen(tens) + n2wlen(unit) 

		if i % 100 != 0:
			res += n2wlen(9999)
	i += 1

print(res)"""