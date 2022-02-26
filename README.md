# Dmitriynic-SkillFactory_D7.5_Django_Python_v2
Запуск celery для отправке сообщения подписчику при добавлении новости: celery -A NewsPaper worker --pool=solo -l INFO
Запуск на windows периодической задачи отправки подписчикам новостей за последнюю неделю не работает, 
для linux: celery -A NewsPaper worker -l INFO -B
