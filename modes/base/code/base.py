from mpf.core.mode import Mode

class rollOver(Mode):

    def rollOver_player1(self):
        if self.machine.game.player1.score >= 100000 and self.machine.game.player1.score < 200000 :
            self.machine.events.post('rollOver_1_100k')
        if self.machine.game.player1.score >= 200000 and self.machine.game.player1.score < 300000 :
            self.machine.events.post('rollOver_1_200k')
        if self.machine.game.player1.score >= 300000 and self.machine.game.player1.score < 300000 :
            self.machine.events.post('rollOver_1_300k')

    def rollOver_player2(self):
    def rollOver_player1(self):
        if self.machine.game.player2.score >= 100000 and self.machine.game.player2.score < 200000 :
            self.machine.events.post('rollOver_2_100k')
        if self.machine.game.player2.score >= 200000 and self.machine.game.player2.score < 300000 :
            self.machine.events.post('rollOver_2_200k')
        if self.machine.game.player2.score >= 300000 and self.machine.game.player2.score < 300000 :
            self.machine.events.post('rollOver_2_300k')
