with open("example.txt", "w") as file:
    file.write("Hello, this is a file I/O example.\n")
    file.write("Writing multiple lines to a file.\n")

with open("example.txt", "r") as file:
    content = file.read()

print("File Content:\n", content)
