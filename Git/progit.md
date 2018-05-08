### The way Git thinks about its data

- A set of files and changes made to each file over time
<img src="images/data_store_vcs.jpg" width="60%" height="60%"/>

- A stream of snapshots
<img src="images/data_store_git.jpg" width="60%" height="60%"/>


### The three states
- modified
- staged
- committed

### The three main sections
- Working directory
- Staging area
- Git directory

### The basic workflow

<img src="images/git_states.jpg" width="60%" height="60%"/>

### Common-used command

#### git config
There are three different places to store git settings:
- /etc/gitconfig: for every users on the system, `--system`
- ~/.gitconfig or ~/.config/git/config: specific to your user, `--global`
- <working_dir>/.git/config: specific to the single repository

#### git diff
- git diff
- git diff --staged/--cached
- git difftool, run `git difftool --tool-help` to see what is available on your system.

#### git mv

#### git rm (-f)

#### git log (-p) (-2) (--stat) (--pretty=oneline) (--pretty=format:"%h %s" --graph)

#### git commit --amend
Undoing Things: the second commit replaces the results of the first.

```
git commit -m "initial commit"
git add forgotten_file
git commit --amend
```

#### git reset HEAD <file>
Unstaging a Staged file: 

#### git checkout -- <file>
Unmodifying a Modified file: git copys another file over it.
  



