Parse the access log located at `/app/access.log` and generate a JSON report at `/app/report.json`.

The report must be a JSON object containing exactly these keys:

1. `total_requests` — the total number of requests in the log.
2. `unique_ips` — the number of unique client IP addresses.
3. `top_path` — the most frequently requested request path.

Success criteria:

1. `/app/report.json` exists and is valid JSON.
2. `total_requests` is correct.
3. `unique_ips` is correct.
4. `top_path` is correct.

Do not write the report anywhere other than `/app/report.json`.

You have {timeout} seconds to complete the task.