# API Previsão do tempo

Olá este é meu primeiro projeto API!  
Este é um projeto de API básico para realizar buscas de dados meteorológicos por cidades. Ele consiste em duas páginas principais: uma página de formulário onde os usuários podem inserir o nome da cidade que desejam buscar e uma página de resultados onde são exibidos os dados da busca.

### Tecnologias usadas:
- Linguagem de programação: Python 
- FrameWork Web: Flask 
- API de Clima : OpenWeatherMap  
### Primeira página
Na primeira página que entramos, há um form com um campo de input onde você insere o nome da cidade que você deseja buscar os dados meteorológicos.
 ![formulario principal](/images/form.png)
Caso o nome inserido não exista, é retornada uma mensagem para inserir uma palavra válida.

 ![mensagem de erro](/images/form_error.png)

E por Fim a API retorna os valores com dados meteorologicas e algumas informaçōes adicionais como: Coordenadas, País e hora do nascer e pôr do sol.
 ![pagáina de resultado](/images/resultado.png)
