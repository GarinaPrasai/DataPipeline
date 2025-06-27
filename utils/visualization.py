import matplotlib.pyplot as plt
from typing import List

class HostVisualization:
    @staticmethod
    def plot_os_distribution(hosts: List[dict]):
        os_count = {}
        for host in hosts:
            os = host.get("os", "Unknown")
            os_count[os] = os_count.get(os, 0) + 1
        
        plt.bar(os_count.keys(), os_count.values())
        plt.xlabel("Operating System")
        plt.ylabel("Host Count")
        plt.title("Host Distribution by Operating System")
        plt.show()
    
    @staticmethod
    def plot_old_vs_new_hosts(hosts: List[dict]):
        old_hosts = [host for host in hosts if host["last_seen"] < "30 days ago"]
        new_hosts = [host for host in hosts if host["last_seen"] >= "30 days ago"]
        
        labels = ["Old Hosts", "New Hosts"]
        counts = [len(old_hosts), len(new_hosts)]
        
        plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title("Old vs New Hosts")
        plt.show()