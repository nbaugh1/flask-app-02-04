# flask-app-2

## How to run

### Build images and containers
#### Via Docker-
- Development:

    - `docker-compose up -d --build`

- Production:

    - `docker-compose -f docker-compose.prod.yml up -d --build`

### Create databases

- Development:

   - `docker-compose exec web python manage.py create_db`

- Production:

    - `docker-compose -f docker-compose.prod.yml exec web python manage.py create_db`

### Kill containers

- `docker-compose down -v`

### Check logs 

- Development:

    - `docker-compose logs -f`

- Production:

    - `docker-compose -f docker-compose.prod.yml logs -f`

