# Contributing to MoodCutter

Thank you for your interest in contributing to **MoodCutter**! We welcome contributions from everyone, whether you're fixing a bug, adding a feature, or improving documentation.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

---

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to learn and build something great together.

---

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/axtheon/MoodCutter.git
   cd MoodCutter
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/axtheon/MoodCutter.git
   ```

---

## How to Contribute

### Types of Contributions We Love

- 🐛 **Bug fixes**
- ✨ **New features** (emotion detection algorithms, export formats, etc.)
- 📚 **Documentation improvements**
- 🧪 **Tests** (unit tests, integration tests)
- 🎨 **UI/UX improvements**
- 🌍 **Translations**
- 💡 **Ideas and suggestions**

---

## Development Setup

1. **Install dependencies** (including dev tools):
   ```bash
   pip install -r requirements.txt
   ```

2. **Install development dependencies**:
   ```bash
   # Uncomment dev dependencies in requirements.txt or install manually:
   pip install black pylint pytest
   ```

3. **Verify your setup**:
   ```bash
   python src/main.py --input examples/sample_input.mp4 --mode funny
   ```

---

## Coding Standards

### Python Style Guide

- Follow **PEP 8** style guidelines
- Use **meaningful variable names**
- Add **docstrings** to functions and classes
- Keep functions **focused and small**

### Code Formatting

We use `black` for automatic code formatting:

```bash
black src/
```

### Linting

Run `pylint` before committing:

```bash
pylint src/
```

### Example Function

```python
def detect_laughter(audio_path: str, threshold: float = 0.8) -> list:
    """
    Detect laughter in audio file.

    Args:
        audio_path: Path to the audio file
        threshold: Confidence threshold for detection (0.0-1.0)

    Returns:
        List of tuples containing (start_time, end_time) of laughter segments
    """
    # Implementation here
    pass
```

---

## Submitting Changes

### Step-by-Step Process

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit them:
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

3. **Keep your branch updated** with upstream:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what you changed and why
   - Reference any related issues (e.g., "Fixes #123")

### Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a verb: `Add`, `Fix`, `Update`, `Remove`, `Refactor`
- Keep the first line under 50 characters
- Add detailed description if needed after a blank line

**Examples:**
```
Add sad moment detection algorithm

Implement basic sad moment detection using audio analysis
and facial expression recognition. Includes unit tests.
```

```
Fix video cropping bug for vertical videos

Resolves issue where vertical videos were being cropped
incorrectly. Fixes #42.
```

---

## Reporting Bugs

Found a bug? Please create an issue with:

- **Clear title** describing the bug
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **System information** (OS, Python version, etc.)
- **Error messages or logs** (if any)
- **Screenshots or videos** (if applicable)

### Bug Report Template

```markdown
**Description:**
Brief description of the bug

**To Reproduce:**
1. Run command '...'
2. Use video file '...'
3. See error

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.10.5]
- MoodCutter Version: [e.g., v0.1]

**Additional Context:**
Any other relevant information
```

---

## Feature Requests

Have an idea? We'd love to hear it!

Create an issue with:
- **Clear description** of the feature
- **Use case** - why would this be useful?
- **Possible implementation** (if you have ideas)
- **Examples** from other projects (if relevant)

---

## Questions?

- Open an issue with the `question` label
- Check existing issues to see if your question has been answered
- Be patient and respectful - maintainers are often volunteers

---

## Recognition

Contributors will be acknowledged in:
- The project README
- Release notes
- Our hearts ❤️

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**Thank you for making MoodCutter better!** 🎉
