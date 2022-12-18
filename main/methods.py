from bs4 import BeautifulSoup
import requests

search = 'https://www.rottentomatoes.com/search?search='


def search_film(name):
    page = requests.get(search + name)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    onlyMoves = soup.find('search-page-result', type="movie")
    scraped = []

    if onlyMoves is None:
        scraped.append(['er', 'er', 'er', 'er'])
    else:
        movies = onlyMoves.findAll('search-page-media-row')
        for move in movies:
            year = move['releaseyear']
            link = move.a['href']
            names = move.findAll('a', class_='unset')
            cast = move['cast']
            scraped.append([names[1].text.strip(), year, link, cast])

    return scraped


def search_full(url):
    global director
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    moviesGenre = soup.find('p', class_='scoreboard__info')
    cons = soup.find('p', class_='what-to-know__section-body')
    dirs = soup.findAll('li', class_='meta-row clearfix')
    moviesRateA = soup.find('score-board')['audiencescore']
    moviesRateK = soup.find('score-board')['tomatometerscore']

    scraped = []

    if moviesGenre is not None:
        scraped.append(moviesGenre.text)
    else:
        scraped.append('Отсутствует информация')
    if moviesRateA != '':
        scraped.append(moviesRateA)
    else:
        scraped.append('Отсутствует информация')
    if moviesRateK != '':
        scraped.append(moviesRateK)
    else:
        scraped.append('Отсутствует информация')
    if cons is not None:
        scraped.append(cons.text)
    else:
        scraped.append('Отсутствует информация')
    if dirs is not None:
        for dir in dirs:
            if dir.text.__contains__('Director'):
                director = dir.text.strip()
                director = director.replace("\n", "")
                director = director.replace("\r", "")
                director = director.replace("Director:", "")
        scraped.append(director)
    else:
        scraped.append('Отсутствует информация')

    return scraped


def search_actors(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    actors = soup.findAll('div', class_='cast-item media inlineBlock')
    scraped = []
    ss = ''

    for actor in actors:
        act = actor.find('div', class_='media-body').a
        if act is not None:
            scraped.append(act)
            ss += str(act.text) + " "

    if ss == '':
        ss = 'Отсутствует информация'

    ss = ss.replace("\r", "")
    ss = ss.replace("\n", "")
    return ss.strip()


def search_pic(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    movies3 = soup.find('img', class_='posterImage')['src']

    if movies3 == '/assets/pizza-pie/images/poster_default.c8c896e70c3.gif':
        movies3 = 'Постер отсутствует'

    return movies3
