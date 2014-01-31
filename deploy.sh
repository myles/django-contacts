set -e
export PIP_DOWNLOAD_CACHE=~/.pip_cache/
export PIP_FIND_LINKS="$PIP_DOWNLOAD_CACHE"
pip install --upgrade $PACKAGE_NAME
echo "from ci_scripts import deploy" | python
