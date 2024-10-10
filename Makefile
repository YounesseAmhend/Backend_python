run: 
	python main.py


test:
	pytest tests.py -q 

hot:
	python hot_reload.py

git:
	git add .
	git commit -m "$(m)"
	git push origin main