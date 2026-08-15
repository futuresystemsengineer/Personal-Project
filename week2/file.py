file = input("File name: ")
file_lower = file.lower()

if file_lower.endswith(".gif"):
    output = "image/gif"
elif file_lower.endswith((".jpg", ".jpeg")):
    output = "image/jpeg"
elif file_lower.endswith(".png"):
    output = "image/png"
elif file_lower.endswith(".pdf"):
    output = "applications/pdf"
elif file_lower.endswith(".txt"):
    output = "text/plain"
elif file_lower.endswith(".zip"):
    output = "ZIP archive"
else:
    output = "application/octet-stream"
print(output)