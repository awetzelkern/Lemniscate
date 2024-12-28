from manim import *

class Lemniscate(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[-2, 2, 0.5], 
            y_range=[-2, 2, 0.5], 
            axis_config={"include_numbers": True}
        )

        # Add labels to axes
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Define the lemniscate equation in polar coordinates
        lemniscate = ParametricFunction(
            lambda t: axes.coords_to_point(
                np.sqrt(2) * np.cos(t) / (np.sin(t) ** 2 + 1),
                np.sqrt(2) * np.cos(t) * np.sin(t) / (np.sin(t) ** 2 + 1),
            ),
            t_range=np.array([-PI / 4, 5 * PI / 4]),
            color=BLUE,
        )

        # Draw everything
        self.play(Create(axes), Write(labels))
        self.play(Create(lemniscate))
        self.wait(2)
