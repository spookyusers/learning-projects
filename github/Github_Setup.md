
# GitHub Setup and Workflow

Below is a summary of how a repository was set up on both a Linux home PC and a Windows laptop, including troubleshooting steps.

## 1. Creating the Repository on GitHub (Website Method)
- The repository `physics-326` was created via GitHub's website.
- It was initialized with a `README.md` file.

## 2. Setting Up Git on Linux Home PC
### Install Git:
```bash
sudo apt update
sudo apt install git
```

### Configure Git:
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Set Up SSH:
```bash
ssh-keygen -t ed25519 -C "youremail@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Clone the Repository:
```bash
git clone git@github.com:spookyusers/physics-326.git .
```

## 3. Setting Up Git on Windows Laptop
### Install Git for Windows:
- Download and install Git from [git-scm.com](https://git-scm.com/download/win).

### Configure Git:
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Set Up SSH:
```bash
ssh-keygen -t ed25519 -C "youremail@example.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

### Clone the Repository:
```bash
git clone git@github.com:spookyusers/physics-326.git .
```

## 4. Troubleshooting Issues

### Issue 1: Remote Repository Rejection (Divergent Branches)
- **Problem:** Error: `Updates were rejected because the remote contains work that you do not have locally.`
- **Solution:** Ran the following to pull and merge unrelated histories:
  ```bash
  git pull origin main --allow-unrelated-histories --no-rebase
  ```

### Issue 2: Directory Nested After Cloning
- **Problem:** Cloned the repository into a subfolder by mistake.
- **Solution:** Deleted the extra folder and re-cloned into the correct directory:
  ```bash
  git clone git@github.com:spookyusers/physics-326.git .
  ```

## 5. Syncing Changes Between Linux and Windows

1. **Making Changes on Either Machine:**
    ```bash
    git add .
    git commit -m "Describe your changes"
    git push origin main
    ```

2. **Syncing Changes on the Other Machine:**
    ```bash
    git pull origin main
    ```

This is the typical workflow to keep things synced between machines.

