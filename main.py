def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:

    result = {}
    divided_string_into_list = query.split(";")

    for el in divided_string_into_list:
        if len(el) > 0:
            pairs_of_dictionary = el.split("=", 1)
            result[pairs_of_dictionary[0]] = pairs_of_dictionary[1]

    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('user=Sam=age=15;id=3') == {'user': 'Sam=age=15', 'id': '3'}
    assert parse_cookie('id=1;number=8;name=Stiv') == {'id': '1', 'number': '8', 'name': 'Stiv'}
    assert parse_cookie(';;') == {}
    assert parse_cookie('item=phone=number=0000000;color=red;') == {'item': 'phone=number=0000000', 'color': 'red'}
    assert parse_cookie('1=1;2=3-1;') == {'1': '1', '2': '3-1'}
    assert parse_cookie('name=Ira;age=20') == {'name': 'Ira', 'age': '20'}
    assert parse_cookie(';name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
