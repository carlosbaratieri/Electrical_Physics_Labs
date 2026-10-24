from manim import *

def primeiraParte(cena):
    modeloTex = TexTemplate()
    modeloTex.add_to_preamble(
        r"\usepackage[siunitx, RPvoltages, american]{circuitikz}"
    )

    circuito = MathTex(
        r"""\draw [line width=0.2pt] (6.25,5.5) to[american voltage source, l=6\,V] (6.25,8.5);""",
        r"""\draw [line width=0.2pt] (6.25,8.5) to[short] (7,8.5);""",
        r"""\draw [line width=0.2pt] (7,8.5) to[R, l=3$\Omega$] (8.25,8.5);""",
        r"""\draw [line width=0.2pt] (8.25,8.5) to[opening switch] node[midway, above, yshift=10pt, xshift=-10pt] {$t=0$} (9.75,8.5);""",
        r"""\draw [line width=0.2pt] (9.75,8.5) to[R, l_=1$\Omega$] (9.75,5.5);""",
        r"""\draw [line width=0.2pt] (6.25,5.5) to[short] (9.75,5.5);""",
        r"""\draw [line width=0.2pt] (9.75,5.5) to[short] (11.5,5.5);""",
        r"""\draw [line width=0.2pt] (9.75,8.5) to[short] (11.5,8.5);""",
        r"""\draw [line width=0.2pt] (11.5,5.5) to[L, l=$\tfrac{1}{2}$\,H] (11.5,8.5);""",
        r"""\draw [line width=0.2pt] (11.5,8.5) to[short] (13.25,8.5);""",
        r"""\draw [line width=0.2pt] (11.5,5.5) to[short] (13.25,5.5);""",
        r"""\draw [line width=0.2pt] (13.25,5.5) to[C, l=$\tfrac{1}{4}$\,F] (13.25,8.5);""",
        tex_environment="circuitikz",
        tex_template=modeloTex,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1
    )

    circuito.move_to(ORIGIN)
    circuito.set_color(GREEN)

    for parte in circuito:
        cena.play(Create(parte), run_time=0.7)

    return circuito


