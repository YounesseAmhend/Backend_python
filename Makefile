run: 
	python app/main.py


test:
	pytest test.py -q 

git:
	git add .
	git commit -m 'test'
	git push origin main