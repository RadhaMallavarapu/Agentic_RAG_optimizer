#src.utils.py

def clean_text(text):
    """
    Remove extra spaces and newlines from a string.
    """
    if not text:
        return " "

    return text.replace("\n", " ").strip()

def truncate_text(text, max_length=500):
    """
    Limit text lenth to max_length characters.
    """
    if not text:
        return " "

    return text[:max_length].strip()
    
