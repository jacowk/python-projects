import bs4
import os

class ScrapLengths:

    def __init__(self, soup):
        self.soup = soup

    def print_divider(self):
        print("-" * 10)

    def scrap(self):
        # http://omz-software.com/editorial/docs/ios/beautifulsoup_ref.html
        div_headings = self.soup.findAll("div", "vheading")
        for div_heading in div_headings:
            if div_heading.text.strip() == "Lengths":
                print(type(div_heading))
                next_sibling = div_heading.findNextSibling()
                print(type(next_sibling))
                print(next_sibling.name)
                help(next_sibling)
