echo "Testing"
pip install --use-wheel --find-links=dist/ django-contacts
echo "import contacts; print 'Hello World';" | python
