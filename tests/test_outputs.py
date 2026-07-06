import json
import re
from collections import Counter
from pathlib import Path


def expected():
    paths = Counter()
    ips = set()
    total = 0

    with open("/app/access.log") as f:
        for line in f:
            if not line.strip():
                continue
            total += 1
            ips.add(line.split()[0])

            m = re.search(
                r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ',
                line,
            )

            if m:
                paths[m.group(1)] += 1

    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def report():
    with open("/app/report.json") as f:
        return json.load(f)


def test_total_requests():
    """Success criterion 1: report contains the correct total_requests."""
    assert report()["total_requests"] == expected()["total_requests"]


def test_unique_ips():
    """Success criterion 2: report contains the correct unique_ips."""
    assert report()["unique_ips"] == expected()["unique_ips"]


def test_top_path():
    """Success criterion 3: report contains the correct top_path."""
    assert report()["top_path"] == expected()["top_path"]