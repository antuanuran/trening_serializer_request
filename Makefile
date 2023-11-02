docer_run:
	docker-compose up -d
	docker-compose down -v
	docker-compose up -d


dumpdb: docer_run
	sleep 5
	python manage.py makemigrations
	python manage.py migrate

recreatedb: dumpdb
	sleep 5
	python manage.py createsuperuser


run: recreatedb
	python manage.py runserver
	


