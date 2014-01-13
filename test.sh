set -e
echo "Testing"
pip install --find-links=dist/ $PACKAGE_NAME
echo "import contacts; print 'Hello World';" | python
