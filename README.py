# Git-note

Git connection set up:

Create Personal Access Token on GitHub
From your GitHub account, go to Settings => Developer Settings => Personal Access Token => 
Generate New Token (Give your password) => Fillup the form => click Generate token => 
Copy the generated Token, it will be something like ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta

Now follow below method based on your machine:

For Windows OS ⤴
Go to Credential Manager from Control Panel => Windows Credentials => 
find git:https://github.com => Edit => On Password replace with with your GitHub Personal Access Token => You are Done

If you don’t find git:https://github.com => Click on Add a generic credential => 
Internet address will be git:https://github.com and you need to type in your username and password will be your 
GitHub Personal Access Token => Click Ok and you are done

For other OS, see the reference :

https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed-please-use-a-personal


1.Some important git command

1.0 Track remote branch(make branch visible in local) 
- To track all branchs :  
for i in `git branch -a | grep remote | grep -v HEAD | grep -v master`; do git branch --track ${i#remotes/origin/} $i; done
- To track one branch at a time :   
git checkout --track origin/branch-name 
- To link local branch to remote branch:
git branch --set-upstream-to=origin/main main  (link branch main in local to the branch main remote)

**
To download a remote branch to local : suppose that if you have 4 branchs in remote and 1 branch in the local, you can download remote branch by doing the command:
git checkout origin/branch_A
git checkout branch_A
=> now you can see branch_A in your local branchs.

1.1 Git checkout 
- To create new branch on Local 
  * git checkout -b [name_of_your_new_branch]
- To create new branch on remote
  * git push --set-upstream origin [name_of_your_new_branch]
- Sometimes there is 2 branch with different files and you want to switch between them(in other words, the index of the working tree differs from HEAD or you have un-staged changes)    
  * git checkout -f branch_name    

1.2 Restore files back to the state of repository
- To restore one file
  * git checkout -- "name of file"
- To restore everything
  * git checkout -- .

1.3 Join two or more development histories together(git merge)  
Reference : https://www.atlassian.com/git/tutorials/using-branches/git-merge  

Git merge will combine multiple sequences of commits into one unified history. In the most frequent use cases, git merge is used to combine two branches. If the repo of remote branch is ahead the repo of local branch, then there will be no conflict. Otherwise we have to solve conflict to merge. To be resolve conflict :   
https://swcarpentry.github.io/git-novice/09-conflict/

Command :     
- Merge 2 branch in local repo : git merge [name of branch need to merge to current branch]
- Merge local branch to remote branch : git merge  

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

1.7 Git reset
1.7.1 git reset --soft
The --soft aims to change the HEAD (where the last commit is in your local machine) reference to a specific commit. 
For instance, if we realize that we forgot to add a file to the commit, we can move back using the --soft with respect to the following format:                                                                   
- git reset --soft HEAD~n to move back to the commit with a specific reference (n). 
- git reset --soft HEAD~1 gets back to the last commit.
- git reset --soft <commit ID> moves back to the head with the <commit ID>                                                                                                
Ex : 
You have 3 files you want to commit (data_acquisition.py data_preprocessing.py model_training.py), then you do :
git add data_acquisition.py data_preprocessing.py
git add data
git commit -m "added data acquisition and preprocessing scripts"
But you reliazed that you forgot to add file  model_training.py, then you can do "git reset --soft HEAD~1", to come back the previous commit to add the remain file.

1.7.2 git reset --mixed
This is the default argument for git reset. Running this command has two impacts: 
(1) uncommit all the changes and 
(2) unstage them. 
Imagine that we accidentally added the model_training.py file, and we want to remove it because the model training is not finished yet. 
Here is how to proceed: 
- Unstage the files that were in the commit with git reset HEAD~n
- Only add the files we need for the commit
Syntax:
- git reset HEAD~n to move back to the commit with a specific reference (n). 
- git reset HEAD~1 gets back to the last commit.
- git reset <commit ID> moves back to the head with the <commit ID>   

1.7.3 git reset --hard
This option has the potential of being dangerous. So, be cautious when using it! 
Basically, when using the hard reset on a specific commit, it forces the HEAD to get back to that commit and deletes everything else after that.

So if in the staging area of the previous commit has a file model_training.py, then you do "git reset --hard HEAD~1", then the file model_training.py will be delete completely 
in both stagging area and in your folder, so please use it carefully !!!!!                                                                                          

Reference:
```
https://www.datacamp.com/tutorial/git-reset-revert-tutorial
```
1.7 Git revert 
Git revert is similar to git reset, but the approach is slightly different. Instead of removing all the commits in its way, the revert ONLY undoes a single commit 
by taking you back to the staged files before the commit.
So, instead of removing a commit, git revert inverts the changes introduced by the original commit by creating a new commit with the underlying inverse content. 
This is a safe way to revoke a commit because it prevents you from losing your history.
Syntax:
- git revert --no-edit <commit ID> : The --no-edit option allows the user to not change the message used for the commit you attend to revert, and this will make git revert file to master branch.
- git revert <commit ID>
Reference:
```
https://www.datacamp.com/tutorial/git-reset-revert-tutorial
```                                                                                                
1.7 Git rebase
Note that git rebase only suitable when you work alone, not with the team. Git rebase work the same as git merge. The difference is :
- Git merge merge 2 branches together but the existing branches are not changed in any way.
- Git rebase merge 2 branches together but it become one branch after the merger, which make the history of the branch is linear. Easy to review and debug => this is the main benefit of using git rebase                                                                                               
                                                                                                
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
Reference : https://www.atlassian.com/git/tutorials/syncing/git-pull 
- Git pull is just the combination of git fetch and git merge. The git pull command first runs git fetch which downloads content from the specified remote repository. Then a git merge is executed to merge the remote content refs and heads into a new local merge commit.

1.10 Git stash
Good Reference:
- https://cafedev.vn/tu-hoc-git-lenh-git-stash/?fbclid=IwAR1r9HHeUd6brsRJKOkMeAZ2hADFakrh6csOhqBfD0kxr_9SvpRJ_blxeyg

1.11 Git commit amend
Update pervious unpushed commit               

git commit --amend -m "New commit message" 

Note that git commit --amend can only work with unpushed commit, for pushed commit it will cause conflict
                    
1.12 Git reset hard
Reset to the previous state:
git reset --hard           
Alternatively, reset to a particular point in time, such as:
git reset --hard master@{"10 minutes ago"}
Reset by chose a specific state:
git reset --hard a0d3fe6
where a0d3fe6 is found by doing:
git reflog                    
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




2.2 Git ignore 
Show ignore files : git status --ignored
Add ignore files : add file name in .gitignore(only work if the file is not in tracked files, if the file is already in tracked files, 
we need to do : git rm --cached file_name first)
                    
                 
                  



Note:
- In the new version, original "master" branch was renamed to "main"
- HEAD is Git’s way of referring to the current snapshot or a pointer. Internally, the git checkout command simply updates the HEAD to point to either the specified branch or commit. When it points to a branch, Git doesn't complain, but when you check out a commit, it switches into a “detached HEAD” state. To be more specific :  
When HEAD point to a single commit on a branch, for example on 527f799, It will show something like "(HEAD detached at 527f799)", and all other commits ahead this commit is in HEAD and other commits behind this commit is not in HEAD.


# Update git credential after change password in git
If we change password in git in the website, probably when we push the code, we will have the authenticaion error, in this case, you should use ssh connection. Ask ChatGPT how to create token SSH then update config in local machine.

Sometime Assystem network does not allow you push the code on git even using guestWifi, in this case, use 3G instead
