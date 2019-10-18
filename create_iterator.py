class CreateIterator:
	@classmethod
	def create(cls,xs,ys):
		def iterator():
			for y in ys:
				for x in xs:
					yield x,y
		return iterator