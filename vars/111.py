import os
import subprocess
import sys

def search_branch(ncp_family_branch):
    ncp_tool_prototype_branch = 'master'
    path = r'D:\111\ncp_tool_prototype'
    os.chdir(path)
    process = subprocess.check_output(['git', 'branch', '-r'], shell=True)
    output = process.decode("utf-8")
    lines_rep = output.replace('  origin/','')
    lines = lines_rep.split('\n')
    a = []
    a.append(lines)
    for line in a[0]:
        if line == ncp_family_branch:
            ncp_tool_prototype_branch = line
    return ncp_tool_prototype_branch

if __name__ == '__main__':
    exit(search_branch(sys.argv[1]))