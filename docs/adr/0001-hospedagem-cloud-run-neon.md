# ADR-0001: Hospedagem em Cloud Run + Neon

Status: aceita (2026-11-23)

## Contexto

Duas pessoas usam o app, no celular. O tráfego é mínimo e o custo precisa ficar perto de zero. Ninguém quer cuidar de servidor.

## Decisão

- App: um container no Google Cloud Run (cota gratuita, escala a zero).
- Banco: Postgres gerenciado no Neon (plano gratuito, 0,5 GB). O Neon suporta `pg_trgm` e `unaccent`, que a busca e a normalização usam.
- Segredos (chave da IA, `SESSION_SECRET`, `DATABASE_URL`) no Secret Manager ou nas variáveis do serviço, nunca no repositório.
- Alerta de orçamento de US$ 1 no Google Cloud antes do primeiro deploy.

## Consequências

- Partida a frio de 1 a 2 s depois de ocioso. Aceitável para uso pessoal.
- O Neon também suspende o compute quando ocioso: a primeira consulta pode demorar e conexões antigas caem, por isso `pool_pre_ping`.
- O health check (`/healthz`) não toca no banco, para o Cloud Run não reiniciar o container por falha do banco.
- Migrações rodam como passo do deploy (job ou CI), não na subida do container: duas instâncias subindo juntas não devem migrar ao mesmo tempo. Use a conexão direta do Neon (sem `-pooler`) para migrar.
- Exige cartão no Google Cloud. Conferir preços e cotas no dia de criar as contas.
- Saída: o app é um container + Postgres, então migrar para uma VPS com Docker Compose custa pouco.

## Alternativa descartada

VPS (Hetzner) com Compose: sem partida a frio, mas backup, atualização e certificado ficam por conta do Gabriel.
