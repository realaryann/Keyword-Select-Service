from . import dictionary

def clean_text(text: str) -> str:
	cleantxt = ''
	for x in text:
		if x.isalpha():
			cleantxt=cleantxt+x
		if x == '\n':
			cleantxt=cleantxt+' '
		if x == ' ':
			cleantxt=cleantxt+' '
	return cleantxt

def get_text() -> str:
	with open("/home/csrobot/vosktest/input_saver/results/test.txt", 'r') as f:
		text: str = f.read()
		if not len(text):
			print("INFO: Please transcribe some audio first")
			return None
		return text

def match(split: list[str] , goal: list[str]) -> list[str]:
	res = []
	for x in split:
		if x in goal:
			res.append(x)
	return res

def main():
	pass

if __name__ == "__main__":
	main()