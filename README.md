<p align="center">
  <img src="https://raw.githubusercontent.com/publicsensors/MicrocontrollerKits/master/images/PS_bannerLogo.png">
</p>

# MicrocontrollerKits
Accompanying code and materials for microcontroller kits. Code and materials are organized by [activity](http://www.publicsensors.org/intro-to-sensors/#).


## How to Contribute
For contributing materials to this repository, we are using the *Fork-Branch-Pull Request* workflow. Additional details on following this workflow using git from command line can be found in the [Data School Step-By-Step Guide](https://www.dataschool.io/how-to-contribute-on-github/). Overview lessons on using Git and GitHub can be found in both English and Spanish at [Software Carpentry](https://software-carpentry.org/lessons/).

Below are brief instructions specific to working within this repository.

##### 1. Fork the publicsensors/MicrocontrollerKits
* You only have to do this step once.
- Sign into https://github.com[GitHub] and navigate to the PublicSensors - MicrocontrollerKits repository at https://github.com/publicsensors/MicrocontrollerKits
- Fork the repository to your account by clicking on the <img src="https://raw.githubusercontent.com/publicsensors/MicrocontrollerKits/master/images/fork_button.png"> button.

TIP: Forking and cloning both create a copy of a repository, but forking is not a Git function. Forking is only done in GitHub and other hosting services. You fork a repository from another account to work on a copy of that project without affecting the original project. After forking a repository, you clone it to your computer to work on it locally.

Once the repository is forked to your GitHub account you can either edit the fork directly on GitHub (easy for if you are only editing text) or clone the repository to your computer and work locally. *We suggest cloning the repository to your computer.*

#### 2. Clone the forked repository to your computer
- You only have to do this step once.
  - Click on the repository to open it.
  - Click on the clone button. Use `Clone with HTTPS`.
  - Click on the clipboard button to save the URL to the clipboard.

1. Open the Git terminal and navigate to the directory (folder) you want to copy the repository to.  

2. Clone the forked repository to your computer. +
Format: 
`git clone https://github.com/_YOUR-USERNAME_/_YOUR-REPOSITORY_.git` 

3. After the local repository is on your computer, change directories again to enter it by typing `cd MicrocontrollerKits`. You have to be in the local repository to work on it. When you are in the repository, the branch name will be in parentheses at the end of the pathname.

#### 3. Add the upstream repository
You now have a copy of the forked repository on your computer, but what happens if there are changes in the upstream repository? How do you get those changes to your local repository? Remember, the upstream repository is the repository you forked from. The remote repository is in your GitHub account. The local repository is the repository on your computer. You need to tell Git what the upstream repository is in order to pull changes from it. This is called "adding the upstream repository" or "adding a remote".

You can first check your repository connections:
```bash
$ git remote -v
```
To add the original reposiory as the upstream :
```bash
$ git remote add upstream https://github.com/publicsensors/MicrocontrollerKits
```
Git does not produce output for this command, but you can verify that it has been added by once again using:
```bash
$ git remote -v
```

Now that the upstream repository is set, when the `publicsensors/MicrocontrollerKits` repository is updated you can pull those updates to your local repository. See the *Updating your forked repository* below.

#### 4. Create your branch
When working on a forked repository you should keep the `master` branch up to date and separate from your working branch. This allows you to mirror the upstream repository and reduce potential merge conflicts later. To create your own working branch, you "checkout" the branch. This command is also how you switch branches.

*NAMING your branch* - You can name your branch anything you want, but name it something descriptive so it is easy to track when merged. 

Create and switch to a new branch:
```bash
$ git checkout -b NEW_BRANCH
```
In your terminal you should notice the name of your branch in parentheses at the end of the pathname to your working directory.

Push your branch to your remote fork to begin tracking:
```bash
git push -u origin EL_doc_edits
```
When you push the branch from your local repository to your remote repository with the `-u` flag, tracking is set up between the two repositories. `-u` is short of `--set-upstream`

#### 5. Make your changes
Go ahead an add any files or make any changes in your repository directory.

#### 6. Stage and commit
After you have added/changed any files, stage it, and commit it to your local repository with a useful commit message. Staging files does two things. First, it tells Git which files to track. Second, once a file is being tracked, staging the file allows the changes to be committed to the repository. It is best practice to commit changes often. Each commit is a snapshot of the repository at that time. Building a series of commits creates a change log for the project.

You can always check the status of any changes using:
```bash
$ git status
```
You can add all of your files/changes using `.`, or insert the name of a specific file:
```bash
$ git add .
$ git commit -m "print multiple measurements on button"
```
The `.` in `$ git add .` tells Git to add all changes in the working directory to the staged area. Nothing is added to the local repository until you run a commit. Git requires a non-empty message with the commit. `-m` in `$git commit -m "print multiple measurements on button"` is the flag that adds the commit message. Commit messages must be surrounded by quotes. TIP: Commit messages with `-m` should be a short (50 characters or less) and concise subject line.

#### 7. Push edits to GitHub
Pushing to GitHub is how you update your remote repository. After you finish your updates and have committed the changes to your local repository, push the commits to your remote repository. 

```bash
$ git push
```

#### 8. Submit a Pull Request
After all your edits have been pushed to the remote repository (your fork on GitHub), submit a pull request to `publicsensors/MicrocontrollerKits`. A pull request tells others about the changes you made (all the commits), allows the convention coordinators to approve or deny your changes, and provides an area to discuss the changes if needed. It is called a pull request because you are asking the upstream repository to pull the changes from the branch of your fork. 

1. In GitHub, open your `MicrocontrollerKits` repository, and switch to your branch by clicking on the down arrow and choosing your branch.
2. Click on `Pull request`.
** If you want to see the differences between the branch of your forked repository and the upstream repository, click on `Compare`. Your additions will be highlighted in green and subtractions will be highlighted in red.
3. Make sure that the `master` branch of the base repository (`publicsensors/MicrocontrollerKits`) pulls the changes from the working branch of your repository.
4. Add a commit message and extra details in the text editor window, then click `Create pull request`. 

Once your pull request has been submitted, an organization administrator will be notified and will review your edits. Your edits will either be merged into the `publicsensors/MicrocontrollerKits` `master` branch or you might receive a reply back to you asking to clarify or update something. 

When your pull request has been merged, you will also be given the option to delete your now merged branch now that you are done with your branch edits. You can also delete the branch yourself with:
```bash
$ git branch -D NEW_BRANCH
```

#### Updating your forked repository
When you create a fork of a repository you only have the version of the files that are in the repository at that time. Assuming you made corrections and edits and submitted a pull request that was accepted, other pull requests and updates could occur to the upstream repository that won't be changed in your fork. Now you have an old copy of the forked repository and are out of sync with the upstream repo. To update your forked repository you have to "synchronize your fork", also known as "getting upstream updates", and you'll want to do it both before and after you plan to work on a new branch of the upstream repository.

1. Sync your local repository to the upstream
```bash
git pull upstream master
```
2. Now that your local version is updated, push those updates your remote fork (the "origin")
```bash
git pull origin master
```
