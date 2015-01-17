import urllib, time, os, re, csv
import pandas
from timeit import timeit

STOCKSTOTICK = [ 'GOOG',
                 'APPL',
                 'STI',
                 'HD',
                 'RGC',
                 'ABBV',
                 'JNJ',
                 'DEPO',
                 'CRRC',
                 'INTC',
                 'SLB',
                 'IESC',
                 'CAT']

os.environ['TZ'] = 'America/New_York'
time.tzset()
t = time.localtime()

print(time.time())
print(time.ctime()+ " NY STOCK EXC TIME")

def financefetch(googleticker):
    url = "http://www.google.com/finance?&q="
    txt = urllib.urlopen(url+googleticker).read()
    t = time.time()
    localtime = time.localtime()
    k = re.search('id="ref_(.*?)">(.*?)<',txt)
    if k:
        tmp = k.group(2)
        q = tmp.replace(',','')
        x = re.search('value="(.*?):{0}"'.format(googleticker),txt)
        x = x.group(1)
    else:
        q = "Nothing found for: "+googleticker
        x = "Unknown"
    return q, x, t , localtime

class TickerDataFrame(object):
    def __init__(self, ticker ):
        self.ticker = ticker
        self.stockdataframe = pandas.DataFrame(columns = ('Time', 'Price'))
        self.tickertype = None


    def tickerdata(self):


#df.loc[len(df)+1]=['8/19/2014','Jun','Fly','98765']

#print financefetch('GOOG')

#def _data_dict(ticker):


for x in range(10000):
    start_time = time.time()
    financefetch('GOOG')
    print "took", time.time()-start_time, "to run"


def add_to_masterdata(ticker):
    quote = financefetch(googleticker)






