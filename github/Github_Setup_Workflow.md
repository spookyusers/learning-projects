

# GitHub Workflow Document

## 1. Setting Up Git and GitHub
Before you begin, ensure that Git is installed on your Linux PC:

```bash
sudo apt-get update
sudo apt-get install git
```

Configure your Git user name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Setting Up SSH Keys (Recommended)
Setting up SSH keys allows for secure communication with GitHub without repeatedly entering your username and password.

Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

If your system doesn't support Ed25519, use:

```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

Add your SSH key to the ssh-agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy the SSH key to your clipboard:

```bash
sudo apt-get install xclip
xclip -sel clip < ~/.ssh/id_ed25519.pub
```

Add the SSH key to your GitHub account:

- Log in to GitHub.
- Go to Settings > SSH and GPG keys > New SSH key.
- Paste the key and click Add SSH key.

Test your SSH connection:

```bash
ssh -T git@github.com
```

## 2. Creating a New Repository
On GitHub:

- Click the + icon and select New repository.
- Fill in the repository details (name, description, visibility).
- Do not initialize with a README, .gitignore, or license (since you'll add them locally).
- Click Create repository.

Clone the repository locally:

```bash
git clone git@github.com:yourusername/repository-name.git
```

Replace `yourusername` and `repository-name` with your GitHub username and repository name.

## 3. Setting Up Local Folders and Files
Navigate to your repository:

```bash
cd repository-name
```

Create new folders as needed:

```bash
mkdir foldername
```

Move existing files into the repository:

```bash
mv /path/to/file foldername/
```

## 4. Creating a .gitignore File
A .gitignore file specifies intentionally untracked files to ignore:

```bash
touch .gitignore
```

Edit .gitignore and add files or patterns to exclude:

```bash
# Ignore node_modules folder
node_modules/

# Ignore all .log files
*.log
```

## 5. Adding Files and Folders to Staging
Add individual files:

```bash
git add filename
```

Add all changes in the current directory (including deletions):

```bash
git add -A
```

Verify the staging area:

```bash
git status
```

## 6. Committing Changes
Commit the staged changes with a descriptive message:

```bash
git commit -m "Add initial project files"
```

### Best Practices for Commit Messages:
- Use the present tense ("Add feature" not "Added feature").
- Keep the message concise but descriptive.

## 7. Pushing Changes to GitHub
Push your commits to the remote repository:

```bash
git push origin main
```

If your default branch is `master`, replace `main` with `master`.

## 8. Pulling Changes from GitHub
Before starting new work, ensure your local repository is up-to-date:

```bash
git pull origin main
```

## 9. Syncing Across Multiple Machines
On another machine:

Clone the repository (if not already cloned):

```bash
git clone git@github.com:yourusername/repository-name.git
```

Navigate to the repository:

```bash
cd repository-name
```

Pull the latest changes:

```bash
git pull origin main
```

After making changes, repeat the add, commit, and push steps.

## 10. Working with Branches (Optional but Recommended)
Using branches helps manage different features or fixes without affecting the main codebase.

Create a new branch:

```bash
git checkout -b feature-branch-name
```

Switch between branches:

```bash
git checkout main
```

After making changes, push the branch to GitHub:

```bash
git push origin feature-branch-name
```

### Merge changes back to main:
- Create a Pull Request on GitHub and merge.

Or merge locally:

```bash
git checkout main
git merge feature-branch-name
```

## 11. Best Practices
- **Regular Commits:** Commit changes frequently with meaningful messages.
- **Pull Before You Push:** Always pull the latest changes before pushing to avoid conflicts.
- **Use .gitignore:** Keep unnecessary files out of your repository.
- **Branching:** Use branches for new features or fixes.
- **Code Reviews:** If collaborating, use Pull Requests for code reviews.

---

### Next Steps
This workflow will help keep your projects organized and synchronized across multiple machines. Save this document to your `learning-projects/github` folder for future reference.
