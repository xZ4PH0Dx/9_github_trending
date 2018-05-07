import requests
from datetime import date, timedelta


def get_maxstars_repos(url, days_to_substract=7, top_repos=20):
    begin_date = date.today() - timedelta(days_to_substract)
    payload = {
        'sort': 'stars',
        'order': 'desc',
        'q': 'created:>{}'.format(begin_date)
            }
    return requests.get(url, params=payload).json()['items'][:top_repos]


def get_repo_stars(repo):
    return (
        repo['html_url'],
        repo['stargazers_count'],
            )


def get_count_issues(owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(owner, repo_name)
    return len(requests.get(url).json())


if __name__ == '__main__':
    repos_url = 'https://api.github.com/search/repositories'
    maxstars_repos_list = get_maxstars_repos(repos_url)
    print('A list of new github repos with max stargazers count:\n')
    for repo in maxstars_repos_list:
        html_url, stargazers = get_repo_stars(repo)
        owner, repo_name = repo['full_name'].split('/')
        open_issues = get_count_issues(owner, repo_name)
        print(html_url, 'stars:', stargazers, 'issues:', open_issues)
