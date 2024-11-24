
# OptiSigns Python Integration Example: File Upload

This project demonstrates how to upload a file to OptiSigns and add it as an asset using the OptiSigns API.

## Features

- **Upload and Add File Asset**:
  - Upload a file and add it as an asset in your OptiSigns account.
  - Demonstrated in `upload_file_example.py`.

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

## Script: Upload File and Create Asset

### Overview
The script `upload_file_example.py` uploads a file and adds it as an asset in your OptiSigns account.

### Usage
1. Place the file you want to upload in the same directory as the script (or provide the full path).

2. Open `upload_file_example.py` and update the `file_path` variable:
   ```python
   file_path = "os-logo.png"  # Replace with your file name or path
   ```

3. Run the script:
   ```bash
   python upload_file_example.py
   ```

4. Output:
   - On success, details of the created file asset will be printed to the console.
   - On failure, error details will be logged for debugging.

---

## Notes

1. **Error Handling**:
   - Ensure your `OPTISIGNS_API_KEY` is correctly set.
   - If an error occurs, check the printed logs for details.

2. **Supported Asset Types**:
   This script supports uploading files such as images, PDFs, and videos.

3. **Default Team ID**:
   The script uses a default `teamId` of `1`. Update this value in the script if your account requires a different team ID.

4. **Security**:
   Never hard-code your API key into the script. Always use environment variables for better security.

---

## References

- [OptiSigns API Documentation](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key)
- [Python Requests Library](https://docs.python-requests.org/)

For further assistance, reach out to [OptiSigns Support](https://support.optisigns.com/).

---
