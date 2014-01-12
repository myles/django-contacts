set -e

echo "Installing Build Requirements"
curl https://raw2.github.com/CaseRails/ci_scripts/master/ci_requirements.txt >> requirements.txt
curl -O https://raw2.github.com/CaseRails/ci_scripts/master/build_artifacts.py
curl -O https://raw2.github.com/CaseRails/ci_scripts/master/deploy.py
curl -O https://raw2.github.com/CaseRails/ci_scripts/master/deploy_wheels.py
curl -O https://raw2.github.com/CaseRails/ci_scripts/master/get_env_vars.py
curl -O https://raw2.github.com/CaseRails/ci_scripts/master/retrieve.py
sort -u requirements.txt > sorted_requirements.txt
pip install -r sorted_requirements.txt
python setup.py bdist_wheel
