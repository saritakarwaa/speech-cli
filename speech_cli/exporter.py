import json
import os

def export_json(metrics: dict, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(metrics, f, indent=2)

def export_md(metrics: dict, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    lines = ['# Speech Feedback Report', '']
    for k, v in metrics.items():
        label = k.replace('_', ' ').title()
        lines.append(f"- **{label}**: {v}")
    with open(out_path, 'w') as f:
        f.write("\n".join(lines))