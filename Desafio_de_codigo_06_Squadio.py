def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
  for m in senha:
    if m.isupper():
        tem_letra_maiuscula = True
    if m.islower():
        tem_letra_minuscula = True
  if tem_letra_maiuscula == False:
     return 'Sua senha nao atende aos requisitos de seguranca.'
  if tem_letra_minuscula == False:
     return 'Sua senha nao atende aos requisitos de seguranca.'
  
  
  
  

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  # TODO: Verificar o comprimento mínimo e critérios de validação

  for m in senha:
    if m.isdigit():
       tem_numero = True
  if tem_numero == False:
     return 'Sua senha nao atende aos requisitos de seguranca.'
  
  for m in senha:
     if not m.isalnum():
        tem_caractere_especial = True
  if tem_caractere_especial == False:
     return 'Sua senha nao atende aos requisitos de seguranca.' 

  return 'Sua senha atende aos requisitos de seguranca. Parabens!'    



# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)