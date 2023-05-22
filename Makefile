
manage_py := docker compose exec -it backend python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

createsuperuser:
	$(manage_py) createsuperuser

shell:
	$(manage_py) shell_plus --print-sql

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	docker exec -it backend pytest app/tests

gunicorn:
	cd app && gunicorn --workers 4 settings.wsgi --max-requests 10000 --log-level info --bind 0.0.0.0:8000
