def adicionarContato(listaContatos, nomeContato, telefoneContato, emailContato):
  dicContatos = {"nome":nomeContato,"telefone":telefoneContato,"email":emailContato, "favoritarContato": False}
  listaContatos.append(dicContatos)
  print(f"\nO contato de {nomeContato} foi adicionado com sucesso!")
  return

def enxergarListaContatos(listaContatos):
  print("\nSua lista de contatos: ")
  for indice, listaContatos in enumerate(listaContatos, start=1):
    contatosFavoritados = "⭐" if listaContatos["favoritarContato"] else ""
    nomeContato = listaContatos["nome"]
    telefoneContato = listaContatos["telefone"]
    emailContato = listaContatos["email"]
    print(f"{indice}. Nome: {nomeContato} Telefone: {telefoneContato} E-mail: {emailContato} Favoritado: [{contatosFavoritados}]")
  return

def editarContato(listaContatos, indiceContato, novoNomeContato, novoTelefoneContato, novoEmailContato):
  indiceAjustado = int(indiceContato) - 1
  if indiceAjustado >=0 and indiceAjustado < len(listaContatos):
    listaContatos[indiceAjustado]["nome"] = novoNomeContato
    listaContatos[indiceAjustado]["telefone"] = novoTelefoneContato
    listaContatos[indiceAjustado]["email"] = novoEmailContato
    print(f"Dados do contato alterado: Nome: {novoNomeContato} Telefone: {novoTelefoneContato} Novo E-mail: {novoEmailContato}" )
  else:
    print("Número inválido! Número digitado não confere com a quantidade de itens na lista de contato!")
  return

def contatoFavoritado(listaContatos,indiceContatoFavoritado):
  indiceContatoAjustado = int(indiceContatoFavoritado) - 1
  contatoFavoritado = listaContatos[indiceContatoAjustado]["favoritarContato"]
  listaContatos[indiceContatoAjustado]["favoritarContato"] = not contatoFavoritado
  contatoMensagem  = "desfavoritado" if contatoFavoritado else "favoritado"
  print(f"O contato {indiceContatoFavoritado} foi {contatoMensagem}")
  return

def visualizarFavoritos(listaContatos):
  print("\nLista dos seu contatos favoritados: ")
  favoritos = [contatos for contatos in listaContatos if contatos["favoritarContato"] is True]
  if favoritos:
    for contato in listaContatos:
      print(f"Nome: {contato["nome"]} Telefone: {contato["telefone"]} E-mail: {contato["email"]}")
  else: ""

def deletarContato(listaContatos, indiceContato):
  indiceAjuste = int(indiceContato) - 1
  listaContatos.pop(indiceAjuste)
  print(f"O contato {indiceContato} foi removido da sua agenda.")
  
  return

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
    adicionarContato(listaContatos, adicionarContatoNovo, adicionarContatoTelefone, adicionarContatoEmail)
  elif selecaoOpcoes == "2":
    enxergarListaContatos(listaContatos)
  elif selecaoOpcoes == "3":
    enxergarListaContatos(listaContatos)
    indice_contato = input("Digite o número do contato que deseja alterar: ")
    novoNomeContato = input("Digite o novo nome do contato: ")
    novoTelefoneContato = input("Digite o novo Telefone: ")
    novoEmailContato = input("Digite o novo Email: ")
    editarContato(listaContatos, indice_contato, novoNomeContato, novoTelefoneContato, novoEmailContato)
  elif selecaoOpcoes == "4":
    enxergarListaContatos(listaContatos)
    selecaoContato = input("Digite o número índice do contato que deseja favoritar: ")
    contatoFavoritado(listaContatos, selecaoContato)
  elif selecaoOpcoes == "5":
    visualizarFavoritos(listaContatos)
  elif selecaoOpcoes == "6":
    enxergarListaContatos(listaContatos)
    selecaoContato = input("Digite o número do contato que deseja deletar: ")
    deletarContato(listaContatos, selecaoContato)
  elif selecaoOpcoes == "7":
    break
