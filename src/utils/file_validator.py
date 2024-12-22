def validate_file_type(file_type: str, allowed_type: str):
    if file_type != allowed_type:
        raise ValueError("Invalid file type! Only PDFs are allowed.")
