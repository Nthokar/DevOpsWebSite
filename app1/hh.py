import requests

URL = f'https://api.hh.ru/vacancies?text=<name>&per_page=100&period=10'
names = [
    'devops',
    'development operations',
    'ci/cd',
]


def get_vacancies(url: str, name: str):
    """

    :param name:
    :type url: object
    """
    url = url.replace('<name>', name)
    try:
        some_object_iterator = iter(name)
    except TypeError as te:
        response = requests.get(url=url).json()
        return response
    else:
        response = requests.get(url=url).json()
        return response['items']


def get_last_vacancies(url: str = URL, name: str = 'devops', n=10):
    vacancies = get_vacancies(url, name)
    vacancies = list(sorted(vacancies, key=lambda vacancy: vacancy['published_at'], reverse=True))[:10]
    vacancies_full = []
    for vacancy in vacancies:
        vacancies_full.append(get_vacancy(vacancy))
    return vacancies_full


def get_vacancy(vacancy):
    vacancy_id = vacancy['id']
    return requests.get(url=f'https://api.hh.ru/vacancies/{vacancy_id}').json()
