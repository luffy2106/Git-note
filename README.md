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

1.3 Join two or more development histories together(git merge)
Reference : https://www.atlassian.com/git/tutorials/using-branches/git-merge
Command :     
- Merge 2 branch in local repo : git merge <name of branch need to merge to current branch>.
- Merge local branch to remote branch : git merge
Git merge will combine multiple sequences of commits into one unified history. In the most frequent use cases, git merge is used to combine two branches. If the repo of remote branch is ahead the repo of local branch, then there will be no conflict. Otherwise we have to solve conflict to merge. To be resolve conflict :   
https://swcarpentry.github.io/git-novice/09-conflict/

Prepare to merge to avoid conflict:
- Confirm the receiving branch : Execute git status to ensure that HEAD is pointing to the correct merge-receiving branch
- Fetch latest remote commits : Make sure the receiving branch and the merging branch are up-to-date with the latest remote changes 

There are 2 ways of merging:  
1.3.1 Fast Forward Merge

A fast-forward merge can occur when there is a linear path from the current branch tip to the target branch. In this case, there will be no conflict.   
1.3.2 3-way merge   

However, a fast-forward merge is not possible if the branches have diverged. When there is not a linear path to the target branch, Git has no choice but to combine them via a 3-way merge. 3-way merges use a dedicated commit to tie together the two histories. The nomenclature comes from the fact that Git uses three commits to generate the merge commit: the two branch tips and their common ancestor. In 3-way merge sometime there will be conflict if the state of each file in 2 branches is different(It will show something like : Automatic merge failed; fix conflicts and then commit the result.), what we have to do is :
- Solve the conflict.
- Add file which was sloved conflict to index.
- Run a normal git commit to generate the merge commit.
- Type git merge again.

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

1.9 The difference between git fetch and git pull 
1.9.1 Git fetch  
Command : Git fetch origin <name_of_the_branch>  
Reference : https://www.atlassian.com/git/tutorials/syncing/git-fetch
- Download all the history from remote resporitory to local repo and keep track by a short-lived ref FETCH_HEAD(you will see after you type command) 
- Ref FETCH_HEAD isolates fetched content from existing local content; it has absolutely no effect on your local development work.
- Then if you want your local respo is the same as the remote respo, simply do git merge, it will merging FETCH_HEAD into the current branch. If there is no conflict, the result is exactly what you'd expect: the commit at the tip of the appropriate remote branch is merged into the commit at the tip of your current branch. 

1.9.2 Git pull 
Referecen : https://www.atlassian.com/git/tutorials/syncing/git-pull 
- Git pull is just the combination of git fetch and git merge. The git pull command first runs git fetch which downloads content from the specified remote repository. Then a git merge is executed to merge the remote content refs and heads into a new local merge commit.

2.0 
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
Do git fetch or git pull before doing anything.








Note:
- In the new version, original "master" branch was renamed to "main"
- HEAD is Git’s way of referring to the current snapshot or a pointer. Internally, the git checkout command simply updates the HEAD to point to either the specified branch or commit. When it points to a branch, Git doesn't complain, but when you check out a commit, it switches into a “detached HEAD” state. To be more specific :  
When HEAD point to a single commit on a branch, for example on 527f799, It will show something like "(HEAD detached at 527f799)", and all other commits ahead this commit is in HEAD and other commits behind this commit is not in HEAD.
