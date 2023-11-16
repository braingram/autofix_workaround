import os

print(os.environ)
cmd = """gh api --method PUT -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /repos/braingram/autofix_workaround/pulls/14/merge -f commit_title='Sneaky' -f commit_message='na'"""
print(os.system(cmd))
