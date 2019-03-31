#!/usr/bin/python
from crawl import *

def main():
	hefei_url = "https://hf.58.com/pinpaigongyu/pn/{page}/?minprice=1500_2000"
	rent_spider = Spider("rent.csv",hefei_url)
	rent_spider.crawl()
	
if __name__ == "__main__":
	main()