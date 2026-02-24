Microsoft Windows [Version 10.0.26200.7840]
(c) Microsoft Corporation. All rights reserved.

C:\Users\ajeys>mkdir ml-project

C:\Users\ajeys>cd ml-project

C:\Users\ajeys\ml-project>git init
Initialized empty Git repository in C:/Users/ajeys/ml-project/.git/

C:\Users\ajeys\ml-project>touch train.py utils.py predict.py README.md
'touch' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\ajeys\ml-project>type nul > train.py

C:\Users\ajeys\ml-project>type nul > utils.py

C:\Users\ajeys\ml-project>type nul > predict.py

C:\Users\ajeys\ml-project>type nul > README.md

C:\Users\ajeys\ml-project>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        predict.py
        train.py
        utils.py

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\ajeys\ml-project>git init
Reinitialized existing Git repository in C:/Users/ajeys/ml-project/.git/

C:\Users\ajeys\ml-project>git add .

C:\Users\ajeys\ml-project>git commit -m "Initial commit"
[main a7a63bf] Initial commit
 2 files changed, 74 insertions(+)
 create mode 100644 README.md
 create mode 100644 predict.py

C:\Users\ajeys\ml-project>gh repo create ml-project --public --source=. --remote=origin --push


C:\Users\ajeys\ml-project>git add train.py utils.py

C:\Users\ajeys\ml-project>git commit -m "Add training script and utilities"
[main (root-commit) e01c133] Add training script and utilities
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 train.py
 create mode 100644 utils.py

C:\Users\ajeys\ml-project>git config --global user.name "Ajey Srinivasu"

C:\Users\ajeys\ml-project>git config --global user.email "ajeysrini@gmail.com"

C:\Users\ajeys\ml-project>git branch -M main

C:\Users\ajeys\ml-project>git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 231 bytes | 231.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/AjeySrini/ml-project.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

C:\Users\ajeys\ml-project>git add train.py utils.py

C:\Users\ajeys\ml-project>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        predict.py

nothing added to commit but untracked files present (use "git add" to track)

Changes from team mate then i will do git pull in local 

Below command to get remote changes got the above lines


C:\Users\ajeys\ml-project>git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 1.93 KiB | 141.00 KiB/s, done.
From https://github.com/AjeySrini/ml-project
   91734d5..fc40eda  main       -> origin/main
Updating 91734d5..fc40eda
Fast-forward
 README.md  | 2 ++
 predict.py | 4 +++-
 2 files changed, 5 insertions(+), 1 deletion(-)

C:\Users\ajeys\ml-project>git pull origin main
From https://github.com/AjeySrini/ml-project
 * branch            main       -> FETCH_HEAD
Already up to date.


C:\Users\ajeys\ml-project>type nul > config.py

To check status of file to track 


C:\Users\ajeys\ml-project>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   utils.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        config.py

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\ajeys\ml-project>git add .

C:\Users\ajeys\ml-project>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        new file:   config.py
        modified:   utils.py

Commit the changes with commit msg

C:\Users\ajeys\ml-project>git commit -m "Update utilities and add config file"
[main af3102a] Update utilities and add config file
 3 files changed, 47 insertions(+)
 create mode 100644 config.py

push to github

C:\Users\ajeys\ml-project>git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 977 bytes | 977.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/AjeySrini/ml-project.git
   fc40eda..af3102a  main -> main



