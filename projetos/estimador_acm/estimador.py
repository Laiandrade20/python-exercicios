"""Regras de cálculo para estimativas de orçamento em ACM."""

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class OrcamentoACM:
    """Resultado consolidado de uma estimativa de ACM."""

    area_liquida_m2: float
    percentual_perda: float
    area_compra_m2: float
    preco_material_m2: float
    custo_instalacao_m2: float
    custo_material: float
    custo_instalacao: float
    custo_total: float

    def como_dicionario(self) -> dict[str, float]:
        """Retorna os valores do orçamento em formato reutilizável."""
        return asdict(self)


def _validar_numero_nao_negativo(nome: str, valor: float) -> None:
    if valor < 0:
        raise ValueError(f"{nome} não pode ser negativo.")


def calcular_orcamento(
    area_liquida_m2: float,
    preco_material_m2: float,
    percentual_perda: float = 10.0,
    custo_instalacao_m2: float = 0.0,
) -> OrcamentoACM:
    """Calcula uma estimativa simples de material e instalação.

    A perda é aplicada somente à quantidade de material. O custo de instalação
    considera a área líquida efetivamente instalada.
    """
    if area_liquida_m2 <= 0:
        raise ValueError("A área líquida deve ser maior que zero.")

    _validar_numero_nao_negativo("O preço do material", preco_material_m2)
    _validar_numero_nao_negativo("O percentual de perda", percentual_perda)
    _validar_numero_nao_negativo("O custo de instalação", custo_instalacao_m2)

    area_compra_m2 = area_liquida_m2 * (1 + percentual_perda / 100)
    custo_material = area_compra_m2 * preco_material_m2
    custo_instalacao = area_liquida_m2 * custo_instalacao_m2

    return OrcamentoACM(
        area_liquida_m2=round(area_liquida_m2, 2),
        percentual_perda=round(percentual_perda, 2),
        area_compra_m2=round(area_compra_m2, 2),
        preco_material_m2=round(preco_material_m2, 2),
        custo_instalacao_m2=round(custo_instalacao_m2, 2),
        custo_material=round(custo_material, 2),
        custo_instalacao=round(custo_instalacao, 2),
        custo_total=round(custo_material + custo_instalacao, 2),
    )
