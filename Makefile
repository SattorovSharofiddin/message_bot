push:
	git add .
	git commit -m $(msg)
	git push -u origin main


setup:
	pip install -r requirements.txt