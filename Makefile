build:
	sudo docker build -t aspect_ml .

run:
	sudo docker run -d -it -p 7000:7000 aspect_ml