from mpf.core.mode import Mode

class ZeroOut(Mode):

  def mode_init(self):
      """Initialize digital score reel."""
      self._frames = {}
      self._reel_count = 5
      self._include_player_number = False


#  async def _initialize(self):
#      await super()._initialize()
#
#      self._reel_count = self.config["reel_count"]
#      self._include_player_number = self.config["include_player_number"]
#      for frame in self.config["frames"]:
#        self._frames[str(frame["character"])] = str(frame["frame"])
#
#      self.machine.events.add_handler(self.name, self._post_reel_values)

  def mode_start(self, **kwargs):
#      self.machine.events.post('player_score_reel', value = 0, player_num = 1)
#      oldScore = self.player.score
#      oldValue = 0 - oldScore
#      self.machine.events.post('player_score', value = 0, prev_value = oldScore, change = oldValue, player_num = 1)
#      self.machine.events.post('player_score', value = 0, prev_value = 0, change = 0, player_num = 2)
#      # Pad the string up to the necessary number of characters in the reel
#      score = str(kwargs["value"]).rjust(self._reel_count, self.config["start_value"])
#      # Create a dict of reel name keys to target frame values
      result = {'1': '2', '2': '2', '3': '2', '4': '2', '5': '2'}
#      # Post the event
      event_name = "score_reel_player_score_player1"
#          self._include_player_number else "score_reel_{}".format(self.name)
      self.machine.events.post(event_name, **result)

      event_name = "score_reel_player_score_player2"
#          self._include_player_number else "score_reel_{}".format(self.name)
      self.machine.events.post(event_name, **result)
