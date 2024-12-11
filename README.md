
# Data Extractor

The **Data Extractor** project is a Python-based tool designed to extract specific data fields from two webpages and save the results in a predefined schema. It processes the webpages and outputs files with the following data schema:

- **Text**
- **Publish Date and Time** (Format: `Year/Month/Day Hour:Minutes`)
- **Author Name**
- **Post Title**

## Features

- Extracts data from two specific webpages:
  1. [phpBB Forum Post](http://www.phpbb.com/community/viewtopic.php?f=46&t=2159437)
  2. [vBulletin Forum Post](https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login)
- Saves extracted data in separate output files for each webpage in the `output` directory.
- Supports configuration via a `config/configs` file.
- Logs program activities to a log file for reference.
- Automatically overrides or creates output files on each run.

## Prerequisites

- Python 3.8 or higher
- Docker (optional for containerized execution)

## Installation and Usage

### Using Virtual Environment

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd data-extractor
   ```

2. **Set up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Program:**
   ```bash
   python main.py
   ```

### Using Docker

1. **Build Docker Image:**
   ```bash
   docker build -t data-extractor .
   ```

2. **Run Docker Container:**
   ```bash
   docker run --rm -v $(pwd)/output:/app/output data-extractor
   ```

## Configuration

The application uses a configuration file located at `config/configs`. This file contains settings such as:
- Input URL list for the webpages.
- Regex patterns for extracting the desired fields.

You can modify the `configs` file to update extraction parameters or add new settings.

## Output

The extracted data is saved as:
- `output/phpbb_data.txt`
- `output/vbulletin_data.txt`

Each file will contain structured information in the following format:
```
Text: <Extracted Text>
Publish Date and Time: <Year/Month/Day Hour:Minutes>
Author Name: <Author>
Post Title: <Title>
```

**Note:** These files are automatically created or overwritten with each run of the program.

## Logging

All program activities, including errors and execution details, are logged to `logs/data_extractor.log`.

## Example Run

1. Ensure the required URLs are listed in the `config/configs` file.
2. Execute the program using the desired method (venv or Docker).
3. Check the `output` directory for the result files.
4. Review the log file for program execution details.

