#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.
# 
# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[56]:


import pyautogui
import time

#pyautogui.click # clocar com o mousemeu_login
#pyautogui.write # escrever um texto
#pyautogui.press # apertar uma tecla
#pyautogui.hotkey # apertat uma combinação de teclas (Ctrl + D)

# O comando pause ele espera em todos os comandos
pyautogui.PAUSE = 2


# passo 1: Entrar no sistemas da empresa (usanso link)
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

# sleep 3 segundos de espera no local correto
time.sleep(3)


# Passo 2: Fazer login

#clicar no espaço de login
pyautogui.click(x=-1462, y=575)

#escrever o login
pyautogui.write("meu_login")


# Senha
pyautogui.click(x=-1363, y=691)
pyautogui.write("minha_senha")

# Clicar em Acessar
pyautogui.click(x=-1459, y=802)
time.sleep(3)

# Exportar a base de dados
pyautogui.click(x=-2208, y=643) # Arquivo compras
pyautogui.click(x=-303, y=319) # 3 pontinhos
pyautogui.click(x=-613, y=926) # Fazer Download

time.sleep(3)


# In[57]:


# Comando para tirar print da tela e pegar a posição
#time.sleep(5)
#print(pyautogui.position())


# In[58]:


# Passo 4: Calcular os indicadores 
import pandas as pd
tabela = pd.read_csv(r"Compras.csv",sep=";")
display(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)


# In[59]:


# Passo 5: Enviar um e-mail para o meu chefe


# In[62]:


import pyperclip
# Entrar no e-mail: https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.press("enter")
time.sleep(3)

# Clicar botão escrever
pyautogui.click(x=-2766, y=317)

#destinario
pyautogui.write("dataanalyticsaironys@gmail.com")
pyautogui.press("tab")

pyautogui.write("aironysgarrido1@gmail.com")
pyautogui.press("tab")

pyautogui.press("tab") # pulando para o Assunto

# Assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pulando para mensagem

texto = f"""
            Prezados...
            Segue o relatório de compras deste mês.
            
            Total Gasto: R${total_gasto:,.2f}
            Quantidade de Produtos: {quantidade:}
            Preço Médio: R${preco_medio:,.2f}
            
            Qualquer dúvida estou à disposição.
            Obrigado!
               
            Att: Aironys Garrido
            
        """

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar
pyautogui.hotkey ("ctrl","enter")


# In[61]:


# Comando para tirar print da tela e pegar a posição
#time.sleep(5)
#print(pyautogui.position())

