-- Quantidade de clientes por email marketing
DROP TABLE IF EXISTS public_raw.raw_cliente_email_marketing;

CREATE TABLE public_raw.raw_cliente_email_marketing AS
WITH
    cliente_email_marketing AS (
        SELECT
            em.descricao_email_marketing AS email_marketing,
            COUNT(DISTINCT c.id_cliente) AS quantidade_clientes
        FROM public_data.tb_cliente c
        JOIN public_data.tb_email_marketing em
            ON em.id_email_marketing = c.id_email_marketing
        GROUP BY em.descricao_email_marketing
        ORDER BY quantidade_clientes DESC
    )
SELECT
    email_marketing,
    quantidade_clientes,
    ROUND((quantidade_clientes * 100.0 / nullif(
        (SELECT SUM(quantidade_clientes)
        FROM cliente_email_marketing), 0)), 2) AS percentual_clientes
FROM cliente_email_marketing
ORDER BY quantidade_clientes DESC
