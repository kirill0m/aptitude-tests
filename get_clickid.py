from urllib.parse import urlparse


def get_query_pars(url_str: str) -> dict | None:
    query = urlparse(url_str).query
    # query = url_str.split('?')[-1]

    if not query:
        raise Exception('no queries found in url')

    return dict([p.split('=') for p in query.split('&')])


if __name__ == '__main__':
    url = 'https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE'
    parsed_url = get_query_pars(url)
    print(parsed_url.get('clickid'))
