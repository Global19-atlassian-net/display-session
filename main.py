import shutil


class DisplaySession:

    def __init__(self, byline="", default_ansi="", include_timestamp=True, header_alignment='center', justify_char="-"):
        self.byline = byline
        self.default_ansi = default_ansi
        self.include_timestamp = include_timestamp
        self.header_alignment = header_alignment
        self.justify_char = justify_char

        self.columns = None

        # as percent of terminal width
        self.h1_pct = .7
        self.h2_pct = .5
        self.h3_pct = .3

    @staticmethod
    def map_align(alignment):
        if alignment.lower() == 'center' return "^"
        elif alignment.lower() == 'left' return "<"
        elif alignment.lower() == 'right' return ">"
        else raise AttributeError(hey)

    @staticmethod
    def color_msg(msg, color):
        return color + msg + "\033[0m"

    @staticmethod
    def _pad_msg(msg):
        return " " + msg.lstrip().rstrip() + " "

    def _align(self, msg, width, align, justify_char):
        template = '{0:{fill}{align}' + str(int(width)) + "}" # hack for format string to get max
        return template.format(msg, fill=justify_char, align=align, width=width)

    def h1(self, msg, ansi=None, align=None, justify_char=None):
        self._evaluate_terminal_size()

        ansi = ansi or self.default_ansi
        align = align or self.header_alignment
        justify_char = justify_char or self.justify_char

        prepared_msg = self.color_msg(self._pad_msg(msg), ansi)
        width = self.columns * self.h1_pct

        justified_msg = self._align(msg=prepared_msg, width=width, align=align, justify_char=justify_char)

        print(justified_msg)

    def _evaluate_terminal_size(self):
        columns, rows = shutil.get_terminal_size()
        # if terminal has been resized, recalculate header lengths
        if columns != self.columns:
            self.columns = columns

    def show_pallette(self):
        for style in range(8):
            for foreground in range(15, 38):
                s1 = ''
                for background in range(40, 48):
                    format = ';'.join([str(style), str(foreground), str(background)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')
