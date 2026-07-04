from datetime import datetime

print("Python artifact demo")

with open("reults.txt", "w") as file:
  file.write("Hello from GitHub\n")
  file.write("This file is created in Git\n")
  file.write(f"Generated Time: {datetime.now()}\n")

print("result.txt file created successfully")
