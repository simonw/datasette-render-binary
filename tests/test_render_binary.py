from datasette_render_binary import render_cell

GIF_1x1 = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00"


def test_render_cell_not_binary():
    assert None == render_cell("hello")


def test_render_cell_no_suggestion():
    expected = '<code style="color: #999; font-family: monospace">01 00 01 00 80 00 00 00 00 00 FF</code>'
    actual = render_cell(b"\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff")
    assert expected == actual


def test_render_cell_gif_with_suggestion():
    expected = (
        '<p style="margin-top: 0; font-family: monospace; font-size: 0.8em;">Suggestion: gif (image/gif)</p> '
        'GIF89a <code style="color: #999; font-family: monospace">01 00 01 00 80 00 00 00 00 00 FF FF FF</code>'
        ' ! <code style="color: #999; font-family: monospace">F9 04 01 00 00 00 00</code> , '
        '<code style="color: #999; font-family: monospace">00 00 00 00 01 00 01 00 00 02 01</code> '
        'D <code style="color: #999; font-family: monospace">00</code>'
    )
    assert expected == render_cell(GIF_1x1)
