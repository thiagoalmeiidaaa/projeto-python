# Apache Iceberg

Este módulo demonstra como realizar operações básicas em uma tabela Apache Iceberg no Apache Spark.

## Comandos

```sql
-- INSERT
INSERT INTO default.produtos VALUES (4, 'Teclado', 120.0)

-- UPDATE
UPDATE default.produtos SET valor = 135.0 WHERE id = 4

-- DELETE
DELETE FROM default.produtos WHERE id = 4
```
