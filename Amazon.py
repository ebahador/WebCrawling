# Getting price and reviews regarding the specific product
from bs4 import BeautifulSoup
import requests


def getReviews(session, link):
    session.headers['User-Agent'] = 'Mozilla/5.0'
    response = session.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find_all('div', {'data-hook': 'review-collapsed'})


def getPrice(session, link):
    session.headers['User-Agent'] = 'Mozilla/5.0'
    response = session.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find_all('td', {'class': 'a-span12'})


def getRate(session, link):
    session.headers['User-Agent'] = 'Mozilla/5.0'
    response = session.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find_all('span', {'id': 'acrPopover'})


# Main method
if __name__ == '__main__':
    FLAG = True
    checking = 'https://www.amazon.com/'
    while FLAG:
        link = input('Please put your Amazon link here: ')
        if checking in link:
            FLAG = False
        else:
            print('Your website either is not Amazon or has not observed "HTTPS" legislation.')
    with requests.Session() as session:
        for price in getPrice(session, link):
            print(f'{price.text}\n', end='')
        print('*' * 50)
        for rates in getRate(session, link):
            print(f'{rates.text}\n', end='')
        print('*' * 50)
        for reviews in getReviews(session, link):
            print(f'{reviews.text}\n')
