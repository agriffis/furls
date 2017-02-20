.PHONY: dev
dev: build
	docker-compose run web python manage.py migrate
	$(MAKE) -j2 serve port

# bit of a hack: rebuild the image when requirements.txt
# is newer than Dockerfile, then touch Dockerfile to keep up.
.PHONY: build
build: Dockerfile
Dockerfile: requirements.txt
	docker-compose build web
	@touch Dockerfile

.PHONY: serve
serve:
	docker-compose up

.PHONY: port
port:
	@while true; do \
	    sleep 1; \
	    output=$$(docker-compose port web 8000 2>&1) && break; \
	done; \
	echo "======================================================"; \
	echo "||"; \
	echo "|| Listening on http://$$(hostname):$${output#*:}/"; \
	echo "||"; \
	echo "======================================================"
