# UI-Group-Project-
UI COMS W4170 - Group Project: Spring 2022

## Requirements
* Flask
* Gunicorn

## Testing
Please use `gunicorn -w 1 --bind 0.0.0.0:8000 wsgi:app` when running the app, Flask struggles with image loading.
