class Checker:
	@staticmethod
	def check(new,old):
		if new[:5] == old[:5]:
			return True
			 
		else:
			return False
	
	@staticmethod
	def diff(new, old):

		result = []
		for i in range(min(5, len(new))):
			if not new[i] in old:
				result.append(new[i])

		return result