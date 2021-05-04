from mpf.core.mode import Mode

class Base(Mode):

  def mode_init(self, machine, name):
    self._current_value = None

  def mode_start(self, **kwargs):
      self.machine.leds.l_gi11.color('blue')

  def rollOver_player1(self, **kwargs):
    if self.machine.game.player1.score >= 100 and self.machine.game.player1.score < 2000 :
        self.machine.events.post('rollOver_1_100k')
    if self.machine.game.player1.score >= 200000 and self.machine.game.player1.score < 300000 :
        self.machine.events.post('rollOver_1_200k')
    if self.machine.game.player1.score >= 300000 and self.machine.game.player1.score < 300000 :
        self.machine.events.post('rollOver_1_300k')

  def rollOver_player2(self):
    if self.machine.game.player2.score >= 100000 and self.machine.game.player2.score < 200000 :
        self.machine.events.post('rollOver_2_100k')
    if self.machine.game.player2.score >= 200000 and self.machine.game.player2.score < 300000 :
        self.machine.events.post('rollOver_2_200k')
    if self.machine.game.player2.score >= 300000 and self.machine.game.player2.score < 300000 :
        self.machine.events.post('rollOver_2_300k')
