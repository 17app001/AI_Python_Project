# Git Setup and Remote Repository Guide

## Git Repository Status

Your project is now initialized with Git version control!

### Current Status
- **Repository**: Initialized
- **Branch**: master
- **Initial Commit**: Completed (e6862b3)
- **Files Tracked**: 10 files
- **Working Tree**: Clean

## Files Committed

```
.gitignore                # Git ignore configuration
app.py                    # Streamlit GUI application
docs/startup_guide.md     # Launch instructions
docs/workflow_diagram.md  # System flowcharts
main.py                   # CLI application
requirements.txt          # Python dependencies
run_cli.bat              # CLI launcher script
run_gui.bat              # GUI launcher script
setup_and_run.bat        # Complete setup script
src/scraper.py           # Core scraping logic
```

## Connecting to Remote Repository

### Option 1: GitHub
```bash
# Create a new repository on GitHub first, then:
git remote add origin https://github.com/yourusername/taiwan-hot-stocks-scraper.git
git branch -M main
git push -u origin main
```

### Option 2: GitLab
```bash
# Create a new repository on GitLab first, then:
git remote add origin https://gitlab.com/yourusername/taiwan-hot-stocks-scraper.git
git branch -M main
git push -u origin main
```

### Option 3: Bitbucket
```bash
# Create a new repository on Bitbucket first, then:
git remote add origin https://bitbucket.org/yourusername/taiwan-hot-stocks-scraper.git
git branch -M main
git push -u origin main
```

## Git Commands Cheat Sheet

### Basic Commands
```bash
# Check status
git status

# View commit history
git log --oneline

# View changes
git diff

# Add files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to remote
git push

# Pull from remote
git pull
```

### Branch Management
```bash
# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name

# Create and switch branch
git checkout -b feature-name

# Merge branch
git merge feature-name

# Delete branch
git branch -d feature-name
```

## Recommended Git Workflow

### 1. Setup Remote Repository
1. Create repository on GitHub/GitLab/Bitbucket
2. Add remote origin
3. Push initial commit

### 2. Daily Development
```bash
# Start working
git checkout main
git pull origin main

# Create feature branch
git checkout -b new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push feature branch
git push origin new-feature
```

### 3. Merge and Deploy
```bash
# Switch to main
git checkout main

# Merge feature
git merge new-feature

# Push to main
git push origin main

# Delete feature branch
git branch -d new-feature
```

## .gitignore Configuration

The `.gitignore` file excludes:
- Python cache files (`__pycache__/`, `*.pyc`)
- Virtual environments (`venv/`, `env/`)
- IDE files (`.vscode/`, `.idea/`)
- Data files (`data/*.csv`, `data/*.json`)
- Log files (`logs/*.log`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Temporary files (`*.tmp`, `temp/`)

## Backup and Recovery

### Local Backup
```bash
# Create backup archive
git archive --format=zip HEAD > taiwan-stocks-scraper-backup.zip
```

### Clone Repository
```bash
# Clone from remote
git clone https://github.com/yourusername/taiwan-hot-stocks-scraper.git

# Setup after cloning
cd taiwan-hot-stocks-scraper
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Collaboration Workflow

### For Team Development
```bash
# 1. Fork repository (on GitHub/GitLab)
# 2. Clone your fork
git clone https://github.com/yourusername/taiwan-hot-stocks-scraper.git

# 3. Create feature branch
git checkout -b your-feature-name

# 4. Make changes and commit
git add .
git commit -m "Describe your changes"

# 5. Push to your fork
git push origin your-feature-name

# 6. Create Pull Request on original repository
```

## Release Management

### Tagging Releases
```bash
# Create tag
git tag -a v1.0.0 -m "First stable release"

# Push tags
git push origin --tags

# List tags
git tag -l
```

### Release Checklist
- [ ] Update version in files
- [ ] Test all features
- [ ] Update documentation
- [ ] Create release tag
- [ ] Write release notes

## Troubleshooting

### Common Issues

#### "Permission Denied" (SSH)
```bash
# Generate SSH key
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Add SSH key to GitHub/GitLab account
# Then use SSH URL:
git remote set-url origin git@github.com:yourusername/repo.git
```

#### "Remote Already Exists"
```bash
# Remove existing remote
git remote remove origin

# Add new remote
git remote add origin https://github.com/yourusername/repo.git
```

#### "Push Rejected"
```bash
# Force push (use carefully)
git push --force-with-lease origin main

# Or pull first
git pull origin main --rebase
git push origin main
```

## Best Practices

### Commit Messages
- Use present tense ("Add feature" not "Added feature")
- Be concise but descriptive
- Reference issue numbers if applicable

### Branch Naming
- `feature/description`
- `bugfix/description`
- `hotfix/description`

### Code Review
- Always review before merging
- Use pull requests for team collaboration
- Keep commits small and focused

## Security Considerations

- Never commit API keys or passwords
- Use environment variables for sensitive data
- Review `.gitignore` regularly
- Use private repositories for sensitive projects
