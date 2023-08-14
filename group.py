from manim import *
from math import *

config.background_color = "#ffffcc"


def createTriangle():
    t = Triangle(color=BLACK)
    red = Dot(color=RED)
    blue = Dot(color=BLUE)
    red.align_to(t, UP).shift(0.2 * DOWN)
    blue.align_to(t, DR).shift(0.1 * LEFT)
    g = VGroup(t, red, blue)
    return g


class D3(Scene):
    def construct(self):
        # identity
        t0 = createTriangle().shift(1.5 * UL + 2 * LEFT)
        e = Tex(
            "e",
            color=BLACK,
            font_size=36,
            tex_template=TexFontTemplates.latin_modern_tw,
        )
        e.next_to(t0, UL, buff=0.1)
        # rotate 120
        t1 = createTriangle().shift(1.5 * UP)
        r1 = MathTex(
            r"\rho",
            color=BLACK,
            font_size=36,
            tex_template=TexFontTemplates.latin_modern_tw,
        )
        r1.next_to(t1, UL, buff=0.1)
        # rotate 240
        t2 = createTriangle().shift(1.5 * UR + 2 * RIGHT)
        r2 = MathTex(
            r"\rho^2",
            color=BLACK,
            font_size=36,
            tex_template=TexFontTemplates.latin_modern_tw,
        )
        r2.next_to(t2, UL, buff=0.1)
        # reflect y-axis
        t3 = createTriangle().shift(1.5 * DL + 2 * LEFT)
        r3 = MathTex(
            r"r_1",
            color=BLACK,
            font_size=36,
            tex_template=TexFontTemplates.latin_modern_tw,
        )
        r3.next_to(t3, UL, buff=0.1)
        # reflect by UR axis
        t4 = createTriangle().shift(1.5 * DOWN)
        r4 = MathTex(
            r"r_2",
            color=BLACK,
            font_size=36,
            tex_template=TexFontTemplates.latin_modern_tw,
        )
        r4.next_to(t4, UL, buff=0.1)
        # make direction array
        left = t4[0].get_vertices()[1]
        right_mid = midpoint(t4[0].get_vertices()[0], t4[0].get_vertices()[2])
        left_to_up_right = right_mid - left
        # reflect by UL axis
        t5 = createTriangle().shift(1.5 * DR + 2 * RIGHT)
        r5 = MathTex(
            r"r_3",
            color=BLACK,
            font_size=36,
            tex_template=TexFontTemplates.latin_modern_tw,
        )
        r5.next_to(t5, UL, buff=0.1)
        # make direction array
        right = t5[0].get_vertices()[2]
        left_mid = midpoint(t5[0].get_vertices()[0], t5[0].get_vertices()[1])
        right_to_up_left = left_mid - right
        # create all triangles
        self.play(
            Create(t0),
            Create(e),
            Create(t1),
            Create(r1),
            Create(t2),
            Create(r2),
            Create(t3),
            Create(r3),
            Create(t4),
            Create(r4),
            Create(t5),
            Create(r5),
        )
        # play animation (change about point to fix the shift after rotation)
        self.play(
            Rotate(
                t1,
                angle=2 / 3 * PI,
                about_point=[-3.33066907e-16, 1.50000000e00, 0.00000000e00],
            )
        )
        self.play(Rotate(t2, angle=4 / 3 * PI, about_point=[3.5, 1.5, 0.0]))
        self.play(Rotate(t3, angle=PI, axis=UP))
        self.play(
            Rotate(
                t4,
                angle=PI,
                axis=left_to_up_right,
                about_point=[0.2888528, -1.37368421, 0],
            )
        )
        self.play(
            Rotate(
                t5,
                angle=PI,
                axis=right_to_up_left,
                about_point=[3.7888528, -1.60368421, 0.0],
            )
        )
