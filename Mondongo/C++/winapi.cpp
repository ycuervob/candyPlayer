#include <X11/Xlib.h>

int main() {
    Display* display = XOpenDisplay(nullptr);

    if (display) {
        int x = 500;
        int y = 500;

        XWarpPointer(display, None, XRootWindow(display, DefaultScreen(display)),
                     0, 0, 0, 0, x, y);

        XFlush(display);
        XCloseDisplay(display);
    }

    return 0;
}
