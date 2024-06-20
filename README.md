# Dsafio Grupo Casas Bahia

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

> Projeto tem como objetivo exemplificar a produtizacao de um modelo para desafio


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `<Python / 3.9 / requeridos>`
- Você tem uma máquina `<Windows / Linux / Mac>`. Indique qual sistema operacional é compatível / não compatível.
- Você instalou a versão mais recente de `<Docker / 24.0 / ou superior>`

## 🚀 Instalando <nome_do_projeto>

Para Utilizar siga estas etapas:

Clone o repositorio Linux e macOS:

```
 [cl](https://github.com/Blakinston/desafio.git)
```

Execute Docker estando dentro da pasta app:

```
  docker build -t nome_container .  
```
Execute a imagem para o servidor poder ser utilizado:
```
  docker run -d -p 7070:7070 nome_container  
```

## ☕ Previsoes  

As previsões podem ser feitas via curl ou python 

```
  curl -X POST "http://localhost:7070/predict" -H "Content-Type: application/json" -d "{\"fixed_acidity\":7.4,\"volatile_acidity\":0.7,\"citric_acid\":0,\"residual_sugar\":1.9,\"chlorides\":0.076,\"free_sulfur_dioxide\":11,\"total_sulfur_dioxide\":34,\"density\":0.9978,\"sulphates\":0.56,\"alcohol\":3.56,\"ph_acid\":5.4,\"ph_basic\":1}"
```


## 😄 Seja um dos contribuidores

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
