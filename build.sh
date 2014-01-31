set -xe
#
# Check if PACKAGE_NAME is set, if not, load it from the file PACKAGE_NAME
#
if [ -z "$PACKAGE_NAME" ]
    then
    echo "Setting PACKAGE_NAME from file."
    export PACKAGE_NAME=`cat PACKAGE_NAME`
fi

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
#python setup.py bdist_wheel
#python setup.py bdist_egg
python setup.py sdist
#cp dist/*.egg $PIP_DOWNLOAD_CACHE
#cp dist/*.whl $PIP_DOWNLOAD_CACHE
cp dist/* $PIP_DOWNLOAD_CACHE
