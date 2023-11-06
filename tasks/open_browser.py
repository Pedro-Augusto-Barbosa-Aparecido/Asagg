import os
import sys

# asking user if he wants to open the coverage of
# tests on the browser
try:
    can_be_open_browser = input(
        "Do you want to open the browser to see coverage? (Y/n) "
    ).upper()
except Exception as e:
    exit(0)

match can_be_open_browser:
    case "Y":
        pass
    case _:
        exit(0)

# getting an operational system
operational_platform = sys.platform.lower()

# command to run in shell
command = ""

# matching with an operational system
if "linux" in operational_platform:
    command = "python -m webbrowser"
elif "darwin" in operational_platform:
    command = "open"
elif "win" in operational_platform:
    command = "explorer"
else:
    raise OSError("Unknown Operational System")

# getting path to coverage html file
local_directory = os.path.dirname("poetry.lock")
html_coverage_file = os.path.join(local_directory, "htmlcov", "index.html")

command_complete = f'{command} "{html_coverage_file}"'

# running broswer
try:
    os.system(command_complete)
except Exception as e:
    print(e)

    try:
        command_complete = f'python -m webbroser "{html_coverage_file}"'
        os.system(command_complete)
    except Exception as e:
        pass
