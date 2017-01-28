.PHONY: dev
dev:
	docker-compose run web python manage.py migrate
	$(MAKE) -j2 serve port

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
