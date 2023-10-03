# r = read(leitura)
# w = write(escrita)
# 1º passo : abrir o arquvo em mémoria
arquivo = open("./arquivo.txt","r")
# 2º passo : ler o conteudo do arquivo
conteudo = arquivo.read()
print(conteudo)
# 3º passo: fechar o arquivo aberto
arquivo.close()