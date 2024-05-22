## Git interview question

[Sanofi] How gitflow work ?

The workflow is great for a release-based software workflow. The overall flow of Gitflow is:

1. A develop branch is created from main
2. Feature branches are created from develop
3. A release branch is created from develop (Where there are enough features to realease)
4. When a feature is complete it is merged into the develop branch
5. When the release branch is done it is merged into develop and main
6. If an issue in main is detected a hotfix branch is created from main
7. Once the hotfix is complete it is merged to both develop and main

For more details:
```
https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
```

[Sanofi] What is hotfix in git ?

1. Purpose:
Hotfix branches are created to fix urgent problems that need to be resolved immediately in the production environment.
They allow developers to work on the fix independently from ongoing development work and release the fix quickly without waiting for the next scheduled release.

2. Workflow:
To create a hotfix, you typically branch off from the "main branch" (e.g., master) instead of the development branch.
Once the hotfix branch is created, you make the necessary changes to resolve the critical issue.
After the hotfix is tested and verified, it is merged back into both the main branch and the development branch to ensure that the fix is included in future releases.

3. Naming Convention:
Hotfix branches are often named with a specific prefix (e.g., hotfix/) followed by a descriptive name that indicates the issue being addressed.

4. Best Practices:
It's important to communicate clearly with the team when creating and applying hotfixes to ensure everyone is aware of the changes being made.
Hotfixes should be well-tested to avoid introducing new issues while resolving the urgent problem.

By using hotfix branches in Git, development teams can effectively manage and deploy critical fixes to production environments in a controlled and efficient manner.


[Sanofi] V3.0 was released but users reported a bug in an old feature which was stable prior to this release(V2.0). Please specfiy what may happened? select all that apply

1. Developers produced a bug in a new feature branch that was missed while testing
2. The developers forgot to merge the feature branch into development before creating a release branch
3. The developers forgot to merge the hotfix with the feature branch
4. The developers forgot to merge the hotfix with the development branch
5. None of the above

Answer :
Based on the scenario described, the following reasons could have led to the bug being present in an old stable feature:

1. Developers produced a bug in a new feature branch that was missed while testing
This is a possibility where a bug was introduced in a new feature branch and was not caught during testing, leading to its presence in the release.

2. The developers forgot to merge the feature branch into development before creating a release branch
If the feature branch containing the bug fixes or changes was not merged into the development branch before creating the release branch for V3.0, the bug would not have been included in the release.

4. The developers forgot to merge the hotfix with the development branch
Rembember that hotfix is fork from main branch, then after we do the bug fix, we need to merge hotfix branch to main branch and development branch. If the hotfix was not merged back into the development branch, the bug would persist in the V3.0 release.

The answer 3 is not nessessary because normally hotfix branch is created to fix urgent problems and it needs to be merge back to main branch and development branch. The release 3.0 branch is based on development branch, so as long as development branch solve the old feature bug, then release 3.0 branch will not have this bug any more. So it's not obligate to merge the hotfix with the feature branch 

