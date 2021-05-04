from mpf.core.mode import Mode

class Base(Mode):

  def mode_init(self, machine, name):
    self._current_value = None

  def mode_start(self, **kwargs):
      self.machine.leds.l_gi11.color('blue')
      self.add_mode_event_handler('player_score', self.rollOver)

  def rollOver(self, **kwargs):
    self.machine.leds.l_gi11.color('yellow')

    if self.machine.game.player1.score >= 300 and self.machine.game.player1.score < 2000 :
        self.machine.events.post('rollOver_1_100k')
    if self.machine.game.player1.score >= 200000 and self.machine.game.player1.score < 300000 :
        self.machine.events.post('rollOver_1_200k')
    if self.machine.game.player1.score >= 300000 and self.machine.game.player1.score < 300000 :
        self.machine.events.post('rollOver_1_300k')

    if self.machine.game.player2.score >= 100000 and self.machine.game.player2.score < 200000 :
        self.machine.events.post('rollOver_2_100k')
    if self.machine.game.player2.score >= 200000 and self.machine.game.player2.score < 300000 :
        self.machine.events.post('rollOver_2_200k')
    if self.machine.game.player2.score >= 300000 and self.machine.game.player2.score < 300000 :
        self.machine.events.post('rollOver_2_300k')
