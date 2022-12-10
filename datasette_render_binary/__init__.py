import re
import filetype
from datasette import hookimpl
from markupsafe import escape, Markup

sequence_re = re.compile(r"((?:\\x[0-9a-f]{2})+)")
octet_re = re.compile(r"(\\x[0-9a-f]{2})")


@hookimpl(trylast=True)
def render_cell(value):
    if not isinstance(value, bytes):
        return None
    # Attempt to guess filetype
    suggestion = None
    match = filetype.guess(value[:1000])
    if match:
        suggestion = "{} ({})".format(match.extension, match.mime)
    encoded = repr(value)
    # Ditch the b' and trailing '
    if encoded.startswith("b'") and encoded.endswith("'"):
        encoded = encoded[2:-1]
    # Split it into sequences of octets and characters
    chunks = sequence_re.split(encoded)
    html = []
    if suggestion:
        html.append(
            '<p style="margin-top: 0; font-family: monospace; font-size: 0.8em;">Suggestion: {}</p>'.format(
                escape(suggestion)
            )
        )
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
            html.append(escape(chunk.replace("\\\\", "\\")))
    return Markup(" ".join(html).strip())
