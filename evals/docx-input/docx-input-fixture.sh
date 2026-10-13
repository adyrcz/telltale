#!/bin/bash
set -euo pipefail
python3 - <<'PY'
import zipfile
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
paras = [
    "The ferry was late again, which meant Dov had forty minutes to decide whether to tell his sister about the money.",
    "It wasn't the money that scared him. It was the silence after.",
    "TODO: decide if Ruth already knows about the loan",
    "Ruth was the third one off the boat, carrying a duffel he recognized from their father's garage. In that moment, everything changed.",
]
body = "".join(f'<w:p><w:r><w:t xml:space="preserve">{p.replace("&", "&amp;")}</w:t></w:r></w:p>' for p in paras)
with zipfile.ZipFile("chapter-02.docx", "w") as z:
    z.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
    z.writestr("word/document.xml", f"<w:document {W}><w:body>{body}</w:body></w:document>")
PY
