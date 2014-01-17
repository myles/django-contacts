set -x
mkdir -p ~/.pip_cache
export ORIGINAL_HOME=`pwd`
export ORIGINAL_PACKAGE_NAME=$PACKAGE_NAME
export PIP_DOWNLOAD_CACHE=~/.pip_cache/
export CI_DIST=~/clone/ci_scripts/dist
export PACKAGE_DIST=~/clone/dist
export PIP_FIND_LINKS="$PIP_DOWNLOAD_CACHE"
pip install --upgrade pip setuptools
export PIP=`which pip`
echo "Post-Upgrade PIP Version:"
$PIP -V
git clone https://github.com/CaseRails/ci_scripts.git
cd ci_scripts
./build.sh
./test.sh
cd $ORIGINAL_HOME
export PACKAGE_NAME=$ORIGINAL_PACKAGE_NAME
export PIP_FIND_LINKS="$PIP_DOWNLOAD_CACHE $CI_DIST"
$PIP install ci_scripts
python setup.py clean
python setup.py build
python setup.py bdist_wheel
python setup.py bdist_egg
