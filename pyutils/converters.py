def bytes2HumanReadable(bytes: float, buffer: float = 1000.0):
    """
        * Convert bytes to human readable sizes
    """
    for b in ["b", "kb", "mb", "gb", "tb", "pt"]:
        if bytes < buffer:
            return (bytes, f"{round(bytes, 2)} {b}")
        bytes /= buffer