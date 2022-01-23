def Praselirl(uri):

req= requests.get(url, headers headers) soup => Beautiful Soup (req.content, 1xm1')

if last page is not None:

last_page soup.find(text='Next') page last page.find_previous('li').find_previous('li') page_url ('https://www.brainyquote.com return [page_url str(x) for x in range(1, int(page.text)+1)]

page.a['href'].split('&')[0]&pg=')

else:

return None

##requests each page, parse and return list of dictionary

def Parse(url,dato []):

req= requests.get(url, headers headers)

soup BeautifulSoup (req.content, 'Ixml')

quotes soup.find_all('div',attrs {'class': 'qll-bg"})

if quotes is not None: for x in quotes:

Quote x.find(title='view quote')

Author x.find(title='view author')

Tags x.find(class_ "kw-box')

parse_data { "Quote:Quote.text.strip() if Quote else**

*Author':Author.text.strip() if Author else" *Tags':Tags.text.strip().replace("\n",, ) if Tags else"

'QuoteUrl': 'https://www.brainyquote.com Quote['href'] if Quote else",

*AuthorUrl': 'https://www.brainyquote.com Author['href'] if Author else

} data.append(parse_data)

return data
