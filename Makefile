run: 
	python app/main.py


test:
	pytest tests.py -q 

git:
	git add .
	git commit -m "$(m)"
	git push origin main