import rumps
import time

class Livesplit(rumps.App):
    def __init__(self, selfquit_button='Quit'):
        super(Livesplit, self).__init__("LiveSplit")
        self.menu = ["Start run"]
        rumps.debug_mode("On")

    @rumps.clicked("Start run")
    def start_run(self, sender):
        # rumps.notification("starting run", "Subtitle", "go!")
        window = rumps.Window("window", "title", default_text=" ", ok=None, cancel=None, 
                     dimensions=(320, 160))

        window.add_button("start")
        response = window.run()
        print(response.text)

        # TODO: parse response, add segments


def main():
    Livesplit().run()

if __name__ == "__main__":
    main()