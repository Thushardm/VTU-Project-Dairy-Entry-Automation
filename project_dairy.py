import sys
import argparse
import time
import os

# --- Dependency Handling ---
try:
    import pandas as pd
    import requests
except ImportError:
    print("Error: Missing dependencies.")
    print("Please install them using: pip install pandas requests openpyxl")
    sys.exit(1)

# --- CONFIGURATION ---
LOGIN_URL = "https://vtuapi.internyet.in/api/v1/auth/login"
STORE_URL = "https://vtuapi.internyet.in/api/v1/student/project-diaries/store"

# REPLACED AS REQUESTED
PROJECT_ID = "your_project_id"  # Replace with your actual project ID (from the VTU portal using browser dev tools)

# --- COMPLETE SKILL MAPPING ---
SKILLS = {
    "JavaScript": "1", "PHP": "2", "Python": "3", "Laravel": "4", "CakePHP": "5",
    "WordPress": "6", "Flutter": "7", "FilamentPHP": "8", "React.js": "9", "Java": "10",
    "C++": "11", "AWS": "12", "Azure": "13", "Google Cloud": "14", "Machine learning": "15",
    "Data visualization": "16", "Statistical analysis": "17", "Network architecture": "18",
    "Database design": "19", "SQL": "20", "NoSQL": "21", "MongoDB": "22", "Cassandra": "23",
    "DevOps": "24", "TensorFlow": "25", "PyTorch": "26", "computer vision": "27",
    "Natural language processing": "28", "HTML": "29", "CSS": "30", "React": "31",
    "Angular": "32", "Vue.js": "33", "Node.js": "34", "Ruby on Rails": "35", "CodeIgniter": "36",
    "IaaS": "37", "PaaS": "38", "SaaS": "39", "Cloud access control": "40", "Data encryption": "41",
    "MySQL": "42", "PostgreSQL": "43", "Data modeling": "44", "Indexing": "45", "TCP/IP": "46",
    "DHCP": "47", "LAN": "48", "WAN": "49", "Firewall configuration": "50", "Keras": "51",
    "VPNs": "52", "scikit-learn": "53", "Tableau": "54", "Power BI": "55", "D3.js": "56",
    "Xamarin": "57", "Swift": "58", "Objective-C": "59", "Xcode": "60", "Android Studio": "61",
    "Kotlin": "62", "Git": "63", "Kubernetes": "64", "Docker": "65", "TypeScript": "66",
    "VLSI Design": "67", "Circuit Design": "68", "Layout Design": "69", "Physical Design": "70",
    "Digital Design": "71", "Design with FPGA": "72", "Verification & Validations": "73",
    "IoT": "74", "Embedded Systems": "75", "Intelligent Machines": "76",
    "BIM FOR CONSTRUCTION": "77", "BIM FOR ARCHITECTURE": "78", "INTERIOR AND EXTERIOR DESIGN": "79",
    "BIM FOR STRUCTURES": "80", "BIM FOR HIGHWAY ENGINEERING": "81", "PRODUCT DESIGN & 3D PRINTING": "82",
    "PRODUCT DESIGN & MANUFACTURING": "83", "BIM CONCEPTS WITH MEP AND PRODUCT DESIGN": "84",
    "3D PRINTING CONCEPTS, DESIGN AND PRINTING": "85", "Manufacturing": "86"
}

def validate_and_load_file(file_path):
    """Loads CSV/Excel and ensures all required columns are present."""
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            print("Error: Unsupported file format. Use .csv, .xls, or .xlsx.")
            sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    required_cols = ['date', 'description', 'hours', 'learnings', 'blockers', 'skills']
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"Error: Missing columns in file: {', '.join(missing)}")
        sys.exit(1)

    return df

def get_skill_ids(skills_str):
    """Maps a comma-separated string of skill names to their ID list."""
    if pd.isna(skills_str): return []
    names = [s.strip() for s in str(skills_str).split(',')]
    return [SKILLS[name] for name in names if name in SKILLS]

def main():
    parser = argparse.ArgumentParser(description="VTU Project Diary Automator via CLI")
    parser.add_argument("--email", required=True, help="Your portal login email")
    parser.add_argument("--password", required=True, help="Your portal login password")
    parser.add_argument("--file", required=True, help="Path to your Excel/CSV diary file")
    args = parser.parse_args()

    # Load and validate data
    df = validate_and_load_file(args.file)
    print(f"Successfully loaded {len(df)} entries.")

    session = requests.Session()

    # 1. Authentication
    try:
        print("Logging in...")
        auth_resp = session.post(LOGIN_URL, json={"email": args.email, "password": args.password})
        auth_resp.raise_for_status()
        token = auth_resp.json().get('token')
        headers = {
            "Authorization": f"Bearer {token}", 
            "Content-Type": "application/json", 
            "Accept": "application/json"
        }
        print("Authentication successful.")

        # 2. Sequential Posting
        
        for idx, row in df.iterrows():
            payload = {
                "project_id": PROJECT_ID,
                "date": str(row['date']).split(' ')[0], # Format YYYY-MM-DD
                "description": str(row['description']),
                "hours": float(row['hours']),
                "links": "",
                "blockers": str(row['blockers']) if not pd.isna(row['blockers']) else "",
                "learnings": str(row['learnings']) if not pd.isna(row['learnings']) else "",
                "mood_slider": 5,
                "skill_ids": get_skill_ids(row['skills'])
            }

            print(f"[{idx+1}/{len(df)}] Posting entry for {payload['date']}...")
            resp = session.post(STORE_URL, json=payload, headers=headers)
            
            if resp.status_code in [200, 201]:
                print("  Status: Success")
            else:
                print(f"  Status: Failed ({resp.status_code}) - {resp.text}")
            
            time.sleep(1.5) # Anti-spam delay

    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    main()