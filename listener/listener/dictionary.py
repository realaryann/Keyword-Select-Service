import yaml

class Words:
	words: list = []
	def __init__(self, name):
		path = f"/home/csrobot/vosktest/src/hubo_voice_command/dict/{name}"
		with open(path, 'r') as f:
			self.words = yaml.load(f, Loader=yaml.SafeLoader)
	def add(self, word: str) -> None:
		self.words.append(word)
	def get(self) -> list:
		return self.words 

def main():
	pass

if __name__ == "__main__":
	main()