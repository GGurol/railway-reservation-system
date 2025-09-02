# Railway-reservation-Django



###
Clone the repository:

```
git clone https://github.com/GGurol/railway-reservation-system.git
cd railway-reservation-system
```

###
For clean database:
```
sudo rm db.sqlite3
```

###

Build the docker:
```
docker compose up build -d

```

###
Database migrations:
```
docker compose exec web python manage.py migrate
```

###
Create admin login (you should login with this login to adding trains):
```
docker compose exec web python manage.py createsuperuser
```

###
Visit:
```
localhost:8000
```
