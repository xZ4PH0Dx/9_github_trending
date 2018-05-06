import requests
from datetime import date, timedelta


def get_maxstars_items(url, days_to_substract=7, items_per_page=20):
    begin_date = date.today() - timedelta(days_to_substract)
    payload = ('q=language:python+created:>{}'
               '&per_page={}&sort=stars&order=desc'
               .format(begin_date, items_per_page))
    return requests.get(url, params=payload).json()['items']


def get_repo_stats(maxstars_items):
    return (maxstars_items['html_url'],
            maxstars_items['stargazers_count'],
            maxstars_items['open_issues_count']
            )


if __name__ == '__main__':
    url = 'https://api.github.com/search/repositories'
    maxstars_items_list = get_maxstars_items(url)
    print('A list of new github repos with max stargazers count:\n')
    for maxstars_item in maxstars_items_list:
        html_url, stargazers, open_issues = get_repo_stats(maxstars_item)
        print(html_url, 'stars:', stargazers, 'issues:', open_issues)
