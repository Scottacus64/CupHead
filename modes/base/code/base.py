from mpf.core.mode import Mode

class Base(Mode):

  def mode_init(self):
    self._current_value = None

  def mode_start(self, **kwargs):
      self.add_mode_event_handler('player_score', self.rollOver)

  def rollOver(self, **kwargs):
    if self.player.score >= 100000 and self.player.score < 200000 :
        if self.player.number == 1:
            self.machine.events.post('rollOver_1_100k')
        if self.player.number == 2:
            self.machine.events.post('rollOver_2_100k')
    if self.player.score >= 200000 and self.player.score < 300000 :
        if self.player.number == 1:
            self.machine.events.post('rollOver_1_200k')
        if self.player.number == 2:
            self.machine.events.post('rollOver_2_200k')
    if self.player.score >= 300000 and self.player.score < 400000 :
        if self.player.number == 1:
            self.machine.events.post('rollOver_1_300k')
        if self.player.number == 2:
            self.machine.events.post('rollOver_2_300k')
    if self.player.score >= 400000 and self.player.score < 500000 :
        if self.player.number == 1:
            self.machine.events.post('rollOver_1_400k')
        if self.player.number == 2:
            self.machine.events.post('rollOver_2_400k')
