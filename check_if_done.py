import json
import sys
import re

def main():
    """Main function for the check_if_done agent."""
    history_json_string = sys.stdin.read()
    history = json.loads(history_json_string)

    code_edit_detected = False
    for msg in reversed(history):
        if msg["role"] == "assistant":
            if re.search(r"```", msg["content"]):  # Look for code fences
                code_edit_detected = True
                break

    if code_edit_detected:
        print("check your code, are you done with the changes?")

if __name__ == "__main__":
    main()
