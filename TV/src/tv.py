class TV:

    def __init__(self):
        self.__is_on = False
        self.__volume = 0
        self.__channel = 0
        self.__is_muted = False

    @property
    def is_on(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    @property
    def volume(self):
        if self.__is_on: return f"Volume: {self.__volume}"
        return "TV is off"

    def increase_volume_by(self, amount):
        if self.__is_on:
            if self.__volume + amount <= 100:
                self.__volume += amount
                return f"Volume set to {self.__volume}"
            else:
                return "Volume cannot exceed 100"
        return "TV is off"

    def decrease_volume_by(self, amount):
        if self.__is_on:
            if self.__volume - amount >= 0:
                self.__volume -= amount
                return f"Volume set to {self.__volume}"
            else:
                return "Volume cannot fall below 0"
        return "TV is off"

    @property
    def channel(self):
        if self.__is_on: return f"Channel set to {self.__channel}"
        return "TV is off"

    def channel_down(self):
        if self.__is_on:
            if self.__channel != 0:
                self.__channel -= 1
                return f"Channel set to {self.__channel}"
            return "Channel cannot fall below 0"
        return "TV is off"

    def channel_up(self):
        if self.__is_on:
            if self.__channel != 50:
                self.__channel += 1
                return f"Channel set to {self.__channel}"
            return "Channel cannot exceed 50"
        return "TV is off"

    def set_channel(self, channel: int):
        if self.__is_on:
            if isinstance(channel, int):
                if 50 >= channel >= 0:
                    self.__channel = channel
                    return f"Channel set to {self.__channel}"
                return "Channel cannot neither exceed 50 nor fall below 0"
            return TypeError("Value must be an integer")
        return "TV is off"

    @property
    def is_mute(self):
        if self.__is_on:
            if self.__is_muted: return "TV is muted"
            return "TV is not muted"
        return "TV is off"

    def mute(self):
        if self.__is_on:
            if self.__is_muted: return "TV is already muted"
            self.__is_muted = True
            return "TV is muted"
        return "TV is off"

    def unmute(self):
        if self.__is_on:
            if not self.__is_muted: return "TV is already not muted"
            self.__is_muted = False
            return "TV is not muted"
        return "TV is off"
