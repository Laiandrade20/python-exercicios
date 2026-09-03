"""Interface de linha de comando do estimador de orçamento em ACM."""

from .estimador import calcular_orcamento


def ler_numero(mensagem: str) -> float:
    """Lê números aceitando vírgula ou ponto como separador decimal."""
    return float(input(mensagem).strip().replace(",", "."))


def formatar_reais(valor: float) -> str:
    """Formata um número no padrão monetário brasileiro."""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "_").replace(".", ",").replace("_", ".")


def main() -> None:
    print("\nEstimador de orçamento em ACM\n")

    try:
        area = ler_numero("Área líquida (m²): ")
        preco_material = ler_numero("Preço do material por m²: R$ ")
        perda = ler_numero("Percentual de perda [%]: ")
        instalacao = ler_numero("Custo de instalação por m²: R$ ")

        resultado = calcular_orcamento(
            area_liquida_m2=area,
            preco_material_m2=preco_material,
            percentual_perda=perda,
            custo_instalacao_m2=instalacao,
        )
    except ValueError as erro:
        print(f"\nNão foi possível calcular: {erro}")
        return

    print("\nResumo da estimativa")
    print(f"Área líquida: {resultado.area_liquida_m2:.2f} m²")
    print(f"Área de compra: {resultado.area_compra_m2:.2f} m²")
    print(f"Material: {formatar_reais(resultado.custo_material)}")
    print(f"Instalação: {formatar_reais(resultado.custo_instalacao)}")
    print(f"Total estimado: {formatar_reais(resultado.custo_total)}")


if __name__ == "__main__":
    main()
