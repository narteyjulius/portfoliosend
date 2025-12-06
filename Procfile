python manage.py makemigrations && \
python manage.py migrate && \
python manage.py createsuperuser --noinput || true && \
gunicorn portfolio_site.wsgi:application --log-file -
