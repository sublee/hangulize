import platform


def color(msg, color):
    if platform.win32_ver()[0]:
        return msg
    colors = dict(BLACK=30, RED=31, GREEN=32, YELLOW=33, BLUE=34,
                  MAGENTA=35, CYAN=36, WHITE=37)
    code = colors[color.upper()]
    return '\033[1;%dm%s\033[0m' % (code, msg)
