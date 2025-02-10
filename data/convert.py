
import pathlib, os, tqdm

# https://archive.org/details/bad-apple-resources
url = "https://archive.org/download/bad-apple-resources/bad_apple.mp4"
if not pathlib.Path("bad_apple.mp4").exists():
    os.system(f"curl -LO {url}")

output = pathlib.Path("output")
if not output.exists():
    output.mkdir()

os.system(r"ffmpeg -i bad_apple.mp4 output/frame-%04d.png")

root = pathlib.Path(".")
for one in tqdm.tqdm(root.glob("output/*.png"), total=6574):
    stem = one.stem
    # width("…")=width("—")=1000 in Helvetica (text field's default font)
    os.system(f'jp2a output/{stem}.png --chars="…—" --output=output/{stem}.txt')

frame = []
for x in tqdm.tqdm(range(1, 6574)):
    name = pathlib.Path("output/frame-%04d.txt" % x)
    raw = '"' + "\\n".join(name.read_text().split("\n")) + '"'
    frame.append(raw)

with open("frame.js", "w", encoding="U8") as out:
    out.write("var frame = [\n")
    for one in frame:
        out.write(one)
        out.write(",\n")
    out.write("];")
