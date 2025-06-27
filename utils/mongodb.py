from dotenv import load_dotenv
import os

from data_processing.fetch import DataFetcher
from data_processing.normalize import DataNormalizer
from data_processing.dedupe import DataDeduper
from utils.visualization import HostVisualization

# Don't import MongoDB until needed
MongoDB = None

def main():
    global MongoDB  # So we can assign it conditionally
    load_dotenv()

    test_mode = os.getenv("TEST_MODE", "true").lower() == "true"
    qualys_token = os.getenv("QUALYS_TOKEN", "DUMMY")
    crowdstrike_token = os.getenv("CROWDSTRIKE_TOKEN", "DUMMY")

    print(f"🧪 TEST_MODE = {test_mode}")

    fetcher = DataFetcher(qualys_token, crowdstrike_token)
    hosts = fetcher.fetch_all_hosts()

    normalizer = DataNormalizer()
    normalized_hosts = normalizer.normalize_hosts(hosts)

    deduper = DataDeduper()
    deduped_hosts = deduper.dedupe_hosts(normalized_hosts)

    if test_mode:
        print("⚠️ TEST MODE ON: Skipping MongoDB insert")
    else:
        try:
            # Import only if needed
            from utils.mongodb import MongoDB
            db = MongoDB()
            db.insert_hosts(deduped_hosts)
            print("✅ Inserted deduplicated hosts into MongoDB")
        except Exception as e:
            print("❌ MongoDB connection failed or class could not be loaded.")
            print(f"   Error: {e}")
            return

    # Always visualize
    HostVisualization.plot_os_distribution(deduped_hosts)
    HostVisualization.plot_old_vs_new_hosts(deduped_hosts)

if __name__ == "__main__":
    main()
