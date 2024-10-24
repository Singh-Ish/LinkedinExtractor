# LinkedIn Profile Data Downloader

A Python-based command-line tool that downloads LinkedIn profile data using the Scrapin.io API. This tool allows you to download data for single profiles or batch process multiple LinkedIn URLs.

## Features

- Single profile and batch processing modes
- Automatic rate limiting to prevent API throttling
- JSON output with timestamps
- Environment variable configuration
- Error handling and status updates
- Safe file naming and storage

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Scrapin.io API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/linkedin-profile-downloader.git
cd linkedin-profile-downloader
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and add your API key
SCRAPIN_API_KEY=your_api_key_here
```

## Usage

### Single Profile Download
To download data for a single LinkedIn profile:
```bash
python linkedin_downloader.py https://www.linkedin.com/in/profile-name/
```

### Batch Processing
To download data for multiple profiles:

1. Create a text file (e.g., `urls.txt`) with one LinkedIn URL per line:
```text
https://www.linkedin.com/in/profile1/
https://www.linkedin.com/in/profile2/
https://www.linkedin.com/in/profile3/
```

2. Run the script with the file option:
```bash
python linkedin_downloader.py --file urls.txt
```

## Output

Downloaded data is saved in the `linkedin_data` directory. Each file is named using the format:
```
{profile_name}_{timestamp}.json
```

Example: `john-doe_20240324_153022.json`

## Project Structure

```
linkedin-profile-downloader/
├── linkedin_downloader.py    # Main script
├── requirements.txt          # Python dependencies
├── .env                     # Configuration file (not in repo)
├── .env.example             # Example configuration
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── linkedin_data/          # Output directory (created on first run)
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| SCRAPIN_API_KEY | Your Scrapin.io API key | Yes |

## Error Handling

The script includes error handling for common scenarios:
- Missing API key
- Invalid URLs
- API request failures
- File system errors

Error messages are displayed in the console with relevant details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Scrapin.io](https://scrapin.io) for providing the LinkedIn data API
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management
- [requests](https://requests.readthedocs.io/) for HTTP requests

## Support

For support, please open an issue in the GitHub repository or contact [your-email@example.com].

## Disclaimer

This tool is for educational and research purposes only. Please ensure you comply with LinkedIn's terms of service and Scrapin.io's usage guidelines when using this tool.