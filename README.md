# Обрезка ссылок с помощью VK API
  
Данный скрипт с помощью VK API позволяет выводить сокращенную ссылку полученного URL, а также при введенной сокращенной ссылке считает кол-во переходов по ней за все время. 

## Установка

### Создание виртуального окружения

Python3 должен быть уже установлен.
Для корректной работы скрипта, рекомендую использовать все зависимости из файла `requirements.txt`
Запуск лучше производить используя виртуальное окружение `venv`.

Для создания `venv` и использования скрипта выполните следующие шаги:

Создать виртуальное окружение
```
python -m venv <name venv>
```

Активировать
```
<name venv>\Scripts\activate
```

Установить все зависимости из `requirements.txt`
```
pip install -r requirements.txt
```

### Токен VK API

Для работы со скриптом необходимо получить токен VK API. Для этого следует ознакомится с информацией из документации о получении [сервисного токена приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token).

Добавьте полученный токен в переменную `VK_API_KEY` в файле `.env`:

Пример файла `.env`:
```
VK_API_KEY=<ваш токен>
```

### Примеры использования

Сокращение ссылки:
```
(venv) C:\Проекты\VK_API> python main.py https://dvmn.org/modules
https://vk.cc/cvPDMl
```
Получение статистики по сокращённой ссылке:
```
(venv) C:\Проекты\VK_API> python main.py https://vk.cc/cvPDMl
Количество кликов по ссылке: 42
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
