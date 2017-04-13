all:
	@echo 'check        check your python code'
	@echo 'run          runs all features in app_name'

check:
    # ignore the Long lines, not using it right now
	@flake8 --exclude=virtualenv/ --ignore E501 .

run:
	@behave app_name

smoke:
	@behave app_name --tags=smoke

