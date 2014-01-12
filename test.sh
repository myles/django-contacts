echo "Testing"
pip install --use-wheel --find-links=dist/ $PACKAGE_NAME
echo "import contacts; print 'Hello World';" | python
