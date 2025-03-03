import datetime
import os
import sys
import traceback
import json
import csv
import threading
from typing import TextIO


# noinspection PyTypeChecker
class Error:
    """A standardized error class for consistent error handling across programs."""

    LOG_LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]  # Predefined log levels
    LOG_COLORS = {
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[91;1m"  # Bold Red
    }
    RESET_COLOR = "\033[0m"  # Reset color

    log_lock = threading.Lock()  # Ensure thread-safe logging

    def __init__(self, message: str, code: int, subtype: str = "UNKNOWN", category: str = "GeneralError",
                 level: str = "ERROR",
                 capture_trace: bool = False, trace_depth: int = None, jonson: bool =False):  # type: ignore
        """
        Initialize an Error instance.

        :param message: Human-readable error message.
        :param code: Unique error code (0 for success, nonzero for errors).
        :param subtype: A string representing a more detailed error classification.
        :param category: Type of error (e.g., "FileError", "NetworkError").
        :param level: Log level (e.g., "INFO", "WARNING", "ERROR", "CRITICAL").
        :param capture_trace: Whether to capture the stack trace.
        :param trace_depth: Number of stack frames to capture (None for full trace).
        """
        self.message = message
        self.code = code
        self.subtype = subtype
        self.category = category
        self.level = level if level in self.LOG_LEVELS else "ERROR"  # Ensure the level is valid
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Capture the time of error
        self.script_name = os.path.basename(sys.argv[0])  # Identify the script that triggered the error
        self.function_name, self.line_number = self.get_caller_info()  # Extract caller function name and line number
        self.stack_trace = self.capture_stack_trace(
            trace_depth) if capture_trace else None  # Capture traceback if enabled
        self.jonson = jonson

    def __str__(self, for_user=False, jonson=False):
        """String representation of the error, useful for logging and debugging. for_user == True for a simplified output.
        :param for_user: enable a simple output
        """
        color = self.LOG_COLORS.get(self.level, "")
        if not for_user:
            return (f"{color}[Time: {self.timestamp}] [Script: {self.script_name}] "
                    f"[Function: {self.function_name}] [Line: {self.line_number}] "
                    f"[Category: {self.category}] [Subtype: {self.subtype}] [Level: {self.level}] Error {self.code}: {self.message}{self.RESET_COLOR}")
        elif for_user:
            return f"{color}{self.level}: {self.message}; of type {self.category} {self.subtype}; Code: {self.code}{self.RESET_COLOR}"
        elif jonson or self.jonson:
            return json.dumps({
                "timestamp": self.timestamp,
                "script": self.script_name,
                "function": self.function_name,
                "line": self.line_number,
                "category": self.category,
                "subtype": self.subtype,
                "level": self.level,
                "code": self.code,
                "message": self.message,
                "stack_trace": self.stack_trace
            })
        elif for_user and (jonson or self.jonson):
            return json.dumps({
                "message": self.message,
                "level": self.level,
                "code": self.code,
                "category": self.category,
                "subtype": self.subtype
            })

    def log(self, log_file="error.log", format_type="json", log_dir="logs", custom_handler=None,
            rotate_size=5 * 1024 * 1024):
        """
        Logs the error message to a file in various formats, supports custom handlers, log rotation, and directory control.

        :param log_file: Filename for logs.
        :param format_type: Format of the log file ("txt", "json", "csv").
        :param log_dir: Directory where logs should be stored.
        :param custom_handler: A function that processes the log entry before writing.
        :param rotate_size: Max size before log rotation (default 5MB).
        """
        log_entry = {
            "timestamp": self.timestamp,
            "script": self.script_name,
            "function": self.function_name,
            "line": self.line_number,
            "category": self.category,
            "subtype": self.subtype,
            "level": self.level,
            "code": self.code,
            "message": self.message,
            "stack_trace": self.stack_trace
        }

        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, log_file)

        # Log rotation: rename old log if size exceeds limit
        if os.path.exists(log_path) and os.path.getsize(log_path) > rotate_size:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            os.rename(log_path, f"{log_path}.{timestamp}.bak")

        with self.log_lock:  # Ensure thread safety
            if custom_handler:
                custom_handler(log_entry)

            if format_type == "json":  # Log as JSON
                with open(log_path, "a", encoding="utf-8") as file:
                    file.write(json.dumps(log_entry) + "\n")
            elif format_type == "csv":  # Log as CSV
                file_exists = os.path.isfile(log_path)
                with open(log_path, "a", newline='', encoding="utf-8") as file:
                    file: TextIO  # type: ignore
                    writer = csv.DictWriter(file, fieldnames=log_entry.keys())
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(log_entry)
            else:  # Default to plain text
                with open(log_path, "a", encoding="utf-8") as file:
                    file.write(str(self) + "\n")

    def is_success(self):
        """Returns True if the error code is 0 (indicating success)."""
        return self.code == 0

    def get_caller_info(self):
        """Retrieve the function name and line number where the error was created."""
        stack = traceback.extract_stack()
        if len(stack) > 2:
            caller = stack[-3]  # Get the function that called the error class
            return caller.name, caller.lineno
        return "Unknown", -1

    def capture_stack_trace(self, depth=None):
        """Capture stack trace up to a specified depth."""
        stack_trace = traceback.format_stack()
        return "".join(stack_trace[-depth:]) if depth else "".join(stack_trace)

    @staticmethod
    def get_logs(log_file="logs/error.log", format_type="json", level=None, category=None, subcode=None):
        """Retrieve and filter logs based on level, category, and subtype."""
        if not os.path.exists(log_file):
            return []

        filtered_logs = []
        with open(log_file, "r", encoding="utf-8") as file:
            if format_type == "json":
                for line in file:
                    entry = json.loads(line)
                    if (not level or entry["level"] == level) and (not category or entry["category"] == category) and (
                            not subcode or entry["subtype"] == subcode):
                        filtered_logs.append(entry)
        return filtered_logs
