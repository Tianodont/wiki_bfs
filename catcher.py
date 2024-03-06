from bs4 import BeautifulSoup
import requests

def string_vorovalka(url):
    res = requests.get(url).text
    soup = BeautifulSoup(res, "html.parser").find(class_='mw-content-ltr mw-parser-output')
    result = set(["https://ru.wikipedia.org"+i["href"] for i in soup.find_all("a") if not i.has_attr("class") and '"/wiki/' in str(i) and i.text!=" "])
    return result

def title_vorovalka(url):
    res = requests.get(url).text
    tit_soup = BeautifulSoup(res, "html.parser").find(class_='mw-page-title-main')
    return tit_soup.text

if __name__ == "__main__":
    test_url = input()
    print("links:")
    print(string_vorovalka(test_url))