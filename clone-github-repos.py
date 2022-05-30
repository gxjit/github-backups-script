from argparse import ArgumentParser
from json import loads
from os import chdir, mkdir
from os.path import exists, expanduser, join
from shutil import rmtree
from subprocess import PIPE, run

# from pprint import PrettyPrinter


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("-p", "--private", action="store_true")

    return parser.parse_args()


pargs = parseArgs()


def download(url):
    print("\n----\nDownloading...", url, "\n")
    run(["git", "clone", url])


downloadDir = "github-private-repos" if pargs.private else "github-public-repos"

downloadPath = join(expanduser("~"), "Downloads", downloadDir)

getRepos = run(
    ["gh", "api", "/user/repos?per_page=100&page=1"], check=True, stdout=PIPE
)
# &visibility=private

reposAll = getRepos.stdout.decode().strip()
# .replace("'", "")

if exists(downloadPath):
    rmtree(downloadPath)

mkdir(downloadPath)
chdir(downloadPath)

repos = loads(reposAll)

# pprint = PrettyPrinter().pprint

for repo in repos:
    if pargs.private:
        if repo["private"]:
            # pprint(repo["name"])
            # pprint(repo["private"])
            download(repo["ssh_url"])
    else:
        if not repo["fork"]:
            download(repo["ssh_url"])

print("\nAll Done...")
