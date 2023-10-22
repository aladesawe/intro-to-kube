import subprocess
import yaml
def run_checks(gh_actions_file: str):
    with open(gh_actions_file) as f:
        actions = yaml.safe_load(f)
    steps = actions['jobs']['scavenger']['steps']
    checks = [step for step in steps if 'Checks' in step['name']]
    for check in checks:
        subprocess.run(check["run"], capture_output=False, shell=True, executable='/bin/bash')
        
run_checks('/workspaces/intro-to-kube/.github/workflows/rbac-to-the-future.yml')