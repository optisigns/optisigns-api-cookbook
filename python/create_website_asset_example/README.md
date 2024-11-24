
# OptiSigns Python Integration Example: Create Website Asset

This project demonstrates how to programmatically create a website asset in OptiSigns using the OptiSigns API.

## Features

- **Create Website Asset**:
  - Add a website link as an asset to your OptiSigns account.
  - Demonstrated in `create_website_asset_example.py`.

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

## Script: Create Website Asset

### Overview
The script `create_website_asset_example.py` creates a website asset in your OptiSigns account.

### Usage
1. Open `create_website_asset_example.py` and update the `asset_name` and `url` values:
   ```python
   asset_name = "Your Asset Name"
   url = "https://your-website-url.com"
   ```

2. Run the script:
   ```bash
   python create_website_asset_example.py
   ```

3. Output:
   - On success, details of the created website asset will be printed to the console.
   - On failure, error details will be logged for debugging.

---

## Notes

1. **Error Handling**:
   - Ensure your `OPTISIGNS_API_KEY` is correctly set.
   - If an error occurs, check the printed logs for details.

2. **Default Team ID**:
   The script uses a default `teamId` of `1`. Update this value in the script if your account requires a different team ID.

3. **Security**:
   Never hard-code your API key into the script. Always use environment variables for better security.

---

## References

- [OptiSigns API Documentation](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key)
- [Python Requests Library](https://docs.python-requests.org/)

For further assistance, reach out to [OptiSigns Support](https://support.optisigns.com/).

---
