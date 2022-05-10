# UI-Group-Project-
UI COMS W4170 - Group Project: Spring 2022

## Requirements
* Flask
* Gunicorn

## Testing
Please use `gunicorn -w 1 --bind 0.0.0.0:8000 wsgi:app` when running the app, Flask struggles with image loading.

If running on Mac, follow the instructions below: 
1. Run "python3 -m venv env" in your directory
2. Type "source env/bin/activate" in terminal
3. Type "pip install flask, gunicorn" to install Flask and Gunicorn
4. Run "gunicorn -w 1 --bind 0.0.0.0:8000 wsgi:app" in the terminal
