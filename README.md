# ETA

ETA = Estimated Time of Agony  --  [not really](https://en.wikipedia.org/wiki/Estimated_time_of_arrival) ;)



This is the simple `ETA` class I've always wanted to be in the Python Standard Library.

Use it like this:

```python
from eta import ETA
import time

eta = ETA()
eta.start()  # call this when you start

for i in range(1,101):
    time.sleep(1)
    print(eta.pretty(i,100)) # then call pretty with progress and total
```

That will get you the following:

    00:01:39
    00:01:38
    00:01:37
    ...
    00:00:03
    00:00:02
    00:00:01
    00:00:00

Like it?
