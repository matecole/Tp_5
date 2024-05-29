import enum, arcade



class AttackType(enum.Enum):

   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2
   BOT = 3



class AttackAnimations(arcade.Sprite):
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type, pos_x, pos_y):
        super().__init__(center_x=pos_x, center_y=pos_y)

        self.number_of_swaps = 0
        self.animation_update_time = 1.0 / AttackAnimations.ANIMATION_SPEED
        self.time_since_last_swap = 0.0
        self.attack_type = attack_type
        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png"),
            ]
        elif self.attack_type == AttackType.SCISSORS:
            self.textures = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png"),
            ]
        elif self.attack_type == AttackType.BOT:
            self.textures = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/srock.png"),
            ]


        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def on_update(self, delta_time: float = 1 / 60):
        # Update the animation.
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:

            self.current_texture += 1

            self.number_of_swaps += 1

            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0