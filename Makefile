.PHONY: install run test clean docker-up docker-down

install:
	pip3 install -r requirements.txt

run:
	python3 app.py

test:
	cd tests && python3 -m pytest testing.py -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete 2>/dev/null || true
	rm -rf tmp/

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down
