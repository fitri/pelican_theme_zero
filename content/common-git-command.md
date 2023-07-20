Title: Commonly Use Git Command
Date: 2023-07-21
Category: Git
Tags: tools, deployment, vsc, git, commandline
Slug: commonly-use-git-command
Authors: Fitri Rahim

## Setting Up

### user and email configuration
git config --global user.name "Fitri Rahim"
git config --global user.email "person@fitri.me"

### initialize git repo
git init

### cache credentials
git config --global credential.helper cache



## Adding and Removing File

### add single file
git add thefilename.log

### add all file inside of current dir
git add .

### remove file from tracked, wildcards accepted
git rm thedirname/thefiletoremove



## Staging and Commit

### status of the current repo
git status

### commit changes with short message short
git commit -m "what changes have you made? write here"

### show differences
git diff

### discard changes made to the files
git checkout filenametorestore

### discard all the changes made
git checkout

### reset file to the last commit - unstaged
git reset HEAD thefiletorevert

### reset all files to the last commit -unstaged
git reset HEAD

### reset working dir to the last commit - discard all changes
git reset --hard HEAD

> git checkout is like switching to different version (like switching user concept in Linux), but git reset is discard by moving to another commit completely (like logout and login as new user concept in Linux). Only use git reset for unstage, for revert better options use git revert.

###  show differences after git add
git diff --staged

### show differences for single file
git diff filenametodiff

### open default editor to add multiple line to commit history
git commit

### change git commit message
git commit --amend -m "new message to replace the last commit message"

### add file to the last commit
git add fileforgettentoadd
git commit --amend --no-edit

### backdated commit
git commit --allow-empty --date="Sat Nov 14 14:00 2015 +0100"-m '2 Dec commit'



## Log and History

### simple log with details commit message
git log -p

### draw history to show commit log
git log --graph --oneline --decorate

### draw history to show commit log for all branches
git log --graph --oneline --decorate --all

### view particular commit
git show thecommitrevnumberhere

### revert to previous commit by create new commit on top of latest commit
git revert HEAD

### revert to specifc version of the commit
git revert thegithashversioncommit



## Branching and Merging

### create new branch
git branch thenewbranchname

### create new branch and change to it
git checkout -b thenewbranch

### list all the branches
git branch

### list all including remote
git branch -a

### delete branch
git branch -d existingbranchtodelete

### delete remote branch
git push origin --delete remotebranchtodelete

### merging another branch into current checkin branch
git merge existingbranch

### merge and commit
git merge --no--ff exisitingbranch

### abort merge if conflicted
git merge --abort

### or can use git reset to abort
git reset



## Remote Repository

### adding remote repository
git remote add origin gettheurlfromgithub

### show all remote repository
git remote -v

### get specific remote repo info
git remote show nameoftheremoterepo

### push changes to remote repository
git push remoterepositoryname branchname

### pull changes from remote repository
git pull remoterepositoryname branchname

### merge remote with local repository
git merge remoterepositoryname

### push branch to remote repo
git push -u origin thebranchtopush

### combine branch to the current branch including the commits
git rebase thebranchnametocombinewith
