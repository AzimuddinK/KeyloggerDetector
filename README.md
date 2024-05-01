# KeyloggerDetector
Detect Keyloggers using Python GUI 

Personalized UI: The user interface is simplified and includes buttons for starting, stopping, and clearing the output.
Dynamic Detection: The detection process is initiated manually by the user clicking the "Start Detection" button.
Live Detection Updates: The detection process is set to run periodically (every 5 seconds) and continuously updates the output box with any detected potential keyloggers.
Dynamic Whitelisting/Blacklisting: When a potential keylogger is detected, the user is prompted to decide whether to trust the application. The user's decision determines whether the application is added to the whitelist or blacklist.
Process Name Extraction: The script extracts the process name corresponding to the detected network activity, providing more detailed information to the user.


## Keylogger Detector

This Python application aims to detect potential keyloggers running on your system by monitoring network connections and checking for suspicious processes.

### How to Use:

#### Save the Code:

Save the provided Python code (including the classes and functions) as a file named `keylogger_detector.py`.

### Run the Script:

Open a terminal or command prompt and navigate to the directory where you saved the `keylogger_detector.py` file.

Run the script using the following command:


Bash
```bash


python keylogger_detector.py
Use code with caution.
content_copy
```

### Start Detection:

The application will launch a graphical user interface (GUI) window.
Click the "Start Detection" button to begin monitoring your system for potential keyloggers.

### Monitoring and Output:

The application will periodically check for network connections on suspicious ports commonly used by keyloggers (587, 465, 2525).

If a suspicious connection is detected, the application will display the following information in the output window:
"Potential keylogger detected!"

"Process Name: [Process Name]" (the name of the process associated with the suspicious connection)
A confirmation dialog will appear asking if you trust the application.
If you trust the application, clicking "Yes" will add it to a whitelist, preventing future warnings for that specific process.
If you don't trust the application, clicking "No" will:
Add the process name to a blacklist.
Terminate the process using `psutil`.

### Stop Detection:

If you want to stop the monitoring, click the "Stop Detection" button.

#### Clear Output:

To clear the output window, click the "Clear Output" button.

## Additional Notes:

This application provides a basic approach to keylogger detection. While it can identify suspicious network activity, it's crucial to exercise caution and conduct further investigation before terminating processes.
Consider using antivirus software and other security measures alongside this tool for a more comprehensive defense against keyloggers and other malicious software.
