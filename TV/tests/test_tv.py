from unittest import TestCase
from src import tv

class TestTV(TestCase):

    def setUp(self):
        self.tv = tv.TV()

    def test_initial_state(self):
        self.assertFalse(self.tv.is_on)

    def test_turn_on_function(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

    def test_initial_volume(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.assertEqual(self.tv.volume, "Volume: 0")

    def test_raise_volume(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.tv.increase_volume_by(10)
        self.assertEqual(self.tv.volume, "Volume: 10")

    def test_decrease_volume(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.tv.increase_volume_by(10)
        self.assertEqual(self.tv.volume, "Volume: 10")
        self.tv.decrease_volume_by(5)
        self.assertEqual(self.tv.volume, "Volume: 5")

    def test_cannot_increase_volume_past_100(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.volume, "Volume: 0")
        self.tv.increase_volume_by(100)
        self.assertEqual(self.tv.volume, "Volume: 100")

        self.assertEqual(self.tv.increase_volume_by(1), "Volume cannot exceed 100")

    def test_cannot_decrease_volume_below_0(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.volume, "Volume: 0")

        self.assertEqual(self.tv.decrease_volume_by(1), "Volume cannot fall below 0")

    def test_cannot_get_volume_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)

        self.assertEqual(self.tv.volume, "TV is off")

    def test_cannot_increase_volume_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)

        self.assertEqual(self.tv.increase_volume_by(1), "TV is off")

    def test_cannot_decrease_volume_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)

        self.assertEqual(self.tv.decrease_volume_by(1), "TV is off")

    def test_initial_channel(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.assertEqual(self.tv.channel, "Channel set to 0")

    def test_increment_channel(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.channel, "Channel set to 0")

        self.tv.channel_up()
        self.assertEqual(self.tv.channel, "Channel set to 1")

    def test_decrement_channel(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.channel, "Channel set to 0")

        self.tv.channel_up()
        self.assertEqual(self.tv.channel, "Channel set to 1")

        self.tv.channel_down()
        self.assertEqual(self.tv.channel, "Channel set to 0")

    def test_set_channel(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.tv.set_channel(26)
        self.assertEqual(self.tv.channel, "Channel set to 26")

    def test_cannot_increment_to_channel_past_50(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.tv.set_channel(50)
        self.assertEqual(self.tv.channel, "Channel set to 50")

        self.assertEqual(self.tv.channel_up(), "Channel cannot exceed 50")

    def test_cannot_decrement_to_channel_below_0(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.channel, "Channel set to 0")

        self.assertEqual(self.tv.channel_down(), "Channel cannot fall below 0")

    def test_cannot_set_channel_beyond_50_or_below_0(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.set_channel(51), "Channel cannot neither exceed 50 nor fall below 0")
        self.assertEqual(self.tv.channel, "Channel set to 0")

        self.assertEqual(self.tv.set_channel(-1), "Channel cannot neither exceed 50 nor fall below 0")
        self.assertEqual(self.tv.channel, "Channel set to 0")

    def test_cannot_change_channel_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)

        self.assertEqual(self.tv.channel_up(), "TV is off")
        self.assertEqual(self.tv.channel_down(), "TV is off")
        self.assertEqual(self.tv.set_channel(10), "TV is off")

        self.tv.turn_on()
        self.assertEqual(self.tv.channel, "Channel set to 0")

    def test_mute_tv(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.assertEqual(self.tv.is_mute, "TV is not muted")

        self.tv.mute()
        self.assertEqual(self.tv.is_mute, "TV is muted")

    def test_unmute_tv(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.tv.mute()
        self.assertTrue(self.tv.is_mute)

        self.tv.unmute()
        self.assertEqual(self.tv.is_mute, "TV is not muted")

    def test_cannot_get_mute_state_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)

        self.assertEqual(self.tv.is_mute, "TV is off")

    def test_cannot_mute_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)

        self.assertEqual(self.tv.mute(), "TV is off")
        self.tv.turn_on()
        self.assertEqual(self.tv.is_mute, "TV is not muted")

    def test_cannot_unmute_if_tv_is_off(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

        self.tv.mute()
        self.assertEqual(self.tv.is_mute, "TV is muted")

        self.tv.turn_off()
        self.assertEqual(self.tv.unmute(), "TV is off")

        self.tv.turn_on()
        self.assertEqual(self.tv.is_mute, "TV is muted")