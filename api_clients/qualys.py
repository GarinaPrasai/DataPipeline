import os
from typing import List

class QualysAPIClient:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.test_mode = os.getenv("TEST_MODE", "true").lower() == "true"
        self.base_url = "https://qualysapi.example.com"  # Placeholder for real API

    def fetch_hosts(self) -> List[dict]:
        if self.test_mode:
            print("[Qualys] 🔁 Using mock data (TEST_MODE=True)")
            return [
                {
                    "host_id": "q-001",
                    "hostname": "qualys-host-1",
                    "ip_address": "192.168.1.10",
                    "os": "Linux",
                    "last_seen": "2023-06-10"
                },
                {
                    "host_id": "q-002",
                    "hostname": "qualys-host-2",
                    "ip_address": "192.168.1.11",
                    "os": "Windows",
                    "last_seen": "2023-06-20"
                }
            ]
        else:
            import requests
            url = f"{self.base_url}/hosts"
            headers = {"Authorization": f"Bearer {self.api_token}"}
            response = requests.get(url, headers=headers)
            return response.json().get("hosts", [])
