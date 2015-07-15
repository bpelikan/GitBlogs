---
layout: default
comments: true
category: code
tags: [productivity]
title: Basic Git Commands
---
---

**Git** commands can be searched everywheere. Here I will list only the commonly used ones in **my** development.

First of all, try the following commands first:

* **git help:** get git basic commands.

* **git help COMMAND:** get help of a command.

###Check commit history

First, use **git log** to find the commit we want. We can use **git log --author=someone** to narrow the scope.

Then, use **git diff COMMIT^ COMMIT** to get all the changes of one commit.

###.gitignore

Sometimes we want to ignore some files/folders from being tracked by git. We can use **.gitignore** file to do this. But this only works for the untracked items. If you have done *git add file* to the file once, .gitignore will not exclude this file from being tracked. For this case, we can use the following two ways to ignore the file:

#####git rm \-\-cached file

This command will remove the file from the stage, and if you exclude the file in the **.gitignore**, it will not appear in the *untrancked files* list. But you will get a *deleted: file* in the *changes to be commited* list, and the next time you commit, the file in the repo will be deleted. 

If this is not what you want, and you only want to ignore the file locally, and don't want to remove it in the repo, because someone else may need this file, go to the second method.

#####git update-index \-\-assume-unchanged file

This method doesn't need **.gitignore**, and will not delete the file in the repo. The disadvantage is: when you clone the repo in other places, you need to run the command again.
