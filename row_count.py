import csv, pathlib

rows = sorted(p for p in pathlib.Path("data").rglob("*") if p.is_file())
with open("files.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["filepath", "split", "label", "filename"])
    for p in rows:
        w.writerow([p.as_posix(), p.parts[1], p.parts[2], p.name])
print(len(rows), "rows")