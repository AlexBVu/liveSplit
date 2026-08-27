import rumps
import time

TIME_INTERVAL = 25*60

class Timer(object):
    def __init__(self):
        self.timer = rumps.Timer(self.on_tick, 1)
        self.timer.stop()
        self.timer.count = 0

        self.app = rumps.App('timer')

        self.start_pause_button = rumps.MenuItem(title='Start timer',
                                                 callback=self.start_timer)
        self.stop_button = rumps.MenuItem(title='Stop timer',
                                                callback=self.stop_timer)
        self.app.menu = [self.start_pause_button,
                         self.stop_button]

    def run(self):
        self.app.run()

    def start_timer(self, sender):
        if sender.title in ['Start timer', 'Continue timer']:
            if sender.title == 'Start timer':
                self.timer.count = 0
                self.timer.end = TIME_INTERVAL

            sender.title = 'Pause timer'

            self.timer.start()

        else:
            sender.title = 'Continue timer'
            self.timer.stop()

    def on_tick(self, sender):
        time_left = sender.end - sender.count
        # handle minute and second counter if positive/negative time left
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            # add minus sign if between -1 and -59 seconds
            self.app.title = '-{:2d}:{:02d}'.format(mins, secs)
        else:
            self.app.title = '{:2d}:{:02d}'.format(mins, secs)

        sender.count += 1
        if sender.count == sender.end:
            rumps.notification(title='Time is up! Take a break :)',
                               subtitle='PyModoro',
                               message='')
            ## Uncomment if hard stop of timer wanted
            # print('stopping timer')
            # stop_timer()

    def stop_timer(self, sender=None):
        self.timer.stop()
        self.timer.count = 0
        self.app.title = None
        self.start_pause_button.title = 'Start timer'
        # app.menu._menu[0].title = 'Start timer'

if __name__ == "__main__":
    app = Timer()
    app.run()