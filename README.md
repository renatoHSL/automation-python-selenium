# 🔍 Web Scraping de Vagas - Indeed

## 📌 Sobre o Projeto
Este é um projeto de **Web Scraping** que coleta dados de vagas de emprego do site **Indeed** usando a biblioteca **SeleniumBase**. O objetivo é extrair e organizar informações sobre oportunidades de emprego de forma automatizada, possibilitando a análise e filtragem de vagas de interesse.

## 🚀 Funcionalidades
- Busca automatizada de vagas no **Indeed**
- Extração de:
  - ✅ Título da vaga
  - ✅ Nome da empresa
  - ✅ Localização
  - ✅ Descrição breve
- Salvamento dos dados coletados em um arquivo **CSV**
- Tratamento de **Captcha** para evitar bloqueios
- **Delays aleatórios** para simular comportamento humano e reduzir riscos de bloqueio

## 🛠️ Tecnologias Utilizadas
- **Python** 🐍
- **SeleniumBase** para automação de navegação 🖥️
- **Pandas** para manipulação de dados 📊
- **JSON** para estruturação das informações extraídas

## 📥 Como Usar
### 1️⃣ Instale as dependências:
```sh
pip install seleniumbase pandas
```
### 2️⃣ Execute o script:
```sh
python scraping.py
```
### 3️⃣ Veja os resultados no arquivo `out.csv` gerado após a execução.

## 🔎 Personalização
Caso queira buscar outras vagas, edite as variáveis no código:
```python
posicao = "Desenvolvedor Junior"
local = "São Paulo"
```

## 📌 Observações
- O Indeed pode bloquear o scraper caso detecte tráfego automatizado excessivo.
- Futuramente, este projeto poderá ser otimizado para utilizar **APIs do Indeed**, reduzindo a necessidade de scraping via Selenium.

## 🤝 Contribuições
Sinta-se à vontade para abrir **issues** ou enviar um **pull request** caso tenha sugestões de melhorias!

---
📢 **Se esse projeto te ajudou ou você gostou, não esqueça de deixar uma ⭐ no repositório!** 🚀

