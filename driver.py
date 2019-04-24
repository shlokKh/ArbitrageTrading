from requests_html import HTMLSession
from graph import graph

session = HTMLSession()
currency = graph(5)

bases = ['USD', 'EUR', 'NZD', 'GBP', 'AUD']

for i in range(len(bases)):
    for j in range(len(bases)):
        if i == j:
            currency.add_edge(i, j, 1)
        else:
            print(bases[i]+bases[j])
            r = session.get('https://www.google.com/search?q='+ bases[i]+'+to+'+bases[j])
            info = r.html.find('.DFlfde')
            print(len(info))
            exchange = float(info[1].attrs['data-value'])
            currency.add_edge(i, j, exchange)

currency.print_matrix()