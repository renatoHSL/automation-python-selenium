from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configurar opções do Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Executa sem abrir o navegador (opcional)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Evita detecção de bot
chrome_options.add_argument("start-maximized")  # Maximiza a tela para parecer humano
chrome_options.add_argument("disable-infobars")  # Remove notificações do Chrome
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas em ambientes Linux
chrome_options.add_argument("--no-sandbox")  # Ignora restrições do sandbox
chrome_options.add_argument("--disable-gpu")  # Desativa renderização GPU

# Alterando o User-Agent para um navegador real
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

# Inicializando o WebDriver com WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa o site do Indeed
driver.get("https://quotes.toscrape.com//")







# Exibe o código fonte da página (para verificar se o bloqueio foi contornado)
# print(driver.page_source)

driver.quit()

