import urllib2
from bs4 import BeautifulSoup

price=raw_input("Amount: ")
input_curr=raw_input("From: ")
output_curr=raw_input("To: ")
page="http://www.xe.com/currencyconverter/convert/?Amount="+price+"=&From="+input_curr+"&To="+output_curr
converter=urllib2.urlopen(page)
soup=BeautifulSoup(converter,'html.parser')
extract=soup.find('span',attrs={'class':'uccResultAmount'})
money=extract.text.strip()
print(money)