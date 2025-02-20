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