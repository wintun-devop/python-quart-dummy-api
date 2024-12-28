## installing alembic and sqlalchemy
```
pip install alembic sqlalchemy
```
## alembic initialization
```
alembic init migrations
```
## alembic db-source configuration-postgresql
```
[app]
sqlalchemy.url = postgresql+psycopg2://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:{port}/${DB_NAME}
```
## config env.py
```
import model to env.py as Admin setup
```
## migration
```
alembic revision --autogenerate -m "your migration name"
```
```
alembic upgrade heads
```
