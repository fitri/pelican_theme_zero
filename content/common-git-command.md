Title: Commonly Use Git Command
Date: 2023-07-21
Category: Git
Tags: tools, deployment, vsc, git, commandline
Slug: commonly-use-git-command
Authors: Fitri Rahim

## Setting Up

### user and email configuration
```bash
git config --global user.name "Fitri Rahim"
```
```bash
git config --global user.email "person@fitri.me"
```

### initialize git repo
```bash
git init
```

### cache credentials
```bash
git config --global credential.helper cache
```



## Adding and Removing File

### add single file
```bash
git add thefilename.log
```

### add all file inside of current dir
```bash
git add .
```

### remove file from tracked, wildcards accepted
```bash
git rm thedirname/thefiletoremove
```



## Staging and Commit

### status of the current repo
```bash
git status
```

### commit changes with short message short
```bash
git commit -m "what changes have you made? write here"
```

### show differences
```bash
git diff
```

### discard changes made to the files
```bash
git checkout filenametorestore
```

### discard all the changes made
```bash
git checkout
```

### reset file to the last commit - unstaged
```bash
git reset HEAD thefiletorevert
```

### reset all files to the last commit -unstaged
```bash
git reset HEAD
```

### reset working dir to the last commit - discard all changes
```bash
git reset --hard HEAD
```

> git checkout is like switching to different version (like switching user concept in Linux), but git reset is discard by moving to another commit completely (like logout and login as new user concept in Linux). Only use git reset for unstage, for revert better options use git revert.

###  show differences after git add
```bash
git diff --staged
```

### show differences for single file
```bash
git diff filenametodiff
```

### open default editor to add multiple line to commit history
```bash
git commit
```

### change git commit message
```bash
git commit --amend -m "new message to replace the last comm
it message"```

### add file to the last commit
```bash
git add fileforgettentoadd
```
```bash
git commit --amend --no-edit
```

### backdated commit
```bash
git commit --allow-empty --date="Sat Nov 14 14:00 2015 +0100"-m 
'2 Dec commit'```



## Log and History

### simple log with details commit message
```bash
git log -p
```

### draw history to show commit log
```bash
git log --graph --oneline --decorate
```

### draw history to show commit log for all branches
```bash
git log --graph --oneline --decorate --all
```

### view particular commit
```bash
git show thecommitrevnumberhere
```

### revert to previous commit by create new commit on top of latest commit
```bash
git revert HEAD
```

### revert to specifc version of the commit
```bash
git revert thegithashversioncommit
```



## Branching and Merging

### create new branch
```bash
git branch thenewbranchname
```

### create new branch and change to it
```bash
git checkout -b thenewbranch
```

### list all the branches
```bash
git branch
```

### list all including remote
```bash
git branch -a
```

### delete branch
```bash
git branch -d existingbranchtodelete
```

### delete remote branch
```bash
git push origin --delete remotebranchtodelete
```

### merging another branch into current checkin branch
```bash
git merge existingbranch
```

### merge and commit
```bash
git merge --no--ff exisitingbranch
```

### abort merge if conflicted
```bash
git merge --abort
```

### or can use git reset to abort
```bash
git reset
```



## Remote Repository

### adding remote repository
```bash
git remote add origin gettheurlfromgithub
```

### show all remote repository
```bash
git remote -v
```

### get specific remote repo info
```bash
git remote show nameoftheremoterepo
```

### push changes to remote repository
```bash
git push remoterepositoryname branchname
```

### pull changes from remote repository
```bash
git pull remoterepositoryname branchname
```

### merge remote with local repository
```bash
git merge remoterepositoryname
```

### push branch to remote repo
```bash
git push -u origin thebranchtopush
```

### combine branch to the current branch including the commits
```bash
git rebase thebranchnametocombinewith
```
