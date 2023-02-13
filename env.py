import os
import sys
import subprocess
print("HOMW: "+ os.environ.get("HOME", ""))
# Set environment variable HOME to /home/repl
os.environ["HOME"] = "/home/repl"
# Set environment variable on Linux
os.environ["EDITOR"] = "vim"
# or
# export EDITOR=vim
print(sys.argv)

# Create copy of environment
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
