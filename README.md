# Git-note

Some important git command


1. Create a new branch
- To create new branch on Local 
  * git checkout -b [name_of_your_new_branch]
- To create new branch on remote
  * git push --set-upstream origin [name_of_your_new_branch]

2. Restore files back to the state of repository
- To restore one file
  * git checkout -- "name of file"
- To restore everything
  * git checkout -- .

3. Join two or more development histories together
* git merge
Resolve conflict : https://swcarpentry.github.io/git-novice/09-conflict/

4. Pull only one file from git(not sure, need to test)
git fetch  
git checkout -m <revision> <yourfilepath>  
git add <yourfilepath>  
git commit  
 
Regarding the git checkout command: <revision> - a branch name, i.e. origin/master <yourfilepath> does not include the repository name (that you can get from clicking copy path button on a file page on GitHub), i.e. README.md

