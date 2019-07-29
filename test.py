headers = {
    'Accept':         'text/plain',
    'Content-Length': 348,
    'Host':           'http://mingrammer.com'
}


def pre_process(headers):
    """
    I preprocess the headers you give me
    :param headers: http compatible headers
    :return: I don't return anything
    """
    content_length = headers['Content-Length']
    print('content length: ', content_length)

    host = headers['Host']
    if 'https' not in host:
        raise ValueError('You must use SSL for http communication')


pre_process(headers)