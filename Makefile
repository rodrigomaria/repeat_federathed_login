help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Common sequence of commands:'
	@echo '- make black'
	@echo '- make isort'
	@echo '- make flake8'
	@echo '- make lint'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'


black: ## run black over the code
	@ black *.py

isort: ## run isort over the code
	@ isort automation.py execute.py

flake8: ## run flake8 over the code
	@ flake8 automation.py execute.py

lint: ## run linters over the code
	@ make black
	@ make isort
	@ make flake8