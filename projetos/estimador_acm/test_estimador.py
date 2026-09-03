import unittest

from projetos.estimador_acm.estimador import calcular_orcamento


class TestCalcularOrcamento(unittest.TestCase):
    def test_calcula_material_instalacao_e_total(self) -> None:
        resultado = calcular_orcamento(
            area_liquida_m2=50,
            preco_material_m2=150,
            percentual_perda=10,
            custo_instalacao_m2=50,
        )

        self.assertEqual(resultado.area_compra_m2, 55)
        self.assertEqual(resultado.custo_material, 8250)
        self.assertEqual(resultado.custo_instalacao, 2500)
        self.assertEqual(resultado.custo_total, 10750)

    def test_calcula_sem_perda_e_sem_instalacao(self) -> None:
        resultado = calcular_orcamento(
            area_liquida_m2=20,
            preco_material_m2=100,
            percentual_perda=0,
        )

        self.assertEqual(resultado.area_compra_m2, 20)
        self.assertEqual(resultado.custo_total, 2000)

    def test_rejeita_area_igual_a_zero(self) -> None:
        with self.assertRaisesRegex(ValueError, "área líquida"):
            calcular_orcamento(area_liquida_m2=0, preco_material_m2=100)

    def test_rejeita_preco_negativo(self) -> None:
        with self.assertRaisesRegex(ValueError, "material"):
            calcular_orcamento(area_liquida_m2=10, preco_material_m2=-1)

    def test_rejeita_perda_negativa(self) -> None:
        with self.assertRaisesRegex(ValueError, "perda"):
            calcular_orcamento(
                area_liquida_m2=10,
                preco_material_m2=100,
                percentual_perda=-5,
            )


if __name__ == "__main__":
    unittest.main()
