from catcher import string_vorovalka, title_vorovalka
from bs4 import BeautifulSoup
import requests

def bfs(start_url, finish_url="https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D1%82%D0%BB%D0%B5%D1%80,_%D0%90%D0%B4%D0%BE%D0%BB%D1%8C%D1%84"):
	queue = [[start_url]]
	used = set()
	while len(queue) > 0:
		x = queue.pop(0)
		if x[-1] not in used:
			used.add(x[-1])
			li = string_vorovalka(x[-1])
			if finish_url in li:
				return x + [finish_url]
			queue+=[x+[i] for i in li]
	return None

def main():
	url = input("Введите ссылку: ")
	url_f = input("Введите финальную ссылку(не обязательно): ")
	if url_f:
		path = bfs(url, url_f)
	else:
		path = bfs(url)
	if bfs != None:
		for i in path:
			print(title_vorovalka(i))
	else:
		print("sorry")

if __name__ == "__main__":
	main()
