def parse(query: str) -> dict:

    result_dict = {}
    divided_url = query.split('?')

    if len(divided_url) > 1:

        divided_attributes = divided_url[1].split('&')

        for el in divided_attributes:
            if len(el) > 0:
                pairs_of_dictionary = el.split('=')
                result_dict[pairs_of_dictionary[0]] = pairs_of_dictionary[1]

    return result_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://www.aliexpress.com/?spm=a2g0o.detail.1000') == {'spm': 'a2g0o.detail.1000'}
    assert parse('https://www.google.com/search?q=split+python&oq=&aqs=chrome') == {'q': 'split+python', 'oq': '', 'aqs': 'chrome'}
    assert parse('https://www.work.ua/jobs-odesa-it/?advs=1') == {'advs': '1'}
    assert parse('https://www.work.ua/jobs-odesa/?advs=1&category=22+1') == {'advs': '1', 'category': '22+1'}
    assert parse('https://translate.google.com/?sl=en&tl=ru&text=Step%202%20of%202') == {'sl': 'en', 'tl': 'ru', 'text': 'Step%202%20of%202'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
