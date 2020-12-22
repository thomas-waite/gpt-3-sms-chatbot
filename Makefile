SHELL = /bin/sh
PORT = 80

serve_app:
	FLASK_ENV=development FLASK_APP=app.py flask run -h 0.0.0.0 -p ${PORT}

serve_URL:
	ngrok http ${PORT}

deploy:
	gcloud app deploy

