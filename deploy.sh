curl https://raw2.github.com/CaseRails/ci_scripts/master/deploy.py > deploy.py
curl https://raw2.github.com/CaseRails/ci_scripts/master/requirements.txt > deploy_requirements.txt

pip install -r deploy_requirements.txt
python deploy.py
