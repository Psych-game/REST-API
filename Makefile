init:

clear:

run:
	export FLASK_APP=src/rest && export FLASK_ENV=production && flask run
run_dev:
	export FLASK_APP=src/rest && export FLASK_ENV=development && flask run