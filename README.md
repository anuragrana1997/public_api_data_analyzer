# Public API Data Analyzer

A Python mini-project that fetches data from a public REST API, stores the data in CSV format, and generates summary statistics.

This project demonstrates API integration, file handling, data analysis, exception handling, and modular Python programming.

## Features

- Fetch user data from a public REST API using HTTPX.
- Handle HTTP errors and connection failures.
- Convert JSON responses into Python dictionaries and lists.
- Store API data in a CSV file.
- Calculate summary statistics such as:
  - Total number of users
  - Average age
  - Median age
  - Number of female users
- Organize code into reusable modules.

## Tech Stack

- Python 3
- HTTPX
- CSV
- JSON
- Python Statistics Module

## Project Structure

```text
public_api_data_analyzer/
│
├── config/
│   └── apiNames.py
│
├── helper/
│   ├── apiConfig.py
│   └── storeCSV.py
│
├── src/
│   ├── analyze.py
│   └── main.py
│
├── storage/
│   └── data.csv
│
├── requirements.txt
└── README.md
```

### Module Responsibilities

| File | Responsibility |
|---|---|
| `apiNames.py` | Stores API endpoint configuration |
| `apiConfig.py` | Handles HTTP requests and API responses |
| `storeCSV.py` | Saves fetched data into a CSV file |
| `analyze.py` | Calculates summary statistics |
| `main.py` | Coordinates the complete workflow |

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd public_api_data_analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If you haven't created `requirements.txt`, install HTTPX:

```bash
python -m pip install httpx
```

Then generate the dependency file:

```bash
python -m pip freeze > requirements.txt
```

## Usage

Navigate to the project root directory and run:

```bash
python -m src.main
```

The application will:

1. Fetch user data from the configured API.
2. Parse the JSON response.
3. Save the user records into `storage/data.csv`.
4. Analyze the retrieved data.
5. Display the summary in the terminal.

## Example CSV Output

```csv
id,firstName,lastName,maidenName,age,gender
1,Emily,Johnson,Smith,28,female
2,Michael,Williams,,35,male
```

*Illustrative data only.*

The actual output depends on the API response.

## Example Summary

```text
Total Users: 100
Average Age: 32.45
Median Age: 31
Female Users: 48
```

*Illustrative output. Actual results depend on the retrieved dataset and implemented statistics.*

## Application Workflow

```text
Public REST API
       |
       v
Fetch Data (HTTPX)
       |
       v
Parse JSON Response
       |
       v
Store Data (CSV)
       |
       v
Analyze Data
       |
       v
Display Summary
```

## Error Handling

The application uses Python exception handling to manage API-related failures.

Relevant exceptions include:

- `httpx.HTTPStatusError`: Unsuccessful HTTP responses.
- `httpx.TimeoutException`: Request timeout.
- `httpx.RequestError`: Connection and other request failures.
- `ValueError`: Invalid JSON responses or data conversion failures.

## Concepts Practiced

This project demonstrates:

- Functions and modular programming
- Python imports and packages
- REST API integration
- HTTP status codes and JSON parsing
- CSV file handling
- List and dictionary operations
- Statistical calculations
- Exception handling
- Virtual environments and dependency management

## Future Improvements

- Support multiple public APIs.
- Export analysis results to JSON.
- Add automated tests using pytest.
- Implement structured logging.
- Add charts for data visualization.
- Support command-line arguments.
- requirements.txt needs to be added

## License

This project is intended for educational and portfolio purposes.