SERVER_LOGS = [
    "INFO: User logged in",
    "ERROR: Connection timeout",
    "DEBUG: Query executed",
    "ERROR: Database locked",
]
cleaned_messages = [log.replace("ERROR:","").strip() for log in SERVER_LOGS if log.startswith("ERROR")]
print(cleaned_messages)