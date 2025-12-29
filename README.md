# MoodCutter

**MoodCutter** is an open-source Python project that automatically detects and extracts **funny** and **sad** moments from videos. The goal is to make emotional video clipping effortless and accessible for content creators, researchers, or anyone who wants to analyze video emotions.

---

## Features (v0.1)

- Detect laughter in videos (funny moments)
- Crop video segments automatically
- Command-line interface (CLI)
- Modular structure for easy extension

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/axtheon/MoodCutter.git
cd MoodCutter
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main module:

```bash
python src/main.py --input examples/sample_input.mp4 --mode funny
```

**Options:**
- `--input` : Path to your video file
- `--mode` : `funny` (v0.1 MVP). Future versions will support `sad` and other emotions.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Roadmap

- [ ] Add sad moment detection
- [ ] Support multiple emotion types
- [ ] GUI interface
- [ ] Batch processing support
- [ ] Export to multiple formats

---

**Made with ❤️ for content creators and video enthusiasts**
