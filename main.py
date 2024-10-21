import os
import requests
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, url):
    api_url = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        'url': url,
        'access_token': token,
        'v': '5.199'
    }
    response = requests.post(api_url, data=payload)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response_data:
        error_message = response_data['error']['error_msg']
        raise ValueError(f"Ошибка от VK API: {error_message}")

    short_link = response_data['response']['short_url']
    return short_link


def count_clicks(token, short_url):
    api_url = 'https://api.vk.com/method/utils.getLinkStats'
    key = urlparse(short_url).path.lstrip('/')

    payload = {
        'key': key,
        'access_token': token,
        'v': '5.199',
        'interval': 'forever'
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response_data:
        raise ValueError(f"Ошибка от VK API: {response_data['error']['error_msg']}")

    stats = response_data['response'].get('stats', [])

    total_clicks = stats[0]['views']
    return total_clicks


def is_shorten_link(token, url):
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'vk.cc':
        return False

    key = parsed_url.path.lstrip('/')

    api_url = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'key': key,
        'access_token': token,
        'v': '5.199',
        'interval': 'forever'
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response_data:
        error_message = response_data['error']['error_msg']
        raise ValueError(f"Ошибка от VK API: {error_message}")
    else:
        return True


def main():
    load_dotenv()

    try:
        token = os.environ['VK_API_KEY']
    except KeyError:
        print('Ошибка: не установлена переменная окружения VK_API_KEY.')
        return

    parser = argparse.ArgumentParser(
        description='Укажите URL-адрес в качестве аргумента.'
    )
    parser.add_argument('url', help='Введите URL для сокращения или анализа')
    args = parser.parse_args()

    user_input = args.url

    try:
        if is_shorten_link(token, user_input):
            clicks = count_clicks(token, user_input)
            print(f'Количество кликов по ссылке: {clicks}')
        else:
            short_link = shorten_link(token, user_input)
            print(f'Короткая ссылка: {short_link}')
    except ValueError as vk_err:
        print(f'Ошибка VK API: {vk_err}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP ошибка при обращении к VK API: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Ошибка сети при обращении к VK API: {req_err}')


if __name__ == '__main__':
    main()
