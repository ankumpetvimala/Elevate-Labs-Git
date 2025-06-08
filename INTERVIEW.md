# DevOps Interview Questions & Answers

## Git Fundamentals

### 1. What is Git?
Git is a distributed version control system that:
- Tracks changes in source code
- Enables collaboration among developers
- Maintains complete history of changes
- Allows branching and merging workflows

### 2. What is the difference between merge and rebase?
| Merge | Rebase |
|-------|--------|
| Creates a new merge commit | Rewrites commit history |
| Preserves branch history | Creates linear history |
| Non-destructive operation | Changes commit SHAs |
| Command: `git merge` | Command: `git rebase` |

## Git Operations

### 3. What is a pull request?
A pull request (PR) is:
- A request to merge changes from one branch to another
- A code review mechanism
- A discussion platform for proposed changes
- Common workflow in GitHub/GitLab

Example workflow:
```bash
git checkout -b feature/new-login
# Make changes...
git add .
git commit -m "Add new login feature"
git push origin feature/new-login
# Then create PR on GitHub
```

### 4. How do you resolve merge conflicts?
Step-by-step resolution:
1. Identify conflicts: `git status`
2. Open files with conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Edit to keep desired changes
4. Remove conflict markers
5. Mark as resolved: `git add <file>`
6. Complete merge: `git commit`

## Advanced Concepts

### 5. What are Git tags?
Git tags are reference points in Git history used for:
- Version releases (v1.0, v2.0)
- Important milestones
- Stable points in code

Commands:
```bash
git tag -a v1.0 -m "Release version 1.0"  # Create annotated tag
git push origin v1.0                       # Push tag to remote
```

### 6. What is Git workflow?
Common workflows include:
1. **Feature Branch Workflow**  
   - Isolate features in branches
   - Merge via PRs
2. **Gitflow Workflow**  
   - Uses main/develop/feature branches
   - Strict release process
3. **Forking Workflow**  
   - Contributors fork main repo
   - Changes via PRs

## Git Utilities

### 7. Explain git stash
`git stash` temporarily shelves changes to:
- Switch branches cleanly
- Save WIP without commits
- Clean working directory

Usage:
```bash
git stash        # Save changes
git stash list   # View stashes
git stash pop    # Reapply changes
```

### 8. What is the use of .gitignore?
The `.gitignore` file tells Git which files to ignore, such as:
- Build artifacts (`/dist/`, `*.class`)
- Dependencies (`node_modules/`)
- Environment files (`.env`)
- IDE files (`.vscode/`, `.idea/`)

Example:
```
# Ignore all .log files
*.log

# Except important.log
!important.log

# Ignore build directory
/build/
```
