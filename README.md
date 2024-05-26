# Redlab hack

Разработка модели для выявления аномалий во временном ряду

Сервис доступен по ссылке: http://80.87.104.231:8501/

Документация сервиса доступена по ссылке: http://80.87.104.231:8000/docs

## Описание кейса

🖍️ Проблематика: простои в работе современных ИТ-систем стоят очень дорого. Для того, чтобы их избежать, системы мониторинга должны помогать людям выявлять странности в поведении системы на основании собираемых данных телеметрии и своевременно оповещать о них операторов и техническую команду. Для решения этой задачи, мы предлагаем разработать прототип сервиса, который будет анализировать временной ряд и размечать выявленные аномалии в данных.

🖍️ Вводные данные: слепок данных телеметрии реальной системы для анализа и обучения модели.

🖍️ Предполагаемый результат: минимальный прототип сервиса на Python, который сканирует временное окно для выбранной метрики и подсвечивает аномалии в нем. Критерием оценки результата будет замер точности работы модели по предложенной методике и реализация самого сервиса.
Цель данной задачи состоит в разработке и обучении ИИ модуля, способного анализировать и предсказывать пассажиропоток на станциях метро с использованием имеющихся данных.


## Навигация по репозиторию

В корне репозитория содержатся папки для каждого сервиса системы:
- Back - для эндпоинтов на FastAPI и всё для предобработки и инференса;
- Database - для работы Postgres базы данных и подключения к ней;
- Front - для всего, что связано с фронтом и веб-ui;
- materials - презентация и картинки для оформления;
- utils - вспомогательные функции для всех сервисов.

Помимо папок с сервисами в корне содержатся вспомогательные файлы:
- .env - для применения переменных окружения;
- .gitignore
- config.json - для конфигурации логирования моделей;
- docker-compose.yml - входная точка для разворачивания сервисов;
- Dockerfile_back - входная точка для сборки бэка;
- Dockerfile_front - входная точка для сборки фронта;
- Makefile - инструкции для деплоя на хост и работы там;
- README.md

## Архитектура сервиса

Сервис состоит из четырёх основных компонентов:
- бэкэнд (FastAPI) для обработки запросов с фронта и вызова функционала ML'я;
- база данных (Postgres) для хранения витрин для бэка;
- веб-ui (stgreamlit) для взаимодействия с системой, вызова API-методов и визуальной оценки результатов выполнения инференса;
![Alt text](materials/Redlab_arch.png)

## Деплой сервиса

Простой деплой (при наличии ssh-ключа на сервере) на нужный хост и поднятие сервиса делается через выполнение команд из Makefile. 

В репозитории содержатся все необходимые инструкции для поднятия сервисов (Dockerfile для бэка и фронта, docker-compose для поднятия полной сетки сервисов) и другие вспомогательные файлы для их работы.

## Команда REU DS CLUB

| Участник                            | Роль            | Телеграм       |
|-------------------------------------|-----------------|----------------|
| Пашинская Пелагея                   | Team lead + MLE | @polyanka003   |
| Ворогушин Максим                    | Front           | @Maksoit       |
| Иванов Александр                    | MLE             | @lild1tz       |
| Мичурин Артем                       | DE              | @artemmichurin |
| Ващкевич Алексей                    | Front + MLE     | @gasboy04      |
