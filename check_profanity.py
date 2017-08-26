from urllib.request import urlopen
import urllib
import urllib.request
def read_text():
    quotes=open(r"C:\Users\sdadh\Desktop\Comp_Coding\Python\quotes.txt")
    contents_of_files=quotes.read()
    print(contents_of_files)
    quotes.close()
    check_profanity(contents_of_files)

def check_profanity(content):
    connection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+"conten")
    output=connection.read()

    if (output=="true"):
        print("Profanity Alert")
    else:
        print("shit")

read_text()
