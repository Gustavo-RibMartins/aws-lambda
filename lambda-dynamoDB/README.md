# ![](https://pics.freeicons.io/uploads/icons/png/9820297401540553608-48.png "DynamoDB") DynamoDB ![](https://pics.freeicons.io/uploads/icons/png/12785093741551942290-48.png "Python")

> As funções a seguir são exemplos de códigos lambda que realizam operações simples em tabelas do DynamoDB.

Para o estudo, utilizei a tabela **produto** que tem a seguinte estrutura:

```js
produto {
    “id_produto”: [partition key] int,
    “nome_produto”: string,
    “categoria”: [global secondary index] string,
    “valor”: int
}
```

#### Operações CRUD (Create-Read-Update-Delete)

- **[createItemDynamoDB.py](https://github.com/Gustavo-RibMartins/aws-lambda/blob/main/lambda-dynamoDB/createItemDynamoDB.py "Create Item"):** recebe um Item como evento (JSON) e faz a inserção desse Item em uma tabela;

- **[deleteItemDynamoDB.py](https://github.com/Gustavo-RibMartins/aws-lambda/blob/main/lambda-dynamoDB/deleteItemDynamoDB.py "Delete Item"):** deleta um Item em uma tabela com uma Partition Key específica;

- **[updateItemDynamoDB.py](https://github.com/Gustavo-RibMartins/aws-lambda/blob/main/lambda-dynamoDB/updateItemDynamoDB.py "Update Item"):** recebe uma Partition Key como evento de entrada (JSON) e atualiza um atributo específico desse campo;

- **readItemDynamoDB.py:** em desenvolvimento...