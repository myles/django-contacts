set -e
echo "./test.sh"
export ORIGINAL_HOME=`pwd`
export ORIGINAL_PACKAGE_NAME=$PACKAGE_NAME
export PIP_DOWNLOAD_CACHE=~/.pip_cache/
export CI_DIST=~/clone/ci_scripts/dist
export PACKAGE_DIST=~/clone/dist
export PIP_FIND_LINKS="$PIP_DOWNLOAD_CACHE $CI_DIST $PACKAGE_DIST"
pip install --upgrade --find-links dist/ $PACKAGE_NAME
echo "import $PACKAGE_NAME; print 'Hello World';" | python
