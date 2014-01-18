set -x
mkdir -p ~/.pip_cache
export ORIGINAL_HOME=`pwd`
export ORIGINAL_PACKAGE_NAME=$PACKAGE_NAME
export PIP_DOWNLOAD_CACHE=~/.pip_cache/
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
$PIP install ci_scripts
python setup.py clean
python setup.py build
python setup.py bdist_wheel
python setup.py bdist_egg
cp dist/*.egg $PIP_DOWNLOAD_CACHE
cp dist/*.whl $PIP_DOWNLOAD_CACHE
