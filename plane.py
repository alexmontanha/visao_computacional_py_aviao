import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    airplane = ">"
    airplane_x = sw - 1
    airplane_y = random.randint(1, sh - 2)

    bullet = "*"
    bullet_x = -1
    bullet_y = -1

    while True:
        w.clear()
        w.border(0)

        key = w.getch()

        if key == ord(' '):
            if bullet_x == -1:
                bullet_x = 1
                bullet_y = sh // 2

        if bullet_x != -1:
            w.addch(bullet_y, bullet_x, bullet)
            bullet_x += 1

        if bullet_x == sw:
            bullet_x = -1

        if airplane_x == 0:
            airplane_x = sw - 1
            airplane_y = random.randint(1, sh - 2)

        if bullet_x == airplane_x and bullet_y == airplane_y:
            w.addstr(airplane_y, airplane_x, "BOOM")
            airplane_x = sw - 1
            airplane_y = random.randint(1, sh - 2)
            bullet_x = -1

        w.addch(airplane_y, airplane_x, airplane)
        airplane_x -= 1

        w.refresh()
        time.sleep(0.1)

curses.wrapper(main)