from . import dictionary

def clean_text(text: str) -> str:
	cleantxt: str = ''
	for x in text:
		if x.isalpha():
			cleantxt=cleantxt+x
		if x == '\n':
			cleantxt=cleantxt+' '
		if x == ' ':
			cleantxt=cleantxt+' '
	return cleantxt

def match(split: list[str] , goal: list[str]) -> list[str]:
	res: list = []
	for x in split:
		if x in goal:
			res.append(x)
	return res

def main():
	pass

if __name__ == "__main__":
	main()