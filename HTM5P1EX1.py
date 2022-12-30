class StringVar:
	@classmethod
	def set (cls, iStr):
		return iStr.upper()
	@classmethod
	def get (cls):
		return 'all work and no play makes Jack a dull boy'
s = StringVar
print(s.set('all work and no play makes Jack a dull boy'))
print(s.get())