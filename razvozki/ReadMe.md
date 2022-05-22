- create db razv
- utf8mb4_unicode_ci
- /razv create config.cfg
[LOG_PAS]
user = 
pass = 
sec_key = 
admin = False
- from /razv python manage.py makemigrations
- from /razv python manage.py migrate
- manage.py runserver 8100