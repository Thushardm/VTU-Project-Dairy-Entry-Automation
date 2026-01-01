# VTU Project Diary Automator

An automated Python utility designed to streamline the submission of project diary entries to the VTU Internyet portal. Instead of manual data entry, this script reads your diary from a CSV or Excel file and pushes it to the portal via REST API endpoints.

## 🚀 Features

- **Multi-format Support**: Reads data from both `.csv` and `.xlsx` files
- **Automated Authentication**: Logs in once and uses a Bearer Token for all subsequent entries
- **Auto Project Detection**: Automatically retrieves your project ID - no manual configuration needed
- **Flexible Date Formats**: Supports various date formats (DD-MM-YYYY, MM/DD/YYYY, DD/MM/YY, etc.)
- **Skill Mapping**: Automatically converts human-readable skill names (e.g., "Python") to the specific IDs required by the VTU database
- **Validation**: Checks for required columns and valid file paths before execution
- **Anti-Spam**: Implements a 1.5-second delay between posts to comply with server rate limits
- **Error Recovery**: Continues processing even if some entries fail

## 🛠️ Prerequisites

Ensure you have Python 3.x installed. Install the required libraries using pip:

```bash
pip install pandas requests openpyxl
```

## 📊 Data File Structure

Your Excel or CSV file must contain these headers:

| Header | Description | Example |
|--------|-------------|----------|
| date | Any common date format | 2025-01-07, 07-01-2025, 07/01/25 |
| description | Summary of the day's work | Technical discussion on GANs... |
| hours | Time spent (Numeric) | 8.0 |
| learnings | What was achieved/learned | Learned about generator loss functions. |
| blockers | Issues faced (Optional) | Hardware latency issues. |
| skills | Comma-separated names | Machine learning, Python |

## 💻 Usage

Run the script from your terminal/command prompt:

```bash
# Long form
python project_dairy.py --email "your_email@bit.edu" --password "your_password" --file "path/to/diary.xlsx"

# Short form (recommended)
python project_dairy.py -e "your_email@bit.edu" -p "your_password" -f "diary.xlsx"
```

### Command Line Arguments:
- `-e` or `--email`: Your registered portal email address
- `-p` or `--password`: Your portal password
- `-f` or `--file`: The path to your prepared Excel or CSV file

## ✨ What's New

- **No Setup Required**: Project ID is automatically detected from your account
- **Smart Date Parsing**: Handles various date formats automatically
- **Shorthand Commands**: Use `-e`, `-p`, `-f` for faster typing
- **Better Error Handling**: Skips invalid entries and continues processing