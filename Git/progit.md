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


### Git config
There are three different places to store git settings:
- /etc/gitconfig: for every users on the system, `--system`
- ~/.gitconfig or ~/.config/git/config: specific to your user, `--global`
- <working_dir>/.git/config: specific to the single repository

