"""Validation utilities for file uploads and forms."""


def allowed_file(filename: str, allowed_extensions: set) -> bool:
    """
    Check if a filename has an allowed extension.
    
    Args:
        filename: The filename to check
        allowed_extensions: Set of allowed file extensions
        
    Returns:
        True if the file extension is allowed, False otherwise
    """
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in allowed_extensions
