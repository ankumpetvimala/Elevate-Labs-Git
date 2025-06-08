# Task 4: Build a Version-Controlled DevOps Project with Git

## Objective
To create a version-controlled Python text analyzer project using Git best practices, executed on an AWS EC2 t2.micro Ubuntu instance.

## Tools Used
- Git
- GitHub
- Python 3
- AWS EC2 t2.micro (Ubuntu 22.04 LTS)

## Setup
- Launched an EC2 t2.micro instance with Ubuntu 22.04 LTS.
- Installed Git and Python 3.
- Configured SSH access to GitHub for secure pushes.

## Steps Performed
1. Initialized a Git repository and linked it to GitHub.
2. Created `.gitignore` to ignore unnecessary files.
3. Added a detailed `README.md`.
4. Implemented the core text analyzer in `analyzer.py` (counts words, characters, sentences).
5. Created `main`, `dev`, and `feature/cli` branches.
6. Added a command-line interface in the `feature/cli` branch.
7. Used pull requests to merge `feature/cli` into `dev` and `dev` into `main`.
8. Resolved a simulated merge conflict (documented below).
9. Added a Git tag `v1.0.0` for the release.
10. Documented all steps in this file.

## Merge Conflict Resolution
- Created a conflict by modifying `analyzer.py` in both `dev` and `feature/cli`.
- Resolved by manually editing the conflicting lines to combine changes.
- Committed and pushed the resolution.

## Git Commands Used
- `git init`, `git add`, `git commit`, `git push`
- `git checkout -b`, `git branch`
- `git merge`, `git tag`
- `git remote add origin`

## Outcome
Learned Git workflows, branching strategies, pull requests, and conflict resolution, all within a cloud-based Ubuntu environment
