from manim import *

class WhiteDotAnimation(Scene):
    def construct(self):
        # Définir le fond noir
        black_background = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0,
        )

        # Créer le point blanc initial
        white_dot = Dot(color=WHITE).shift(ORIGIN)

        # Ajouter le point blanc à la scène
        self.play(FadeIn(black_background))
        self.play(FadeIn(white_dot))

        # Animation d'expansion rapide
        self.play(white_dot.animate.scale(20), run_time=0.5)

        # Animation de réduction brève
        self.play(white_dot.animate.scale(0.1), run_time=0.1)

        # Stabilisation (pause)
        self.wait(0.2)

        # Animation de fade-out
        self.play(FadeOut(white_dot), run_time=1)

