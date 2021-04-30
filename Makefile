init:

clear:

run:
	export FLASK_APP=rest && export FLASK_ENV=production && flask run
run_dev:
	export FLASK_APP=rest && export FLASK_ENV=development && flask run