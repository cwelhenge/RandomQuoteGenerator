import requests
from bs4 import BeautifulSoup
from random import randrange


class RandomQuoteGenerator:
    """
        Description: Generate random quotes from http://quotes.toscrape.com/ by web scraping
    """

    def __init__(self):
        self.main_screen()
        while choice == 1:
            self.generate_quote()
            choice = self.main_screen()

    '''
    description: Prints the main screen options
    param: none
    return: main menu option number
    '''

    def main_screen(self):
        print('Welcome to Random Quote Generator!\n')
        print('1. Generate a random quote')
        print('2. Exit')
        print()
        value = int(input("Please enter the number of the option: "))
        while value not in [1, 2]:
            value = int(input("Invalid number, please enter the number of option: "))
        print()
        return value

    '''
    description: Prints a random quote from http://quotes.toscrape.com/
    param: none
    return: none
    '''

    def generate_quote(self):

        # Find the total amount of pages
        page = 0
        end = False
        while not end:
            page += 1
            url = 'http://quotes.toscrape.com/page/' + str(page) + '/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            errorArray = soup.findAll('div', class_='col-md-8')
            # Check if the current page is the last page
            for item in errorArray:
                if 'No quotes found!' in item.text:
                    end = True

        # Find a random page
        randPage = randrange(page)
        url = 'http://quotes.toscrape.com/page/' + str(randPage) + '/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Find a random quote
        quotes = soup.findAll(class_='quote')
        randQuote = randrange(len(quotes))
        print(quotes[randQuote].find(class_='text').text + ' - ' +
              quotes[randQuote].find(class_='author').text + '\n')


def main():
    """
    Initializes random quote generator

    :return: None
    """
    RandomQuoteGenerator()


if __name__ == "__main__":
    main()
