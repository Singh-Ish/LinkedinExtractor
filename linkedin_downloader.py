import requests
import json
from datetime import datetime
import os
import time
from typing import Optional
import sys
from pathlib import Path
from dotenv import load_dotenv

class LinkedInDownloader:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variable with error handling
        self.api_key = os.getenv('SCRAPIN_API_KEY')
        if not self.api_key:
            raise ValueError("SCRAPIN_API_KEY not found in environment variables. Please check your .env file.")
            
        self.base_url = "https://api.scrapin.io/enrichment/profile"
        self.output_dir = Path("linkedin_data")
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)

    def sanitize_filename(self, url: str) -> str:
        """Convert LinkedIn URL to a safe filename."""
        return url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]

    def download_profile(self, linkedin_url: str) -> Optional[dict]:
        """Download data for a single LinkedIn profile."""
        params = {
            "linkedInUrl": linkedin_url,
            "apikey": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error downloading {linkedin_url}: {str(e)}")
            return None

    def save_profile_data(self, data: dict, linkedin_url: str):
        """Save profile data to a JSON file."""
        if not data:
            return

        # Create filename from LinkedIn URL and timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = self.sanitize_filename(linkedin_url)
        filename = f"{safe_name}_{timestamp}.json"
        filepath = self.output_dir / filename

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Saved data to {filepath}")
        except IOError as e:
            print(f"Error saving data: {str(e)}")

    def process_urls(self, urls: list[str]):
        """Process a list of LinkedIn URLs."""
        for url in urls:
            print(f"\nProcessing: {url}")
            data = self.download_profile(url)
            if data:
                self.save_profile_data(data, url)
                # Add a small delay to avoid hitting rate limits
                time.sleep(1)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Single URL: python script.py <linkedin_url>")
        print("2. Multiple URLs from file: python script.py --file <path_to_urls_file>")
        return

    try:
        downloader = LinkedInDownloader()
    except ValueError as e:
        print(f"Error: {e}")
        return

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Please provide the path to the URLs file")
            return
        
        try:
            with open(sys.argv[2], 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
            print(f"Found {len(urls)} URLs in file")
            downloader.process_urls(urls)
        except FileNotFoundError:
            print(f"File not found: {sys.argv[2]}")
    else:
        # Single URL mode
        url = sys.argv[1]
        downloader.process_urls([url])

if __name__ == "__main__":
    main()