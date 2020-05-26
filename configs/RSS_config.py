header = {'User-Agent' :'Mozilla/5.0'} # (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}
RSS_list = [
    {
        'title': 'Zaufana Trzecia Strona',
        'rss_url': 'https://zaufanatrzeciastrona.pl/feed/',
        'overwrite_pubdate': False,
        'date_fmt': '%a, %d %B %Y %H:%M:%S +0000'
    },
    {
        'title': 'Business Insider',
        'rss_url': 'https://businessinsider.com.pl/.feed',
        'overwrite_pubdate': False,
        'date_fmt': '%Y-%m-%dT%H:%M:%S.%fZ'
    },
    {
        'title': 'Rzeczpospolita',
        'rss_url': 'https://www.rp.pl/rss/1019',
        'overwrite_pubdate': False,
        'date_fmt': ' %a, %d %B %Y %H:%M:%S +0300'
    },
    {
        'title': 'Transport Publiczny',
        'rss_url': 'https://www.transport-publiczny.pl/rss/rss.xml',
        'overwrite_pubdate': ['div',{'class': 'wiadData'}],
        'date_fmt': '%Y%m%d%H%M'
    },
    {
        'title': 'Rynek Kolejowy',
        'rss_url': 'https://www.rynek-kolejowy.pl/rss/rss.xml',
        'overwrite_pubdate': ['div',{'class': 'wiadSzczegol'}],
        'date_fmt': '%d%m%Y'
    },
    {
        'title': 'Rynek Lotniczy',
        'rss_url': 'https://www.rynek-lotniczy.pl/rss/rss.xml',
        'overwrite_pubdate': ['div',{'class': 'wiadData'}],
        'date_fmt': '%Y%m%d%H%M'
    },
    {
        'title': 'Rynek Infrastruktury',
        'rss_url': 'http://www.rynekinfrastruktury.pl/rss/rss.xml',
        'overwrite_pubdate': ['div',{'class': 'wiadSzczegol'}],
        'date_fmt': '%d%m%Y'
    }
]

