from manim import *
import numpy as np


class GraficoExponencial(Scene):
    def construct(self):

        def calcularTensao(tempo):
            return -4 * np.exp(-2 * tempo) * np.sin(2 * tempo)

        formulaTexto = Tex(
            r"$V(t) = -4e^{-2t}\sin(2t)$",
            color=PURPLE
        ).scale(0.9)

        self.play(FadeIn(formulaTexto))
        self.wait(0.5)

        self.play(formulaTexto.animate.to_edge(UP))
        self.wait(0.5)

        retanguloDestaque = SurroundingRectangle(
            formulaTexto,
            color=PINK,
            buff=0.2,
            stroke_width=2
        )

        self.play(Create(retanguloDestaque))
        self.wait(0.5)
        
        limiteX = 2.5
        limiteYMin = -2
        limiteYMax = 4

        rastreadorX = ValueTracker(0.01)
        rastreadorY = ValueTracker(0.01)

        eixosAnimados = always_redraw(
            lambda: Axes(
                x_range=[0, rastreadorX.get_value(), 0.5],
                y_range=[limiteYMin, rastreadorY.get_value(), 1],
                x_length=8,
                y_length=5,
                axis_config={
                    "color": GREEN,
                    "stroke_width": 2,
                    "include_numbers": True,
                    "font_size": 20,
                    "tip_width": 0.15,
                    "tip_height": 0.15,
                },
            ).add_coordinates()
        )

        self.add(eixosAnimados)

        self.play(
            rastreadorX.animate.set_value(limiteX),
            rastreadorY.animate.set_value(limiteYMax),
            run_time=2.5,
            rate_func=smooth
        )

        self.remove(eixosAnimados)

        eixosFixos = Axes(
            x_range=[0, limiteX, 0.5],
            y_range=[limiteYMin, limiteYMax, 1],
            x_length=8,
            y_length=5,
            axis_config={
                "color": GREEN,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 20,
                "tip_width": 0.15,
                "tip_height": 0.15,
            },
        ).add_coordinates()

        self.add(eixosFixos)

        rotuloTempo = Tex("t", color=GREEN, font_size=24).next_to(
            eixosFixos.x_axis.get_end(), DOWN, buff=0.1
        )
        rotuloTensao = Tex("V", color=GREEN, font_size=24).next_to(
            eixosFixos.y_axis.get_end(), LEFT, buff=0.1
        )

        self.add(rotuloTempo, rotuloTensao)
        self.wait(0.5)

        controleTempo = ValueTracker(0)

        graficoTensao = always_redraw(
            lambda: eixosFixos.plot(
                calcularTensao,
                x_range=[0, controleTempo.get_value(), 0.01],
                color=ORANGE,
                stroke_width=4
            )
        )

        pontoAtual = always_redraw(
            lambda: Dot(
                eixosFixos.c2p(
                    controleTempo.get_value(),
                    calcularTensao(controleTempo.get_value())
                ),
                color=RED,
                radius=0.06
            )
        )

        self.add(graficoTensao, pontoAtual)

        self.play(
            controleTempo.animate.set_value(2.439),
            run_time=10
        )

        self.wait(2)

