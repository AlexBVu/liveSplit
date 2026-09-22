import rumps
import datetime


class Livesplit(rumps.App):
    def __init__(self, selfquit_button='Quit'):
        super(Livesplit, self).__init__("LiveSplit")
        self.menu = ["Add Segments", "Start Run"]

        self.task = None
        self.time = None

        # self.segments = [] ? do i need this ? 

        rumps.debug_mode("On")

    @rumps.clicked("Add Segments")
    def add_segments(self, sender):
        # rumps.notification("starting run", "Subtitle", "go!")
        window = rumps.Window("Format: [event-minutes;]", "Enter Your Segments:", default_text="", ok=None, cancel=None, 
                     dimensions=(320, 160))

        response = window.run()
        r = response.text.split()

        self.add_segments_helper(r)

    @rumps.clicked("Start Run")
    def start_run(self):
        self.update()
        self.title = "why am i here"

    @rumps.timer(3)
    def update(self):
        if self.task and self.time:
            self.title = self.task + " " + str(self.time)
            self.time -= 1
        else:
            self.title = "error: either are null"

    def add_segments_helper(self, response: list):
        self.task = response[0]
        self.time = response[1]
        # for i in range(0, len(response), 2):
        #     task = response[i]
        #     time = response[i + 1]
        #     self.segments.append((task,time))
        #     self.task = task
        #     self.time = int(time)

def main():
    Livesplit().run()

if __name__ == "__main__":
    main()