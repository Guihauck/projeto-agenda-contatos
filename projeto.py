import funcoesProjeto

listaContatos = []
while True:
  print("\n======= Gerenciador de contatos: =======");
  print("1. Adicionar contato");
  print("2. Visualizar lista de contatos");
  print("3. Editar contato");
  print("4. Marcar/desmarcar um contato como favorito");
  print("5. Visualizar lista de contatos favoritos");
  print("6. Apagar contato");
  print("7. Sair");

  selecaoOpcoes = input("Digite uma opcão: ")

  if selecaoOpcoes == "1":
    adicionarContatoNovo = input("Insira o nome do contato: ")
    adicionarContatoTelefone = input("Insira o telefone do contato: ")
    adicionarContatoEmail = input("Insira o E-mail do contato: ")
    (listaContatos, adicionarContatoNovo, adicionarContatoTelefone, adicionarContatoEmail)
  elif selecaoOpcoes == "2":
    (listaContatos)
  elif selecaoOpcoes == "3":
    (listaContatos)
    indice_contato = input("Digite o número do contato que deseja alterar: ")
    novoNomeContato = input("Digite o novo nome do contato: ")
    novoTelefoneContato = input("Digite o novo Telefone: ")
    novoEmailContato = input("Digite o novo Email: ")
    (listaContatos, indice_contato, novoNomeContato, novoTelefoneContato, novoEmailContato)
  elif selecaoOpcoes == "4":
    (listaContatos)
    selecaoContato = input("Digite o número índice do contato que deseja favoritar: ")
    (listaContatos, selecaoContato)
  elif selecaoOpcoes == "5":
    (listaContatos)
  elif selecaoOpcoes == "6":
    (listaContatos)
    selecaoContato = input("Digite o número do contato que deseja deletar: ")
    (listaContatos, selecaoContato)
  elif selecaoOpcoes == "7":
    break
