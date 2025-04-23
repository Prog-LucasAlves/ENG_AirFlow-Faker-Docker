-- Clientes ativos nos últimos 12 meses
DROP TABLE IF EXISTS public_raw.raw_cliente_ativo;

CREATE TABLE public_raw.raw_cliente_ativo AS
WITH
    cliente_ativo AS (
        SELECT
            p.id_cliente,
            COUNT(p.id_pedido) AS quantidade_pedidos,
            c.primeiro_nome,
            c.sobrenome,
            c.email,
        FROM public_raw.raw_pedido AS p
        LEFT JOIN public_raw.raw_cliente AS c
            ON p.id_cliente = c.id_cliente
        WHERE p.data_pedido >= DATEADD(month, -12, CURRENT_DATE)
        GROUP BY p.id_cliente, c.primeiro_nome, c.sobrenome, c.email
    )
SELECT
    *
FROM cliente_ativo
