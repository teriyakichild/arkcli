"""ark-cli

Usage:
  ark-cli servers <query>
  ark-cli players <server>
  ark-cli (-h | --help)
  ark-cli --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
__version__ = '0.0.1'
import re

from docopt import docopt
from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from tabulate import tabulate
import sys

def get_web_driver(url):
    try:
        driver = webdriver.PhantomJS()
    except Exception as e:
        if 'Unable to start phantomjs with ghostdriver.' in str(e):
            print 'FATAL: PhantomJS is not installed.  Install with "sudo npm -g install phantomjs"'
            exit(1)
        else:
            print e
            exit()
    driver.get(url)
    return driver

def fetch_servers(query):
    driver = get_web_driver('https://arkservers.net/1/search/?term={0}'.format(query))
    servers_element = driver.find_element_by_id('servers_list').get_attribute('innerHTML')
    rank = driver.find_element_by_class_name('grav_srv_rank').get_attribute('innerHTML')
    driver.close()
    driver.quit()
    soup = BeautifulSoup(servers_element)
    strings = [str(value).strip() for value in soup.findAll(text=True) if str(value).strip() != '']
    lists = {}
    keys = ['ids', 'names', 'garbage', 'ips', 'likes', 'maps', 'players']
    for i, key in enumerate(keys):
        lists[key] = [unicode(each, 'utf-8') for each in strings[::7]]
        del strings[0]
    servers = zip(lists['ids'], lists['names'], lists['ips'], lists['likes'], lists['maps'], lists['players'])
    del servers[-1]
    return servers

def fetch_players(server):
    driver = get_web_driver('http://arkservers.net/server/{0}'.format(server))
    players_element = driver.find_element_by_id('server_players').get_attribute('innerHTML')
    driver.close()
    driver.quit()
    soup = BeautifulSoup(players_element)
    players = []
    for row in soup('tr'):
        if 'There are no players online on this server.' in str(row):
            break
        user = row('th')[0].text.encode('utf-8').decode('utf-8','ignore')
        status = row('td')[0].text.encode('utf-8').decode('utf-8','ignore')
        players.append([user, status])
    return players

def generate_table(items, headers, tablefmt='orgtbl'):
    return tabulate(items, headers=headers, tablefmt=tablefmt)

def main():
    arguments = docopt(__doc__, version='ark-cli {0}'.format(__version__))
    if arguments['servers']:
        servers = fetch_servers(arguments['<query>'])
        print generate_table(servers, ['ID', 'Name', 'IP', 'Upvotes', 'Map', 'Players Online'])
    if arguments['players']:
        players = fetch_players(arguments['<server>'])
        print generate_table(players, ['User', 'Status'])

if __name__ == '__main__':
    main()
