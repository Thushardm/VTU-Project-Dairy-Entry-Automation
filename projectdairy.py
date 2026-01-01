import requests
import time

# --- CONFIGURATION ---
LOGIN_URL = "https://vtuapi.internyet.in/api/v1/auth/login"
STORE_URL = "https://vtuapi.internyet.in/api/v1/student/project-diaries/store"

EMAIL = "your_email_id" 
PASSWORD = "your_password"
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

# --- PROJECT DIARY ENTRIES ---
# Add your entries to this list. Follow the commented-out template below.
diary_entries = [
    # {
    #     "date": "2025-01-07",
    #     "desc": "General technical discussion on Machine Learning models and Web scalability.",
    #     "hours": 8.0,
    #     "learn": "Deep dive into CNN architectures and Flask API optimization.",
    #     "block": "Hardware limitations during local model testing.",
    #     "skills": [SKILLS["Machine learning"], SKILLS["Python"]]
    # },
]

def automate_vtu_portal():
    if not diary_entries:
        print("No entries found in the list. Please add entries to the 'diary_entries' variable.")
        return

    session = requests.Session()
    
    # 1. Login to retrieve Bearer Token
    try:
        print("Attempting to login...")
        login_data = {"email": EMAIL, "password": PASSWORD}
        auth_resp = session.post(LOGIN_URL, json=login_data)
        auth_resp.raise_for_status()
        
        token = auth_resp.json().get('token')
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        print("Login Successful. Token acquired.")

        # 2. Iterate and Submit
        for entry in diary_entries:
            payload = {
                "project_id": PROJECT_ID,
                "date": entry["date"],
                "description": entry["desc"],
                "hours": entry["hours"],
                "links": "",
                "blockers": entry["block"],
                "learnings": entry["learn"],
                "mood_slider": 5,
                "skill_ids": entry["skills"]
            }
            
            print(f"Submitting entry for {entry['date']}...")
            resp = session.post(STORE_URL, json=payload, headers=headers)
            
            if resp.status_code in [200, 201]:
                print(f"Successfully posted: {entry['date']}")
            else:
                print(f"Failed for {entry['date']}: {resp.status_code} - {resp.text}")
            
            # Pause to prevent rate limiting
            time.sleep(1.5)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    automate_vtu_portal()