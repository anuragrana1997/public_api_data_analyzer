from statistics import median

def analyzeData(users):
    summary = {}
    summary["medianHeight"] = median(user["height"] for user in users)
    summary["medianWeight"] = median(user["weight"] for user in users)
    summary["averageAge"] = sum(user["age"] for user in users) / len(users)
    summary["femaleCount"] = sum(1 for user in users if user["gender"] == "female") 
    summary["maleCount"] = sum(1 for user in users if user["gender"] == "male")
    summary["userCount"] = sum(1 for user in users if user["role"] == "user")
    summary["moderatorCount"] = sum(1 for user in users if user["role"] == "moderator")
    summary["adminCount"] = sum(1 for user in users if user["role"] == "admin")
    return summary