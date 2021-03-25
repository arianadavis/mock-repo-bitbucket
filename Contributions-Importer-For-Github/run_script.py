value = True;

# Contributions-Importer-For-Github/run_script.py
import sys
sys.path.append ("/usr/local/lib/python3.9/site-packages")
import git 
from git_contributions_importer import *
 
# Your private repo or Bitbucket repo
repo = git.Repo("/Users/adavis/Desktop/dev/chasecenter-com-ng")
repoTwo = git.Repo("/Users/adavis/Desktop/dev/chasecenter-com-api")
repoThree = git.Repo("/Users/adavis/Desktop/dev/sole360")

# Your mock repo
mock_repo = git.Repo("/Users/adavis/Desktop/dev/mock-repo-bitbucket")

importer = Importer([repo, repoTwo, repoThree], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['ariana@sole360.com','arianadavis62@gmail.com','adavis@warriors.com','hello@yourmobilegeek.tech'])
importer.set_start_from_last(value)
importer.import_repository()