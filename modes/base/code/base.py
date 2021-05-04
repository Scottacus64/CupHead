from mpf.core.mode import Mode

class Base(Mode):

  def mode_init(self):
    self._current_value = None

  def mode_start(self, **kwargs):
      self.machine.events.post('knockOut')
      self.add_mode_event_handler('player_score', self.rollOver)

  def rollOver(self, **kwargs):


    if self.player.score >= 300 and self.player.score < 2000 :
        if self.player.number == 1:
            self.machine.events.post('rollOver_1_100k')
