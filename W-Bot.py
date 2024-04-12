#importações necessárias para o funcionamento do bot
#selenium - biblioteca que a princípio iremos trabalhar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# indico jack como o webdriver
jack = webdriver.Firefox()

# implicitly_wait é o sleep implícito
jack.implicitly_wait(2)

# chamo navegador com tela 1920x1080px em half_window
jack.set_window_size(1920, 1080)

# chamo navegador com link para a página destino
jack.get("https://mercadolivre.com")

# mando o robô clicar na aba de pesquisa
jack.find_element(By.ID, "cb1-edit").click()

# Mando o robô escrever na barra de pesquisa
jack.find_element(By.ID, "cb1-edit").send_keys("Fone de Ouvido Bluetooth")

#teste de alerta
#jack.find_element(By.LINK_TEXT, "See a sample confirm").click()
#NÃO FUNCIONOU, MAS VAI FICAR AQUI PRA PENSAR EM UMA SOLUÇÃO MELHOR NO FUTURO
#clicar no botão de pesquisar

jack.find_element(By.CLASS_NAME, "nav-search-btn").click()

#A PARTIR DAQUI SÓ BAIXARIA

#jack.find_element(By.)

sleep(10)
jack.quit()

#Agora que o programa já abre a janela do mercado livre, já faz uma pesquisa, mesmo que simples, vamos começar a buscar soluções para rodar essa carroça na nuvem.

#izi (https://cloud.seenode.com/Wagon-Bot)

