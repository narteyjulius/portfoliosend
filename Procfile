python manage.py makemigrations && \
python manage.py migrate && \
python manage.py shell < portfolio_site/create_super.py && \
gunicorn portfolio_site.wsgi:application --log-file -
