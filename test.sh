set -e
echo "./test.sh"
export PIP_DOWNLOAD_CACHE=~/.pip_cache/
export PIP_FIND_LINKS="$PIP_DOWNLOAD_CACHE"
pip install --upgrade $PACKAGE_NAME
echo "import $PACKAGE_NAME; print 'Hello World';" | python
