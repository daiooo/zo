rm -rf dist/* build/*; python setup.py check && python setup.py install && python setup.py sdist && twine upload dist/*
