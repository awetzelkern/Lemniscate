from manim import *

class Lemniscate(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[-2, 2, 0.5], 
            y_range=[-1, 1, 0.5], 
            axis_config={"include_numbers": False}
        )

        # Add labels to the axes
        # labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Define the lemniscate equation in parametric form
        lemniscate = ParametricFunction(
            lambda t: axes.coords_to_point(
                np.sqrt(2) * np.cos(t) / (1 + np.sin(t) ** 2),
                np.sqrt(2) * np.cos(t) * np.sin(t) / (1 + np.sin(t) ** 2),
            ),
            t_range=np.array([0, 2 * PI]),
            color=BLUE_C,
            stroke_width=16
        )

        # Draw everything
        # self.play(Create(axes), Write(labels))
        self.play(Create(lemniscate), runtime=3)
        self.wait(2)
