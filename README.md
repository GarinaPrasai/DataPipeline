Data Pipeline Project (Qualys + Crowdstrike)

This Python-based data pipeline project:
- Fetches host data from APIs (mocked or real)
- Normalizes and deduplicates records
- Stores in MongoDB (optional)
- Visualizes OS distribution and host recency

---

##  Features

-  Mock data mode for development (`TEST_MODE=true`)
-  MongoDB storage (auto-enabled when `TEST_MODE=false`)
-  Modular design (fetch → normalize → dedupe → store → visualize)
-  Plots: OS distribution & old vs. new hosts
-  `.env` driven configuration


## Project Structure

data_pipeline/
├── api_clients/ # Mock or real API clients
│ ├── qualys.py
│ └── crowdstrike.py
├── data_processing/ # Core pipeline logic
│ ├── fetch.py
│ ├── normalize.py
│ └── dedupe.py
├── models/ # Pydantic model for Host
│ └── host.py
├── utils/ # MongoDB and visualization utils
│ ├── mongodb.py
│ └── visualization.py
├── main.py # Entry point
├── requirements.txt
└── README.md


## Mock Mode vs Real Mode

| Mode | TEST_MODE | MongoDB | API Calls | Use Case |
|------|-----------|---------|-----------|----------|
| Development | `true` | Skipped | Mocked | Fast local testing |
| Production  | `false`| Required | Real | Full pipeline run |

---

## Setup Instructions

### 1. Clone + Set Up Virtual Environment

git clone <your-repo-url>
cd data_pipeline
python -m venv venv
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment
Create a .env file in the root:
# Set to true to run with mock data and no MongoDB
TEST_MODE=true

# Only used when TEST_MODE=false
QUALYS_TOKEN=your_qualys_api_token
CROWDSTRIKE_TOKEN=your_crowdstrike_api_token
MONGO_URI=mongodb://localhost:27017

Running the Pipeline
python main.py

In TEST_MODE=true:
Uses mock data from qualys.py and crowdstrike.py
Skips MongoDB completely
Generates visualizations

In TEST_MODE=false:
Connects to real Qualys and Crowdstrike APIs
Requires MongoDB running (local or Atlas)
Inserts deduplicated records into MongoDB

🧰 MongoDB Setup (Only for TEST_MODE=false)
Local (macOS)

brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community

Docker
docker run -d -p 27017:27017 --name mongo mongo:6

MongoDB Atlas (Cloud)
Create free cluster
Whitelist IP
Copy URI and set MONGO_URI in .env

Visual Output
Two matplotlib charts will be displayed:
1. OS Distribution: Bar chart of operating systems
2. Old vs New Hosts: Pie chart based on last_seen field

Requirements

numpy<2.0
matplotlib==3.7.1
pydantic==2.0.0
requests==2.28.2
pymongo==4.3.3
python-dotenv==1.0.0