# Delta Lake

Este módulo demonstra como realizar operações básicas em uma tabela Delta Lake no Apache Spark.

## Comandos

```python
# INSERT
INSERT INTO delta.`../data/delta_vendas` VALUES (3, 'Carlos', 200, '2025-04-25')

# UPDATE
deltaTable.updateExpr("cliente = 'Carlos'", {"valor": "250"})

# DELETE
deltaTable.delete("cliente = 'Carlos'")
```
