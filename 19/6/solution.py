class Object:
	def __init__(self, Name, Prev=None, Next=None):
		self.Name = Name
		self.Prev = Prev
		self.Next = Next
	
	def getPrev(self):
		return self.Prev
	
	def getNext(self):
		return self.Next

	def getObject(self, Name):
		if self.Next.Name == Name:
			return self.Next
		else:
			return getObject(self.Next, Name)

class Base(Object):
	def __init__(self, Name):
		super().__init__(Name, False)
	
	def addObject(self, Name

with open('input') as f:
	orbit_map = f.read().strip('\n').split('\n')


