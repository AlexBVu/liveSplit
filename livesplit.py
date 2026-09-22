import rumps
import datetime


class Livesplit(rumps.App):
    def __init__(self, selfquit_button='Quit'):
        super(Livesplit, self).__init__("LiveSplit")
        self.menu = ["Add Segments", "Start Run"]

        self.segments = [] 

        self.time = 0
        self.task = ""

        self.timer = rumps.Timer(self.update, 1)

        rumps.debug_mode("On")

    @rumps.clicked("Add Segments")
    def add_segments(self, sender):
        # rumps.notification("starting run", "Subtitle", "go!")
        window = rumps.Window("Format: [event minutes]", "Enter Your Segments:", default_text="", ok=None, cancel=None, 
                     dimensions=(320, 160))

        response = window.run()
        r = response.text.split()

        self.add_segments_helper(r)

    @rumps.clicked("Start Run")
    def commence(self, sender):
        if self.segments:
            self.task = self.segments[0][0]
            self.time = int(self.segments[0][1])
            self.timer.start()
        else:
            self.title = "error, self.segments is null"

    @rumps.timer(1)
    def update(self):
        if self.time is int:
            self.title = str(self.task) + " " + str(self.time)
            self.time -= 1

    def add_segments_helper(self, response: list):
        for i in range(0, len(response), 2):
            task = response[i]
            time = response[i + 1]
            self.segments.append((task,time))

def main():
    Livesplit().run()

if __name__ == "__main__":
    main()