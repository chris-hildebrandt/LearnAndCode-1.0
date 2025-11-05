# **Week 5: GIT - Examples**

In this section, we provide examples of common Git tasks that you will encounter while working on your project.

## **Table of Contents**

- **[Example 1: Interactive Rebase](#example-1-interactive-rebase)**
- **[Example 2: Cherry-picking Commits](#example-2-cherry-picking-commits)**
- **[Example 3: Squashing Commits](#example-3-squashing-commits)**
- **[Example 4: Reverting a Commit](#example-4-reverting-a-commit)**

## **Example 1: Interactive Rebase**

Interactive rebasing allows you to modify your commit history by reordering, editing, squashing, or dropping commits. To perform an interactive rebase, use **`git rebase -i`** followed by the commit hash or branch reference:

```bash
git rebase -i HEAD~3
```

This command will open an editor with a list of the last three commits. You can change the commands (e.g., **`pick`**, **`reword`**, **`edit`**, **`squash`**, **`fixup`**, **`exec`**, **`drop`**) in front of each commit to modify your commit history as needed.

## **Example 2: Cherry-picking Commits**

Cherry-picking allows you to apply specific commits from one branch to another. To cherry-pick a commit, first checkout the target branch:

```bash
git checkout target-branch

```

Next, use the **`git cherry-pick`** command followed by the commit hash you want to apply:

```bash
git cherry-pick commit-hash

```

This command applies the specified commit to the target branch.

## **Example 3: Squashing Commits**

Squashing commits is useful when you want to combine multiple commits into a single commit. You can squash commits using interactive rebase:

```bash
git rebase -i HEAD~3

```

In the editor, change the command for the commits you want to squash from **`pick`** to **`squash`** or **`fixup`**. Save and close the editor. Git will then squash the specified commits into a single commit.

## **Example 4: Reverting a Commit**

Reverting a commit creates a new commit that undoes the changes made in a specific commit. To revert a commit, use the **`git revert`** command followed by the commit hash:

```bash
git revert commit-hash

```

This command will create a new commit that undoes the changes made in the specified commit.
