from json import loads
from os import chdir, mkdir
from os.path import exists, expanduser, join
from subprocess import run
from urllib.request import urlopen
from shutil import rmtree

username = "gxjit"
repoUrl = f"https://api.github.com/users/{username}/repos"
downloadPath = join(expanduser("~"), "Downloads", "github-public-repos")

if exists(downloadPath):
    rmtree(downloadPath)

mkdir(downloadPath)
chdir(downloadPath)

repos = loads(urlopen(repoUrl).read().decode("utf-8"))

for repo in repos:
    if not repo["fork"]:
        print("\n----\nDownloading...", repo["ssh_url"], "\n")
        run(["git", "clone", repo["ssh_url"]])

print("\nAll Done...")
