import re
from datasette import hookimpl
import jinja2

sequence_re = re.compile(r"((\\x[0-9a-f]{2})+)")
octet_re = re.compile(r"(\\x[0-9a-f]{2})")


@hookimpl(trylast=True)
def render_cell(value):
    if not isinstance(value, bytes):
        return None
    encoded = repr(value)
    # Ditch the b' and trailing '
    if encoded.startswith("b'") and encoded.endswith("'"):
        encoded = encoded[2:-1]

    # Split it into sequences of octets and characters
    chunks = sequence_re.split(encoded)
    html = []
    for chunk in chunks:
        if sequence_re.match(chunk):
            octets = octet_re.findall(chunk)
            octets = [o[2:] for o in octets]
            html.append(
                '<code style="color: #999; font-family: monospace">{}</code>'.format(
                    " ".join(octets).upper()
                )
            )
        else:
            html.append(jinja2.escape(chunk.replace("\\\\", "\\")))
    return jinja2.Markup(" ".join(html).strip())
