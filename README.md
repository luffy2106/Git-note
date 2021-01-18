# Git-note

1.Some important git command

1.0 Track remote branch(make branch visible in local) 
- To track all branchs : remote=origin ; for brname in `git branch -r | grep $remote | grep -v master | grep -v HEAD | awk '{gsub(/[^\/]+\//,"",$1); print $1}'`; do git branch --track $brname $remote/$brname  ; done
- To track one branch at a time : git checkout --track origin/branch-name 

1.1 Create a new branch 
- To create new branch on Local 
  * git checkout -b [name_of_your_new_branch]
- To create new branch on remote
  * git push --set-upstream origin [name_of_your_new_branch]

1.2 Restore files back to the state of repository
- To restore one file
  * git checkout -- "name of file"
- To restore everything
  * git checkout -- .

1.3 Join two or more development histories together
* git merge
Resolve conflict : https://swcarpentry.github.io/git-novice/09-conflict/

1.4 Pull only one file from git(not sure, need to test)  
git fetch  
git checkout -m <revision> <yourfilepath>  
git add <yourfilepath>  
git commit  
 
Regarding the git checkout command: <revision> - a branch name, i.e. origin/master <yourfilepath> does not include the repository name (that you can get from clicking copy path button on a file page on GitHub), i.e. README.md

1.5 Add files to staging areas(index)  
- stage all(new, modified, deleted) files : git add -A  
- stage new and modifed files only : git add .  
- stage modified and deleted files only: git add -u  

1.6 Show the commit history : git log  
- To show the commit history in local(with graph) : git log --graph
- To show the commit history in remote(with graph) : git log --graph origin/branch_name

1.7 Delete the last commit(in local)  
- git reset HEAD~1 (you can use 2 or 3 .. if you want to delete the last 2,3 .. commit  

1.8 Unstage a file(remove file from staging area)  
- git restore --staged <file-name> or git rm --cached <file-name>  
 
2. Some popular errors we might encounter

2.1 non-fast-forward errors

2.1.1 Example  
C:\Test_solution\Pandas\just-pandas-things>git push  
To https://github.com/luffy2106/pandas.git  
 ! [rejected]        main -> main (non-fast-forward)  
error: failed to push some refs to 'https://github.com/luffy2106/pandas.git'  
hint: Updates were rejected because the tip of your current branch is behind  
hint: its remote counterpart. Integrate the remote changes (e.g.  
hint: 'git pull ...') before pushing again.  
hint: See the 'Note about fast-forwards' in 'git push --help' for details.  

2.1.2 Cause  
The reason behind this error is your local commit branch and remote commit branch is different. You can check by type 'git status' or use command in section 1.6 to see in detail. This error might come from the fact that you modify the remote branch by another computer or direcly edit in the website of git, and you forget to do 'git pull' before adding new commit and pushing.

2.1.3 How to fix 

Use command in section 1.6 to see the difference between local index and remote index. If the local index is one step more than remote index, we need to either:
- Come back to the previous commit by command in 1.7 then git pull before modify code then git push later.
- Using git merge to merge the local index and remote index

2.1.4 Tips to avoid in the future  
Do git fetch or git pull before doing anything(it's not true, need to update)




