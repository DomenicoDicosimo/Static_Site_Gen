def extract_title(filename):
    lines = filename.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line
    raise Exception("Invalid markdown format - no header found")

    
