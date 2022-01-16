#!/bin/python3

import sys
import subprocess

def main():
    required_version = (3, 10)
    minimum_version = (3, 9) # Got this by trial and error, python requires os.waitstatus_to_exitcode
    # If our version is fine, use it
    if sys.version_info >= required_version:
        print("/bin/python3", end='')
        return 0

    for i in range(required_version[1], minimum_version[1], -1):
        python_path = f'/bin/python3.{i}'
        
        try:
            subprocess.call([python_path, '--version'], stdout=subprocess.DEVNULL)
            print(python_path, end='')
            return 0
        except:
            pass
    
    return 1


if __name__ == "__main__":
    sys.exit(main())
