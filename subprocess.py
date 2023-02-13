import subprocess
# subprocess function on Linux
subprocess.run(["date"])
# Sleep for 2 seconds
subprocess.run(["sleep", "2"])
# subprocess function on Linux ls
result = subprocess.run(["ls", "this_file_does_not_exist"])
# print(result.returncode)
# subprocess for obtaining the output of a command
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)
# this print is in bytes format
print(result.stdout.decode().split())
# subprocess error rm does not exist
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)