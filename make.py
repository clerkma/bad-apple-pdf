import pymupdf
import pathlib

def new_text_stream(doc, src):
    i = doc.get_new_xref()
    doc.update_object(i, "<<>>")
    doc.update_stream(i, src.encode("UTF-16-BE"))
    return f"{i} 0 R"

def new_object(doc, src):
    i = doc.get_new_xref()
    doc.update_object(i, src)
    return f"{i} 0 R"

if __name__ == "__main__":
    frame = pathlib.Path("data/frame.js").read_bytes().decode("U8")
    main = pathlib.Path("code-main.js").read_text()
    code = "\uFEFF" + frame + main # unicode text stream requires a BOM
    console = pathlib.Path("code-console.txt").read_text()
    button = pathlib.Path("code-button.txt").read_text()

    document = pymupdf.open()
    page = document.new_page(width=100, height=100)
    page.draw_rect((0, 40, 100, 100), fill=(0, 0, 0), width=0)
    page.insert_text((0, 10), "bad-apple.pdf", fontname="cour")
    r = page.xref
    document.xref_set_key(
        r, "AA",
        "<</O<</S/JavaScript/JS %s>>>>" % new_text_stream(document, code)
    )
    document.xref_set_key(
        r, "Annots",
        "[%s %s]" % (
            new_object(document, console),
            new_object(document, button)
        )
    )
    document.save("bad-apple.pdf")
