import urllib.request
import re
import datetime

def save_csv_yahoo_indic(symbol='IXIC'):
    stime = datetime.datetime.now()
    etime = datetime.datetime.now() - datetime.timedelta(days=365)
    print(stime, etime)

    ustime = int(stime.timestamp())
    uetime = int(etime.timestamp())
    print(ustime, uetime)

    furl = 'https://query1.finance.yahoo.com/v7/finance/download/%%5E%s?period1=%s&period2=%s&interval=1d&events=history'

    print(furl%(symbol, uetime, ustime))

    with urllib.request.urlopen(furl%(symbol, uetime, ustime)) as response:
        html = response.read()
        with open(symbol + '.csv', 'wb') as save_file:
            save_file.write(html)


def save_csv_m2():
    furl = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%%23e1e9f0&chart_type=line&drp=0&fo=open%%20sans&graph_bgcolor=%%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=M2&scale=left&cosd=1980-11-03&coed=%s&line_color=%%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Weekly%%2C%%20Ending%%20Monday&fam=avg&fgst=lin&fgsnd=%s&line_index=1&transformation=lin&vintage_date=%s&revision_date=%s&nd=1980-11-03'
    tdy = datetime.datetime.today().strftime('%Y-%m-%d')
    url = furl%(tdy,tdy,tdy,tdy)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        with open('M2.csv', 'wb') as save_file:
            save_file.write(html)

if __name__ == "__main__":
    import time
    save_csv_yahoo_indic('IXIC')
    time.sleep(2)
    save_csv_yahoo_indic('GSPC')
    time.sleep(2)
    save_csv_yahoo_indic('RUT')
    time.sleep(2)
    save_csv_m2()