class CenaPrincipal(Scene):
    def construct(self):
        circuito = primeiraParte(self)
        self.wait(1)
        
        modeloTex = TexTemplate()
        modeloTex.add_to_preamble(
            r"\usepackage[siunitx, RPvoltages, american]{circuitikz}"
        )
        
        chaveFechada = MathTex(
            r"""\draw [line width=0.2pt] (8.25,8.5) to[closing switch] node[midway, above, yshift=10pt, xshift=-10pt] {$t=0$} (9.75,8.5);""",
            tex_environment="circuitikz",
            tex_template=modeloTex,
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=1
        )
        chaveFechada.set_color(GREEN)
        chaveFechada.move_to(circuito[3].get_center())
        chaveFechada.shift(DOWN * 0.035)

        fio = MathTex(
            r"""\draw [line width=0.2pt] (3.669,4.5) to[short] (3.75,4.5);""",
            tex_environment="circuitikz",
            tex_template=modeloTex,
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=1
        )
        fio.set_color(GREEN)
        fio.move_to(chaveFechada.get_center())
        fio.shift(DOWN * 0.433)
        
        self.play(ReplacementTransform(circuito[3], chaveFechada))
        self.wait(1)
        self.play(ReplacementTransform(chaveFechada, fio))
        self.wait(1)
        
        indutor = circuito[8]
        self.play(indutor.animate.set_color(ORANGE), run_time=1)
        self.wait(1)

        fioIndutor = MathTex(
            r"""\draw [line width=0.2pt] (11.5,5.5) to[short] (11.5,8.5);""",
            tex_environment="circuitikz",
            tex_template=modeloTex,
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=1
        )
        fioIndutor.set_color(PURPLE)
        fioIndutor.move_to(indutor.get_center())
        self.play(ReplacementTransform(indutor, fioIndutor))
        self.wait(1)
        
        resistor1Ohm = circuito[4]
        self.play(resistor1Ohm.animate.set_color(ORANGE), run_time=1)
        self.wait(1)
        self.play(FadeOut(resistor1Ohm), run_time=1)
        self.wait(1)
        
        capacitor = circuito[11]
        self.play(capacitor.animate.set_color(YELLOW), run_time=1)
        self.wait(1)
        self.play(FadeOut(capacitor), run_time=1)
        self.wait(1)

        terminaisAbertos = MathTex(
            r"""\draw [line width=0.2pt] (13.25,5.5) to[short, -o] (13.25,6.7);
                \draw [line width=0.2pt] (13.25,7.3) to[short, o-] (13.25,8.5);""",
            tex_environment="circuitikz",
            tex_template=modeloTex,
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=1
        )
        terminaisAbertos.set_color(GREEN)
        terminaisAbertos.move_to(capacitor.get_center())
        terminaisAbertos.shift(RIGHT * 0.4)

        self.play(Create(terminaisAbertos), run_time=1)
        self.wait(1)

        circuitoFinal = Group(*self.mobjects)
        self.play(
            circuitoFinal.animate.scale(0.6).shift(LEFT * 3.3),
            run_time=1.5
        )
        self.wait(1)
        
        equacao1 = MathTex("i(t)")
        equacao2 = MathTex("=")
        equacao3 = MathTex("i_L(0^-)")
        equacao4 = MathTex("\\frac{E}{R_{eq}}") 
        equacao5 = MathTex("\\frac{6\\,\\text{V}}{3\\,\\Omega}")  
        equacao6 = MathTex("2\\,\\text{A}")                      

        posicaoInicial = RIGHT * 3.58 + UP * 2.5
        equacao1.move_to(posicaoInicial)

        self.play(Write(equacao1))
        self.wait(0.5)

        self.play(equacao1.animate.shift(LEFT * 0.3))
        self.wait(0.3)

        equacao2.next_to(equacao1, RIGHT)
        self.play(Write(equacao2))
        self.wait(0.3)

        equacao3.next_to(equacao2, RIGHT)
        self.play(Write(equacao3))
        self.wait(0.5)

        posicaoAlvo = equacao1.get_center()

        self.play(FadeOut(equacao1), FadeOut(equacao2))
        self.wait(0.2)

        self.play(equacao3.animate.move_to(posicaoAlvo))
        self.wait(0.5)

        equacao2 = MathTex("=")
        equacao2.next_to(equacao3, RIGHT)
        self.play(FadeIn(equacao2))

        equacao4.next_to(equacao2, RIGHT)
        self.play(FadeIn(equacao4))
        self.wait(0.5)

        equacao5.move_to(equacao4.get_center())
        self.play(Transform(equacao4, equacao5))
        self.wait(0.5)

        equacao6.move_to(equacao4.get_center())
        self.play(Transform(equacao4, equacao6))
        self.wait(0.7)

        grupoFinal = VGroup(equacao3, equacao2, equacao4)
        self.wait(0.5)

        destaque1 = SurroundingRectangle(grupoFinal, color=PURPLE, buff=0.3)
        self.play(Create(destaque1))
        self.wait(1)
       
        self.wait(0.5)
        
        equacao1_2 = MathTex("V_{3\\Omega}")
        equacao2_2 = MathTex("=")
        equacao3_2 = MathTex("i_t \\cdot R_{3\\Omega}")
        equacao4_2 = MathTex("2\\,\\text{A} \\cdot 3\\,\\Omega")
        equacao5_2 = MathTex("6\\,\\text{V}")

        posicaoFinal2 = UP * 0.5 + RIGHT * 3.0
        equacao1_2.move_to(posicaoFinal2)

        self.play(Write(equacao1_2))
        self.wait(0.5)

        equacao2_2.next_to(equacao1_2, RIGHT, buff=0.3)
        self.play(Write(equacao2_2))
        self.wait(0.3)

        equacao3_2.next_to(equacao2_2, RIGHT, buff=0.3)
        self.play(Write(equacao3_2))
        self.wait(0.5)

        equacao4_2.move_to(equacao3_2.get_center())
        self.play(Transform(equacao3_2, equacao4_2))
        self.wait(0.5)

        equacao5_2.move_to(equacao3_2.get_center())
        self.play(Transform(equacao3_2, equacao5_2))
        self.wait(0.7)
        
        self.play(equacao3_2.animate.shift(LEFT * 0.5))

        grupoFinal2 = VGroup(equacao1_2, equacao2_2, equacao3_2)
        self.wait(0.5)

        destaque2 = SurroundingRectangle(grupoFinal2, color=ORANGE, buff=0.3)
        self.play(Create(destaque2))
        self.wait(1)
        
        grupoCompleto2 = VGroup(grupoFinal2, destaque2)
        self.play(grupoCompleto2.animate.shift(RIGHT * 0.3))
        self.wait(1)

        equacaoIndutor = MathTex("V_{L}(0^-)", "=", "0\\,\\text{V}")
        
        posicaoFinal3 = DOWN * 1.5 + RIGHT * 4.0
        equacaoIndutor.move_to(posicaoFinal3)
        
        self.play(Write(equacaoIndutor))
        self.wait(0.5)
        
        destaque3 = SurroundingRectangle(equacaoIndutor, color=PINK, buff=0.3)
        self.play(Create(destaque3))
        self.wait(2)
