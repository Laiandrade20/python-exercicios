# Estimador de orçamento em ACM

Projeto inicial de portfólio que aplica Python a um problema real da área de projetos e orçamentos.

## O que a aplicação calcula

- área de material com percentual de perda;
- custo estimado do material;
- custo estimado de instalação;
- valor total do orçamento.

## Como executar

Na raiz do repositório, rode:

```bash
python -m projetos.estimador_acm.main
```

Exemplo de entrada:

```text
Área líquida (m²): 50
Preço do material por m²: R$ 150
Percentual de perda [%]: 10
Custo de instalação por m²: R$ 50
```

Resultado esperado:

```text
Área de compra: 55.00 m²
Material: R$ 8.250,00
Instalação: R$ 2.500,00
Total estimado: R$ 10.750,00
```

## Testes

Instale a dependência de desenvolvimento e execute o Pytest:

```bash
python -m pip install -r requirements-dev.txt
pytest
```

Os testes verificam o cálculo principal, o cenário sem perda e o tratamento de valores inválidos.

## Evolução planejada

1. Criar uma API com FastAPI.
2. Persistir orçamentos em banco de dados SQL.
3. Analisar os dados com Pandas.
4. Gerar relatórios automaticamente.
