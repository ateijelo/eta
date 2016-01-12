from __future__ import division

import time

class ETA:
    def start(self):
        self._starttime = time.time()

    def eta(self, progress, total):
        if progress == 0:
            return float("inf")
        now = time.time()
        elapsed = now - self._starttime
        totaltime = elapsed * (total / progress)
        return totaltime - elapsed

    def pretty(self, progress, total):
        e = self.eta(progress, total)
        if e == float("inf"):
            return "--:--:--"
        secs = e % 60
        mins = int(e / 60) % 60
        hours = int(e / 3600)
        s = "{:02}:{:02}:{:02.0f}".format(hours, mins, secs)
        return s
