from json import loads
from os import mkdir, chdir
from os.path import exists, expanduser, join
from urllib.request import urlopen, urlretrieve
from shutil import rmtree

username = "gxjit"
archiveFormat = "zipball"
repoUrl = f"https://api.github.com/users/{username}/repos"
downloadPath = join(expanduser("~"), "Downloads", "github-repos")

if exists(downloadPath):
    rmtree(downloadPath)

mkdir(downloadPath)
chdir(downloadPath)

repos = loads(urlopen(repoUrl).read().decode("utf-8"))

for repo in repos:
    if not repo["fork"]:
        archiveUrl, _ = repo["archive_url"].split("/{arc")
        downloadUrl = f"{archiveUrl}/{archiveFormat}/master"
        downloadFile = join(downloadPath, f'{repo["name"]}.zip')
        print(downloadUrl, "\n", downloadFile)
        urlretrieve(downloadUrl, downloadFile)

print("\nAll Done...")


# https://api.github.com/users/gxjit/repos
# https://api.github.com/repos/gxjit/conCatJs/{archive_format}{/ref}
