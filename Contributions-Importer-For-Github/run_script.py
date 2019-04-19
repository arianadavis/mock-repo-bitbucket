# Contributions-Importer-For-Github/run_script.py
import git

from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/adavis/Desktop/dev/chasecenter-com-ng")
repoTwo = git.Repo("/Users/adavis/Desktop/dev/chasecenter-com-api")

# Your mock repo
mock_repo = git.Repo("/Users/adavis/Desktop/dev/mock-repo-bitbucket")

importer = Importer([repo, repoTwo], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['adavis@warriors.com', 'adavis@W-ADAVIS-MB.local', 'adavis@W-ADAVIS-MB.warriors.int'])
importer.import_repository()