# Ticket Manager CLI

A simple command-line ticket manager built with Python. Created for practicing Git workflows, branching, merging, rebasing, pull requests, and CI/CD.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

## Run Tests

```bash
pytest tests/ -v
```

## Features

- View open tickets
- Add new tickets
- Close tickets
- Delete tickets
- Search tickets by keyword
- Get ticket by ID
- Count total tickets
- Priority levels for tickets
- Persistent storage via JSON

## Git Skills Practiced

| Skill | Command | What it does |
|---|---|---|
| Init | `git init` | Start tracking a folder |
| Stage | `git add` | Pick files to save |
| Commit | `git commit -m "msg"` | Save a snapshot |
| Branch | `git checkout -b name` | Work on a separate copy |
| Merge | `git merge branch` | Combine branches |
| Conflicts | Edit markers, add, commit | Fix competing changes |
| Push | `git push` | Upload to GitHub |
| Pull | `git pull` | Download from GitHub |
| Pull Request | Open on GitHub | Ask for review before merge |
| Rebase | `git rebase main` | Clean linear history |
| Stash | `git stash` / `git stash pop` | Pause and resume work |
| Amend | `git commit --amend` | Fix last commit |
| Cherry-pick | `git cherry-pick hash` | Grab one specific commit |
| Reset | `git reset HEAD~1` | Undo commits |
| Tags | `git tag v1.0` | Mark a release |

## CI/CD

This project uses GitHub Actions to automatically run tests on every push and pull request. See `.github/workflows/ci.yml`.

## Contributing

Pull requests are welcome.

## License

MIT
