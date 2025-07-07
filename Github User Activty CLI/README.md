


# GitHub User Activity CLI

A simple command-line interface (CLI) tool to fetch and display the recent activity of a GitHub user using the GitHub public API.

---

## 🚀 Features

- Fetches recent public events (e.g., pushes, stars, issues) of a GitHub user.
- Displays the activity in a readable format in the terminal.
- Handles invalid usernames and API errors gracefully.
- Lightweight, no external dependencies.

---

## 🧰 Technologies Used

- Python 3
- Standard libraries:
  - `sys`
  - `json`
  - `requests` *(You may already have this, or install via `pip install requests`)*

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Code-of-Asura-King/roadmap-projects.git
   cd roadmap-projects/Github\ User\ Activty\ CLI
````

2. **Install the required package (if not installed):**

   ```bash
   pip install requests
   ```

---

## ⚙️ Usage

```bash
python Github-User-Activity.py <github-username>
```

### Example

```bash
python Github-User-Activity.py kamranahmedse
```

### Output

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
...
```

---

## 🔧 Project Structure

```
Github-User-Activity-CLI/
│
├── Github-User-Activity.py   # Main CLI Script
└── README.md                 # Project Documentation
```

---

## 🐞 Error Handling

* Invalid GitHub username: Displays `Error 404` message.
* Network/API failure: Displays a proper error message without crashing.

---

## 📌 Notes

* GitHub API has a rate limit for unauthenticated requests (60 per hour). For more usage, you may need to use authentication.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* [GitHub REST API Docs](https://docs.github.com/en/rest)

```

---

Let me know if you want a version with badges, examples with color formatting, or enhanced styling for GitHub Pages!
```
