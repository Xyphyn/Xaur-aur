class ANSI():
    def background(code):
        return "\033[{code}m".format(code=code)

    def style_text(code):
        return "\033[{code}m".format(code=code)

    def color_text(code):
        return "\033[{code}m".format(code=code)
