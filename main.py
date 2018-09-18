import shutil
import datetime as dt

class DisplaySession:

    def __init__(self, byline="", default_ansi="\u001b[34m", include_timestamp=True, header_alignment='center', justify_char="-"):
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
    def map_align(align):
        if align == 'center':
            return "^"
        elif align == 'left':
            return "<"
        elif align == 'right':
            return ">"
        else:
            assert False

    @staticmethod
    def color_msg(msg, color):
        return color + msg + "\033[0m"

    @staticmethod
    def _pad_msg(msg, align):

        msg = msg.lstrip().rstrip()

        if align == 'center':
            return " " + msg + " "
        elif align == 'right':
            return " " + msg
        elif align == 'left':
            return msg + " "
        else:
            assert False

    def _align(self, msg, width, align, justify_char):
        template = '{0:{fill}{align}' + str(width) + "}"  # hack for format string to get max
        return template.format(msg, fill=justify_char, align=self.map_align(align))

    def h1(self, msg, ansi=None, align=None, justify_char=None):
        self._evaluate_terminal_size()

        ansi = ansi or self.default_ansi
        align = (align or self.header_alignment).lower()
        justify_char = justify_char or self.justify_char

        prepared_msg = self.color_msg(self._pad_msg(msg, align), ansi)
        width = int(self.columns * self.h1_pct)

        justified_msg = self._align(msg=prepared_msg, width=width, align=align, justify_char=justify_char)

        print(justified_msg)

    def _evaluate_terminal_size(self):
        columns, rows = shutil.get_terminal_size()
        # if terminal has been resized, recalculate header lengths
        if columns != self.columns:
            self.columns = columns

    def print(self, msg):
        string = str(dt.datetime.now())
        byline = self.color_msg(self.byline, self.default_ansi)
        print(" ".join([string, byline, msg]))


    def show_pallette(self):
        for style in range(8):
            for foreground in range(15, 38):
                s1 = ''
                for background in range(40, 48):
                    format = ';'.join([str(style), str(foreground), str(background)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')
