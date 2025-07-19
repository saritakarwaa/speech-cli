import argparse, os, time
from speech_cli.recorder import record
from speech_cli.transcriber import transcribe
from speech_cli.analyzer import analyze
from speech_cli.exporter import export_json, export_md

def main():
    p = argparse.ArgumentParser(prog="speech-cli")
    sub = p.add_subparsers(dest="cmd", required=True)

    # record command
    rec = sub.add_parser("record")
    rec.add_argument("--duration", type=int, default=30)
    rec.add_argument("--prompt", type=str, default="")

    # analyze command
    ana = sub.add_parser("analyze")
    ana.add_argument("file", help="path to .wav file")
    ana.add_argument("--duration", type=int, default=30)

    # export command
    exp = sub.add_parser("export")
    exp.add_argument("file", help="path to .wav file")
    exp.add_argument("--format", choices=["json","md"], default="json")

    args = p.parse_args()

    if args.cmd == "record":
        timestamp = int(time.time())
        os.makedirs("recordings", exist_ok=True)
        out = f"recordings/{timestamp}.wav"
        print(f"🎤 Recording for {args.duration}s...")
        record(out, duration=args.duration)
        print("Saved to", out)

    elif args.cmd == "analyze":
        text, conf = transcribe(args.file)
        metrics = analyze(text, conf, args.duration)
        print("📝 Transcription:", text)
        print("📊 Feedback:")
        for k, v in metrics.items():
            print(f"- {k.replace('_', ' ').title()}: {v}")

    # elif args.cmd == "export":
    #     text, conf = transcribe(args.file)
    #     metrics = analyze(text, conf, args.duration)
    #     fname = os.path.splitext(os.path.basename(args.file))[0]
    #     out = f"feedback/{fname}.{args.format}"
    #     if args.format=="json": export_json(metrics, out)
    #     else: export_md(metrics, out)
    #     print("Exported report to", out)

    elif args.cmd == "export":
        text, conf = transcribe(args.file)
        # Use default duration of 30 seconds for analysis during export
        metrics = analyze(text, conf, duration_sec=30)  # Fixed this line
        fname = os.path.splitext(os.path.basename(args.file))[0]
        os.makedirs("feedback", exist_ok=True)  # Ensure directory exists
        out = f"feedback/{fname}.{args.format}"
        if args.format == "json": 
            export_json(metrics, out)
        else: 
            export_md(metrics, out)
        print(f"✅ Exported report to {out}")

if __name__ == "__main__":
    main()