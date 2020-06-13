from json import loads
from os import chdir, mkdir
from os.path import exists, expanduser, join
from subprocess import PIPE, run
from shutil import rmtree
from sys import argv


try:
    if argv[1] == "-p":
        isPrivate = True
except:
    isPrivate = False


def download(url):
    print("\n----\nDownloading...", url, "\n")
    run(["git", "clone", url])


downloadDir = "github-private-repos" if isPrivate else "github-public-repos"

downloadPath = join(expanduser("~"), "Downloads", downloadDir)

getRepos = run(["hub", "api", "/user/repos"], check=True, stdout=PIPE)

reposAll = getRepos.stdout.decode().replace("'", "").strip()

if exists(downloadPath):
    rmtree(downloadPath)

mkdir(downloadPath)
chdir(downloadPath)

repos = loads(reposAll)

for repo in repos:
    if isPrivate:
        if repo["private"]:
            download(repo["ssh_url"])
    else:
        if not repo["fork"]:
            download(repo["ssh_url"])

print("\nAll Done...")
