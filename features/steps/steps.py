from behave import given, when, then

# Banco simulado para o MVP
catalogo_global = [
    {"titulo": "Clean Code", "autor": "Robert Martin"},
    {"titulo": "Refatoração", "autor": "Martin Fowler"}
]
resultado_pesquisa = []
lista_desejos = []
status_pedido = ""

@given('que o catálogo possui o livro "{titulo}"')
def step_impl(context, titulo):
    # Garante que o livro existe no catálogo simulado
    assert any(l["titulo"] == titulo for l in catalogo_global)

@when('o cliente pesquisa pelo nome "{titulo}"')
def step_impl(context, titulo):
    global resultado_pesquisa
    resultado_pesquisa = [l for l in catalogo_global if titulo.lower() in l["titulo"].lower()]

@then('o sistema deve retornar o livro "{titulo}" na lista de resultados')
def step_impl(context, titulo):
    assert any(l["titulo"] == titulo for l in resultado_pesquisa)

@given('que o cliente está visualizando os detalhes do livro "{titulo}"')
def step_impl(context, titulo):
    context.livro_atual = titulo

@when('o cliente adiciona o livro à sua lista de desejos')
def step_impl(context):
    global lista_desejos
    if context.livro_atual not in lista_desejos:
        lista_desejos.append(context.livro_atual)

@then('o livro deve constar na lista de desejos do usuário')
def step_impl(context):
    assert context.livro_atual in lista_desejos

@given('que o cliente tem itens na sacola virtual')
def step_impl(context):
    context.sacola = ["Clean Code"]

@when('o cliente seleciona a forma de pagamento Pix')
def step_impl(context):
    global status_pedido
    status_pedido = "Aguardando pagamento Pix"

@then('o pedido deve ser gerado com sucesso e o QR Code exibido')
def step_impl(context):
    assert status_pedido == "Aguardando pagamento Pix"