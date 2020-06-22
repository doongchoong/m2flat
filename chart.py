from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime


def gen_chart(indic='IXIC', ttyp='Compare'):
    csv_file = indic + '.csv.M2.csv'

    df = pd.read_csv('./' + csv_file)

    from_to = df.iloc[0]['Date'] + ' ~ ' + df.iloc[-1]['Date']
    print(from_to)

    tr1 = go.Candlestick(x=df['Date'],
                    open=df['Open_1'],
                    high=df['High_1'],
                    low=df['Low_1'],
                    close=df['Close_1'],
                    name='M2-Flat')

    tr2 = go.Scatter(x=df['Date'],
                    y=df['M2'],
                    name='M2',
                    yaxis='y2')

    tr3 = go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='original',
                    increasing_line_color= 'gray', decreasing_line_color= 'magenta')

    if ttyp == 'Compare':
        fig = make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(tr1)
        fig.add_trace(tr2, secondary_y=True)
        fig.add_trace(tr3)
    else:
        fig = make_subplots()
        fig.add_trace(tr1)

    ##
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        title_text=indic + ' ' + ttyp + ' (' + from_to + ')'
    )
    fig.layout.xaxis.type = 'category'
    fig.write_html(indic + ttyp + '.html', auto_open=False)


if __name__ == "__main__":
    import itertools

    indics = ['IXIC', 'GSPC', 'RUT']
    typs = ['Compare', 'M2_flat']

    for itm in itertools.product(indics, typs):
        print(itm)
        gen_chart(*itm)
    