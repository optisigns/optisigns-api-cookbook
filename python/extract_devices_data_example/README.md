# OptiSigns Python Integration Example: Extract Devices Data

This project demonstrates how to programmatically extract devices data from OptiSigns using the OptiSigns API.

## Features

- **Extract Devices Data**:
    - Retrieve detailed information about devices in your OptiSigns account.
    - Demonstrated in `extract_devices_data_example.py`.

## Prerequisites

### 1. Python Environment
Ensure you have Python 3.7+ installed on your system. You can verify this by running:
```bash
python --version
```

### 2. OptiSigns API Key
- Follow the instructions in [Generate & Manage OptiSigns API Key](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key) to generate your API key.
- Set the API key as an environment variable named `OPTISIGNS_API_KEY`. For example:
    - **Linux/macOS**:
        ```bash
        export OPTISIGNS_API_KEY=<your_api_key>
        ```
    - **Windows**:
        ```cmd
        set OPTISIGNS_API_KEY=<your_api_key>
        ```

### 3. Required Libraries
Install the required Python libraries using pip:
```bash
pip install requests
```

---

## Script: Extract Devices Data

### Overview
The script `extract_devices_data_example.py` extracts detailed information about devices in your OptiSigns account and saves it to a CSV file.

### Usage
1. Ensure your `OPTISIGNS_API_KEY` is set as an environment variable.

2. Run the script:
     ```bash
     python extract_devices_data_example.py
     ```

3. Output:
     - On success, a CSV file named `devices_data_extract.csv` will be created with the extracted devices data.
     - On failure, error details will be logged for debugging.

---

## Notes

1. **Error Handling**:
     - Ensure your `OPTISIGNS_API_KEY` is correctly set.
     - If an error occurs, check the printed logs for details.

2. **CSV File**:
     The script generates a CSV file named `devices_data_extract.csv` in the current directory. Ensure you have write permissions to this directory.

3. **Security**:
     Never hard-code your API key into the script. Always use environment variables for better security.

---

## References

- [OptiSigns API Documentation](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key)
- [Python Requests Library](https://docs.python-requests.org/)

For further assistance, reach out to [OptiSigns Support](https://support.optisigns.com/).

---