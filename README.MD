# Desenvolvimento Web IV

## Aula 1 
  - 05/08/2025
  - Aplicações voltadas a Microserviços (Web IV)
  - Aplicações Monolíticas (WEB II e III)

### Serialização de dados

JSON (Javascript Object Notation)

Pessoa

- classe
  ```python
  class Pessoa:
    id
    nome
    peso
    altura
  ```
- JSON
  ```js
  {
    "id": 101,
    "nome": "Maria",
    "peso": 75.3,
    "altura": null,
    "filhos": ["JOão", "RObeta", "Luciana"],
    "endereco": {
      "id": 10010,
      "cep": "88482-900",
      "logradouro": "Av. Brasil",
      "numero": 444,
      "municipio": "Foz do Iguaçu"
    }
  }
  ```
```js
  [
    {
      "q":"Among the things you can give and still keep are your word, a smile, and a grateful heart.",
      "a":"Zig Ziglar",
      "h":"<blockquote>&ldquo;Among the things you can give and still keep are your word, a smile, and a grateful heart.&rdquo; &mdash; <footer>Zig Ziglar</footer></blockquote>"}
  ]
```


## Aula 02

- URL: https://zenquotes.io/api/today
- Domínio: zenquotes.io
- Endpoint: /api
- Resource: /today


