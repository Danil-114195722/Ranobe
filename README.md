# Ranobe
## It's landing of website to reading ranobe books

### Build project and start it
```shell
docker-compose up --build -d
```

### Migrate DB
```shell
docker-compose exec web python3 manage.py migrate
```

### Add superuser
```shell
docker-compose exec web python3 manage.py createsuperuser
```

### Access to DB from local comp
```shell
mysql -u root -p -h 172.16.1.4 ranoba_landing
```
