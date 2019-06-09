from datasette_render_binary import render_cell

GIF_1x1 = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00"


def test_render_cell():
    assert None == render_cell("hello")
    expected = (
        "GIF89a {s}01 00 01 00 80 00 00 00 00 00 FF FF FF{e} {s}FF{e} ! "
        "{s}F9 04 01 00 00 00 00{e} {s}00{e} , {s}00 00 00 00 01 00 01 00"
        " 00 02 01{e} {s}01{e} D {s}00{e} {s}00{e}"
    ).format(s='<code style="color: #999; font-family: monospace">', e="</code>")
    assert expected == render_cell(GIF_1x1)
