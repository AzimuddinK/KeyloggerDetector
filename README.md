# KeyloggerDetector
Detect Keyloggers using Python GUI 

Personalized UI: The user interface is simplified and includes buttons for starting, stopping, and clearing the output.
Dynamic Detection: The detection process is initiated manually by the user clicking the "Start Detection" button.
Live Detection Updates: The detection process is set to run periodically (every 5 seconds) and continuously updates the output box with any detected potential keyloggers.
Dynamic Whitelisting/Blacklisting: When a potential keylogger is detected, the user is prompted to decide whether to trust the application. The user's decision determines whether the application is added to the whitelist or blacklist.
Process Name Extraction: The script extracts the process name corresponding to the detected network activity, providing more detailed information to the user.
