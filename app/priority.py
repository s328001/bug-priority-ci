def get_priority(severity, frequency):
    if severity == "critical" and frequency == "rare":
        return "P2"
    if severity == "critical" and frequency == "always":
        return "P1"
    if severity == "major" and frequency == "always":
        return "P1"
    if severity == "major":
        return "P2"
    if severity == "minor":
        return "P3"
    raise ValueError("invalid input")
