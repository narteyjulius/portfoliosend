python manage.py makemigrations && \
python manage.py migrate && \
python manage.py collectstatic --noinput &&\
gunicorn portfolio_site.wsgi:application --log-file -
