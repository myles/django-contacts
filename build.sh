set -xe
#
# Build and install ci_scripts
#
mkdir -p ~/.pip_cache
export ORIGINAL_HOME=`pwd`
export ORIGINAL_PACKAGE_NAME=$PACKAGE_NAME
export PIP_DOWNLOAD_CACHE=~/.pip_cache/
export PIP_FIND_LINKS="$PIP_DOWNLOAD_CACHE"
pip install --upgrade pip setuptools setuptools_git
export PIP=`which pip`
git clone https://github.com/CaseRails/ci_scripts.git
cd ci_scripts
./build.sh
./test.sh
cd $ORIGINAL_HOME
export PACKAGE_NAME=$ORIGINAL_PACKAGE_NAME
$PIP install ci_scripts
#
# End installation of ci_scripts
#
python setup.py clean
python setup.py bdist_wheel
python setup.py bdist_egg
cp dist/*.egg $PIP_DOWNLOAD_CACHE
cp dist/*.whl $PIP_DOWNLOAD_CACHE
