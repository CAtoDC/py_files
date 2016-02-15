import os

BASE_URL = 'http://api.open.fec.gov/v1'

API_KEY = open(os.path.expanduser('c:/py/data/api-keys/data_gov.txt'),'r').read().strip()


def all_results(endpoint, params):
    _params = deepcopy(params)
    _params.update({'api_key': API_KEY})
    _url = BASE_URL+endpoint
    logging.info('querying endpoint: {}'.format(_url))

    initial_resp = requests.get(_url, params=_params)

    logging.debug('full url eg: {}'.format(initial_resp.url))

    initial_data = initial_resp.json()

    num_pages = initial_data['pagination']['pages']
    num_records = initial_data['pagination']['count']
    logging.info('{p} pages to be retrieved, with {n} records'.format(
            p=num_pages, n=num_records))

    current_page = initial_data['pagination']['page']
    logging.debug('page {} retrieved'.format(current_page))

    for record in initial_data['results']:
        yield record

    while current_page < num_pages:
        current_page += 1
        _params.update({'page': current_page})
        _data = requests.get(_url, params=_params).json()
        logging.debug('page {} retrieved'.format(current_page))
        for record in _data['results']:
            yield record

    logging.info('all pages retrieved')


def count_results(endpoint, params):
    _params = deepcopy(params)
    _params.update({'api_key': API_KEY})
    _url = BASE_URL+endpoint

    _data = requests.get(_url, params=_params).json()

    return _data['pagination']['count']
