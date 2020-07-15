import sys

def py2_or_py3():
    major = sys.version_info.major
    if major < 3:
        return 'Python2'
    else:
        return 'Python3'

version = py2_or_py3()
print(version)