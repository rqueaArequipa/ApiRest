venv
db.sqlite3

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations 
python manage.py migrate
