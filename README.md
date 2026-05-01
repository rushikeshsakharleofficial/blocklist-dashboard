# Blocklist Dashboard

Interactive IP/domain blocklist monitoring dashboard with WebSocket updates.

## Features

- Track IP addresses against common DNSBL zones.
- Real-time dashboard updates over WebSockets.
- Add IPs from the browser UI.
- Static report generator for JSON and standalone HTML output.
- Stub/simulation mode for restricted environments.
- Optional live DNSBL mode for production networks.

## Quick start

```bash
pip install -r requirements.txt
uvicorn blocklist_dashboard.server:app --reload
```

Open:

```text
http://127.0.0.1:8000/
```

## Static report

```bash
python -m blocklist_dashboard.generate_report
```

For live DNSBL checks:

```bash
python -m blocklist_dashboard.generate_report --live
```

## Production notes

The default server runs in deterministic simulation mode because many sandboxed or corporate environments block outbound DNSBL lookups. To enable live lookups, edit `blocklist_dashboard/server.py`:

```python
_CHECK_OPTIONS = {"live": True}
```

For a production SaaS version, add persistent storage, authentication, tenant isolation, alerting, rate limits, and audit logging.
