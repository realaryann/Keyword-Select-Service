import yaml

class Words:
	words = []
	def __init__(self):
		with open("/home/csrobot/vosktest/src/listener/dict/dict.yaml", 'r') as f:
			self.words = yaml.load(f, Loader=yaml.SafeLoader)
	def add(self, word: str) -> None:
		self.words.append(word)
	def get(self) -> list():
		return self.words 

def main():
	pass

if __name__ == "__main__":
	main()