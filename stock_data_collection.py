import pandas
from financefetch import financefetch

os.environ['TZ'] = 'America/New_York'
time.tzset()
t = time.localtime()

fname = '_{0}_{1}_{2}_data.csv'.format(t.tm_mon, t.tm_day, t.tm_year)

def store_to_file(ticker,t):
    with open(ticker + fname  , 'a') as f:
        while(t.tm_hour <= 16):
            if(t.tm_hour == 16):
                while(t.tm_min < 01):
                    data, group, epochtime, t = financefetch(ticker)
                    f.write('{0},{1}\n'.format(data,epochtime)
                    time.sleep(1)
            else:
                break
        else:
            data, group, epochtime, t = financefetch(ticker)
            f.write('{0},{1}\n'.format(data,epochtime))
            time.sleep(1)



