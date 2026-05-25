#!/usr/bin/env python3
"""Analyze form submissions — completion rate, averages, distribution."""
import json, sys

def analyze(data):
    submissions = data.get("submissions", [])
    total = len(submissions)
    if total == 0:
        return {"total": 0, "message": "No submissions yet"}
    
    completed = sum(1 for s in submissions if s.get("complete", True))
    ratings = [s.get("rating") for s in submissions if s.get("rating") is not None]
    
    result = {
        "total": total,
        "completed": completed,
        "completion_rate": round(completed / total * 100, 1),
        "avg_rating": round(sum(ratings) / len(ratings), 2) if ratings else None,
        "rating_distribution": {},
    }
    for r in ratings:
        key = str(int(r))
        result["rating_distribution"][key] = result["rating_distribution"].get(key, 0) + 1
    return result

if __name__ == "__main__":
    print(json.dumps(analyze(json.loads(sys.argv[1])), indent=2))
