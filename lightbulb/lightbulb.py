import RPi.GPIO as io

PIN = 0x17

class Lightbulb(object):
  def __init__(self, pin=PIN, *args, **kw):
    super(Lightbulb, self).__init__(*args, **kw)
    self._pin = pin
    self._state = False

    self.setup()

  def setup(self):
    io.setmode(io.BCM)
    io.setup(self._pin, io.OUT)


  def send(self, state=None):
    if state:
      self._state = state
    io.output(self._pin, self._state)

  def toggle(self):
    self.send(not self._state)
    return self._state

  def on(self):
    """The light shines in the darkness, and the darkness has not overcome it.

    - *John 1:5*
    """
    self.send(True)

  def off(self):
    """He sent darkness, and made the land dark; they did not rebel against his words.

    - *Psalm 105:28*
    """
    self.send(False)

  @property
  def state(self):
    return self._state
