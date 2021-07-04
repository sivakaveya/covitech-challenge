import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self, name, price, url, image):
        self.name = name
        self.price = price
        self.url = url
        self.image = image

    def __str__(self):
        return self.name + '<br/> ' + str(self.price) + '<br/> ' + self.url + '<br/>' + self.image


def cleanint(dirtyint):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    clean_string = ''
    for clean in dirtyint:
        if clean in digits:
            clean_string += clean
    if '.' in clean_string:
        return float(clean_string)
    return int(clean_string)

def amazon1(product):
    URL = "https://www.amazon.in/s?k=" + product
    while True:
        page = requests.get(URL)
        if page.status_code == 200:
            break
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('div', attrs={'class': 'a-section a-spacing-medium'})
    items = []

    for result in results:
        name = result.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
        price = result.find('span', attrs={'class': 'a-price-whole'})
        url = result.find('a', attrs={'class': 'a-link-normal a-text-normal'})
        image = result.find('img', attrs={'class': 's-image'})
        if name and price and url and image:
            name = name.text
            price = cleanint(price.text)
            url = "https://www.amazon.in" + url.attrs['href']
            image = image.attrs['src']
            items.append(Item(name, price, url, image))
    
    return sorted(items, key=lambda x: x.price)

def amazon2(product):
    URL = "https://www.amazon.in/s?k=" + product
    while True:
        page = requests.get(URL)
        if page.status_code == 200:
            break
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('div', attrs={'class': 'a-section a-spacing-medium'})
    items = []

    for result in results:
        name = result.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
        price = result.find('span', attrs={'class': 'a-price-whole'})
        url = result.find('a', attrs={'class': 'a-size-base a-link-normal a-text-normal'})
        image = result.find('img', attrs={'class': 's-image'})
        if name and price and url and image:
            name = name.text
            price = cleanint(price.text)
            url = url.attrs['href']
            url = "https://www.amazon.in" + url
            image = image.attrs['src']
            items.append(Item(name, price, url, image))

    return sorted(items, key=lambda x: x.price)

def flipkart1(product):
    URL = "https://www.flipkart.com/search?q=" + product
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('div', attrs={'class': '_2kHMtA'})
    items = []

    for result in results:
        name = result.find('div', attrs={'class': '_4rR01T'})
        price = result.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        url = result.find('a', attrs={'class': '_1fQZEK'})
        image = result.find('div', attrs={'class': 'CXW8mj'})
        if name and price and url and image:
            image = image.contents[0].attrs['src']
            price = cleanint(price.text)
            url = "https://www.flipkart.com" + url.attrs['href']
            items.append(Item(name.text, price, url, image))

    return sorted(items, key=lambda x: x.price)


def flipkart2(product):
    URL = "https://www.flipkart.com/search?q=" + product
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('div', attrs={'class': '_4ddWXP'})
    items = []

    for result in results:
        name = result.find('a', attrs={'class': 's1Q9rs'})
        price = result.find('div', attrs={'class': '_30jeq3'})
        image = result.find('div', attrs={'class': 'CXW8mj'})
        if name and price and image:
            image = image.contents[0].attrs['src']
            price = cleanint(price.text)
            url = "https://www.flipkart.com" + name.attrs['href']
            items.append(Item(name.text, price, url, image))

    return sorted(items, key=lambda x: x.price)

def paytmmall(product):
    URL = "https://paytmmall.com/shop/search?q=" + product
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('div', attrs={'class': '_3WhJ'})
    items = []

    for result in results:
        name = result.find('div', attrs={'class': 'UGUy'})
        price = result.find('span').contents[1]
        url = result.contents[0].__dict__
        url = url['attrs']['href']
        image = result.find('div', attrs={'class': '_3nWP'})
        if name and price and image:
            image = image.contents[0].attrs['src']
            price = cleanint(price)
            url = "https://www.paytmmall.com" + url
            items.append(Item(name.text, price, url, image))

    return sorted(items, key=lambda x: x.price)

def pharmeasy(product):
    URL = "https://pharmeasy.in/search/all?name=" + product
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('div', attrs={'class': '_1jald'})
    items = []

    for result in results:
        name = result.find('h1', attrs={'class': 'ooufh'})
        price = result.find('div', attrs={'class': '_1_yM9'})
        url = result.find('a', attrs={'class': '_3o0NT _1NxW8 iJm6I'})
        if name and price and url:
            price = cleanint(price.text)
            url = "https://www.pharmeasy.in" + url['href']
            image = "default image"
            items.append(Item(name.text, price, url, image))

    return sorted(items, key=lambda x: x.price)

def scrapall(product):
    items = []
    websites = [amazon1, amazon2, flipkart1, flipkart2, paytmmall, pharmeasy]
    for website in websites:
        items += website(product)
    return sorted(items, key=lambda x: x.price)