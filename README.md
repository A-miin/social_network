Для запуска проекта установите python версии 3.7 и выше, Docker 20.10.12 

Для того чтобы клонировать содержимое репозитория выполните команду:
```bash
git clone git@github.com:A-miin/social_network.git
```
После клонирования перейдите в склонированную папку и выполните следующие команды:

Создайте файл .env для хранения переменных окружения. Заполните по типу .env.example
```bash
touch .env
```
Запустите докер командой:
```bash
docker-compose up -d --build
```
Проект будет доступен по адресу: http://127.0.0.1:8000/

Данные для входа: admin@admin.admin: admin (superuser)