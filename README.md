# VTU Project Diary Automator

An automated Python utility designed to streamline the submission of project diary entries to the VTU Internyet portal. Instead of manual data entry, this script reads your diary from a CSV or Excel file and pushes it to the portal via REST API endpoints.

## 🚀 Features

- **Multi-format Support**: Reads data from both `.csv` and `.xlsx` files
- **Automated Authentication**: Logs in once and uses a Bearer Token for all subsequent entries
- **Skill Mapping**: Automatically converts human-readable skill names (e.g., "Python") to the specific IDs required by the VTU database
- **Validation**: Checks for required columns and valid file paths before execution
- **Anti-Spam**: Implements a 1.5-second delay between posts to comply with server rate limits

## 🛠️ Prerequisites

Ensure you have Python 3.x installed. Install the required libraries using pip:

```bash
pip install pandas requests openpyxl
```

## ⚙️ Setup & Configuration

### Obtain Project ID:
1. Log into the VTU portal in your browser
2. Open Developer Tools (F12) and go to the Network tab
3. Submit one diary entry manually
4. Find the store request and look for the `project_id` in the payload (e.g., 3311)

### Update the Script:
Open `vtu_automator.py` and replace the placeholder in `PROJECT_ID = "your_project_id"` with your actual ID.

## 📊 Data File Structure

Your Excel or CSV file must contain these headers:

| Header | Description | Example |
|--------|-------------|----------|
| date | YYYY-MM-DD | 2025-01-07 |
| description | Summary of the day's work | Technical discussion on GANs... |
| hours | Time spent (Numeric) | 8.0 |
| learnings | What was achieved/learned | Learned about generator loss functions. |
| blockers | Issues faced (Optional) | Hardware latency issues. |
| skills | Comma-separated names | Machine learning, Python |

## 💻 Usage

Run the script from your terminal/command prompt:

```bash
python project_dairy.py --email "your_email" --password "your_password" --file "path/to/diary.xlsx"
```

### Command Line Arguments:
- `--email`: Your registered portal email address
- `--password`: Your portal password
- `--file`: The path to your prepared Excel or CSV file