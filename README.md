# Project_1
## Task_3
Задание 3 промежуточного проекта, 28_qa-python

```text
Task_2/
│── allure-results/                             # Отчёты Allure
│
├── data/
│   ├── data_helpers.py                         # Вспомогательные данные
│   └── data_urls.py                            # Данные URL
│
├── pages/
│   ├── account_profile_page.py                 # Методы страницы /account/profile
│   ├── base_page.py                            # Основные методы страниц
│   ├── feed_page.py                            # Методы страницы /feed
│   ├── forgot_password_page.py                 # Методы страницы /forgot-password
│   ├── ingredient_page.py                      # Методы страницы /ingredient
│   ├── login_page.py                           # Методы страницы /login
│   ├── main_page.py                            # Методы главной страницы
│   ├── order_history_page.py                   # Методы страницы /order-history
│   └── reset_password_page.py                  # Методы страницы /reset-password
│
├── tests/
│   ├── test_basic_functionality.py             # Проверка основного функционала
│   ├── test_order_feed_section.py              # Проверка раздела «Лента заказов»
│   ├── test_password_recovery.py               # Проверка раздела «Восстановление пароля»
│   └── test_personal_account.py                # Проверка личного кабинета
│
├── api_methods.py                              # Методы взаимодействия с api                     
├── conftest.py                                 # Фикстуры pytest
├── helpers.py                                  # Вспомогательная логика для тестов
├── requirements.txt                            # Подключённые библиотеки
└── README.md                                   # Описание проекта
