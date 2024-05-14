def extract_title(filename):
    for line in filename:
        if line.startswith("# "):
            return line
    raise Exception("Invalid markdown format - no header found")

    
