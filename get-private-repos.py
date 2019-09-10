from json import loads
from os import chdir, mkdir
from os.path import exists, expanduser, join
from subprocess import PIPE, run
from shutil import rmtree

downloadPath = join(expanduser("~"), "Downloads", "github-private-repos")

getRepos = run(["hub", "api", "/user/repos"], check=True, stdout=PIPE)

reposAll = getRepos.stdout.decode().replace("'", "").strip()

if exists(downloadPath):
    rmtree(downloadPath)

mkdir(downloadPath)
chdir(downloadPath)

repos = loads(reposAll)

for repo in repos:
    if repo["private"]:
        print("\n----\nDownloading...", repo["ssh_url"], "\n")
        run(["git", "clone", repo["ssh_url"]])

print("\nAll Done...")
