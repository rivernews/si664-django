rm db.sqlite3 && \
rm -rf unesco/migrations && \
./manage.py makemigrations unesco && \
./manage.py migrate && \
./manage.py loaddata && echo SUCCESS. && return

echo ERROR: see above message.