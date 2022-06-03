.PHONY: build
build:
	docker build -t petstore-connexion .

.PHONY: run
run: build
	docker run -p 8080:8080/tcp petstore-connexion
