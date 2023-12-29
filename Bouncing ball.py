from manim import *
import os

class BallFalling(Scene):
    def construct(self):
        # Create a ball
        ball = Circle(color=WHITE, radius=1, fill_opacity=1)
        circle = Circle(color=WHITE, radius=1, fill_opacity=0)

        ball_apparition = ball.animate(
            ApplyMethod(ball.scale, 0.9),
        )
        circle_apparition = circle.animate(
            ApplyMethod(circle.scale, 1.2),
            ApplyMethod(circle.set_opacity, 0),
        )

        self.wait(1)
        self.play(Create(ball), Create(circle), run_time = 0)
        self.play(ball_apparition, circle_apparition, run_time = 2)

class PointAnimation(Scene):
    def construct(self):
        # Création du point blanc
        dot = Dot(color=WHITE, radius=1)

        # Étape 1 : Apparition du point
        self.add(dot)

        # Étape 2 : Réduction de taille
        self.play(dot.animate.scale(0.8))

        # Étape 4 : Taille maximale
        self.play(dot.animate.scale(1.5))

        # Étape 5 : Retour à la taille initiale
        self.play(dot.animate.scale(1))

        self.wait(1)  # Attendre un moment à la fin


def main():
    os.chdir("C:/Users/Hugues/Desktop/TikTok/Manim animation/")
    config.pixel_height = 1920
    config.pixel_width = 1080
    PointAnimation().render()

# Render the animation with the custom aspect ratio
if __name__ == "__main__":
    main()