
import curses

class VoidClass():
    pass

def draw_box(window, ref_y, ref_x, nb_line, nb_col):
    window.hline(ref_y, ref_x, 'A', nb_col)
    window.hline(ref_y + nb_line, ref_x, 'B', nb_col)
    window.vline(ref_y, ref_x, 'C', nb_line + 1)
    window.vline(ref_y, ref_x + nb_col, 'D', nb_line + 1)
    window.refresh()

def feed_box(window, ref_y, ref_x, nb_line, nb_col):
    ref_y = ref_y + 1
    ref_x = ref_x + 1
    nb_line = nb_line - 1
    nb_col = nb_col - 1
    while nb_line > 0:
        window.hline(ref_y, ref_x, '.', nb_col)
        nb_line = nb_line - 1
        ref_y = ref_y + 1