from functools import reduce
def getLower( input):
	#: Map
	d = {
	"Ş":"ş", "I":"ı", "Ü":"ü", "Ç":"ç", "Ö":"ö", "Ğ":"ğ", 
	"İ":"i", "Â":"â", "Î":"î", "Û":"û"
	}
	#: Replace
	input = reduce(lambda x, y: x.replace(y, d[y]), d, input)
	input = input.lower()
	#: Return
	return input