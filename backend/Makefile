PGUSER=postgres
PGPASS=12345
PGDATABASE=khe2024

createdb:
	docker exec -it db createdb --username=$(PGUSER) --owner=$(PGUSER) $(PGDATABASE)

dropdb:
	docker exec -it db dropdb -U $(PGUSER) $(PGDATABASE)

initdb:
	docker cp ./sql/init_db.sql db:/init_db.sql
	docker exec -it db psql -U $(PGUSER) $(PGDATABASE) -f /init_db.sql