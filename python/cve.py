#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Nist crawler to get the base score of a CVE.
Python: 3.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Crawler:
    """ Class to get web pages information.
    """

    def _get_bs_html(self, url = None):
        """ Retrieve the HTML of the page.
        :param url: str, url to analyze and get information.
        :return bs: BeautifulSoup object obtained with the HTML.
                False: bool in case of error.
        """
        try:
            html = urlopen(url)
            bs = BeautifulSoup(html.read(), 'html.parser')
            return bs
        except Exception as e:
            print(e)
            return False

class Nist:
    """ Class to work with Nist web page.
    :att base_score: str, text with the base score 3 of the CVE.
                     bool (False) if no value retrieved.
    :att cve: str, CVE to search its base score.
    :att TAG: tag used at the HTML for the text with the CVE.
    :att TAG_ATT: str, attribute of the tag with the CVE.
    :att TAG_ATT_VALUE: str, value of the attribute of the HTML
                        tag with the CVE.
    :att URL: str, Nist URL to check a CVE, the CVE must be added to 
              the end of the string. I.e. URL + 'CVE-2019-5878'.
    """
    TAG             = 'a'
    TAG_ATT         = 'data-testid'
    TAG_ATT_VALUE   = 'vuln-cvss3-panel-score'
    URL             = 'https://nvd.nist.gov/vuln/detail/'

    def __init__(self, cve = None):
        """
        :param cve: str, CVE to search.
        """
        self.cve        = cve
        self.base_score = self._get_base_score()

    def __str__(self):
        # self.cve can have the value None and self.base_score the
        # boolean value False.
        return str(self.cve) + ': ' + str(self.base_score)

    def __repr__(self):
        # self.cve can have the value None.
        return "Nist(cve = '" + str(self.cve) + "')"

    def _get_base_score(self):
        """ Get the Nist base score 3 for a CVE.
        :param None.
        :return base score: str, Nist base score 3 value.
                False: bool, no result retrieved.
        """
        bs = Crawler()._get_bs_html(self.URL + self.cve)
        if bs:
            return bs.find(self.TAG,
                           {self.TAG_ATT: self.TAG_ATT_VALUE}).text
        return False

if __name__ == '__main__': 
    print(Nist(cve = 'CVE-2019-5878'))
