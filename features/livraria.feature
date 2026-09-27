# language: pt
Funcionalidade: MVP da Livraria Digital
  Como cliente da livraria
  Quero interagir com o aplicativo para pesquisar, gerenciar lista de desejos e realizar pagamentos
  Para ter uma experiência de compra ágil e integrada com a loja física

  Cenário: Pesquisar um livro pelo nome
    Dado que o catálogo possui o livro "Clean Code"
    Quando o cliente pesquisa pelo nome "Clean Code"
    Então o sistema deve retornar o livro "Clean Code" na lista de resultados

  Cenário: Adicionar livro à lista de desejos
    Dado que o cliente está visualizando os detalhes do livro "Refatoração"
    Quando o cliente adiciona o livro à sua lista de desejos
    Então o livro deve constar na lista de desejos do usuário

  Cenário: Realizar pagamento com Pix
    Dado que o cliente tem itens na sacola virtual
    Quando o cliente seleciona a forma de pagamento Pix
    Então o pedido deve ser gerado com sucesso e o QR Code exibido