import time

import rumps


class Livesplit(rumps.App):
    def __init__(self):
        super().__init__("LiveSplit")
        self.menu = ["Add Segments", "Start Run", "Next Split", "Reset"]

        self.segments = []  # (name, target seconds)
        self.i = 0
        self.start = 0.0

        self.timer = rumps.Timer(self.update, 0.05)

    @rumps.clicked("Add Segments")
    def add_segments(self, sender):
        window = rumps.Window(
            "Format: task minutes task minutes ...",
            "Enter Your Segments:",
            default_text="",
            ok=None,
            cancel=None,
            dimensions=(320, 160),
        )
        new, words = [], []
        for t in window.run().text.split():
            if not t.replace(".", "", 1).isdigit():  # a number closes the segment
                words.append(t)
            elif words:
                new.append((" ".join(words), float(t) * 60))
                words = []
            else:
                words = None  # number with no name
                break
        if words is None or words:  # bad number, or trailing name with no minutes
            rumps.alert("Bad input", "Use: task words minutes task words minutes ...")
            return
        self.segments += new

    @rumps.clicked("Start Run")
    def commence(self, sender):
        if not self.segments:
            rumps.alert("Add segments first")
            return
        self.i = 0
        self.start = time.monotonic()
        self.timer.start()

    @rumps.clicked("Next Split")
    def split(self, sender):
        if not self.timer.is_alive():
            return
        self.i += 1
        if self.i >= len(self.segments):
            self.timer.stop()
            self.title = "done"
        else:
            self.start = time.monotonic()

    @rumps.clicked("Reset")
    def reset(self, sender):
        self.timer.stop()
        self.title = "LiveSplit"

    def update(self, _):
        name, target = self.segments[self.i]
        elapsed = time.monotonic() - self.start
        # green under the last minute, yellow in the last minute, red once over target
        dot = "🟢" if elapsed < target - 60 else "🟡" if elapsed < target else "🔴"
        m, s = divmod(elapsed, 60)
        self.title = f"{dot} {name} {int(m)}:{s:06.3f}"


def main():
    Livesplit().run()


if __name__ == "__main__":
    main()
