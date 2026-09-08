# Avanish Garg

**Applied AI Engineer** · IST (UTC+5:30) · Open to remote roles

[LinkedIn](https://www.linkedin.com/in/avanish-garg-90562b255/) · [Email](mailto:gargavanish@gmail.com) · [GitHub](https://github.com/avanish-garg) · [X](https://x.com/GARGAVANISH)

---

## Summary

AI Engineer with 3+ years building and deploying production AI/ML systems — LLM fine-tuning, RAG,
agentic pipelines, and model evaluation. Track record optimizing model quality, latency, and
inference cost at scale, backed by open-source contributions to major AI/ML repositories. Focused
on turning research techniques into reliable, reusable AI infrastructure.

## Core Skills

- **AI/ML:** LLMs, Transformers, RAG, Fine-Tuning, LoRA, Quantization, Embeddings, NLP, Computer Vision, VLMs, Prompt Engineering, AI Agents
- **Languages:** Python, TypeScript, Go
- **Cloud & DevOps:** AWS, Kubernetes, Docker, Terraform, GitHub Actions, Linux
- **Frameworks & Tools:** PostgreSQL, SQLAlchemy, Redis, Git

## Experience

**Applied AI Engineer, Syvora** — Jan 2024 – Present
- Developed document-processing workflows combining OCR, VLM inference, validation, and structured extraction, reducing manual processing time by 80%.
- Built AI services integrating LLMs, RAG, PostgreSQL, Redis, and REST APIs, handling 100K+ requests/day across production workflows.
- Implemented model routing, caching, batching, and provider fallbacks, reducing AI infrastructure costs by 61% while maintaining 95%+ task success.
- Deployed AI workloads on Kubernetes, implementing GPU scheduling, autoscaling, health checks, rolling deployments, and model version management.

**GenAI Engineer, Syvora** — Jul 2023 – Jan 2024
- Optimized Transformer architectures across attention, model size, objectives, and data composition, improving F1 by 12% and reducing inference latency by 31%.
- Architected hybrid RAG pipelines combining dense retrieval, BM25, metadata filtering, query expansion, and reranking, improving Recall@10 from 60% to 85%.
- Built LoRA + quantization fine-tuning pipelines for 7B–13B LLMs, reducing trainable parameters by 99%+ while improving domain-task performance by 12%.
- Implemented defense-in-depth for LLM applications using prompt-injection detection, retrieval isolation, tool authorization, output validation, and policy checks.

## Open Source Contributions

- **Apache Airflow** — extended the listener architecture with two new hooks (DAG pause-state changes, task-instance retry events) across the REST API, CLI, and task-execution paths, with tests and documentation. [PR #72378](https://github.com/apache/airflow/pull/72378) · [PR #72424](https://github.com/apache/airflow/pull/72424)
- **etcd** — added a `--from-key` flag to `etcdctl watch` (parity with `get`/`del`) and `ResumeMutex` to the `concurrency` package (parity with the existing `ResumeElection`), each verified with integration/e2e tests against a live cluster. [PR #22383](https://github.com/etcd-io/etcd/pull/22383) · [PR #22384](https://github.com/etcd-io/etcd/pull/22384)
- **Lago** — implemented lifecycle webhooks for the `Coupon` and `AddOn` resources (parity with `Plan`/`BillableMetric`), with full RSpec coverage. [PR #6306](https://github.com/getlago/lago-api/pull/6306) · [PR #6308](https://github.com/getlago/lago-api/pull/6308)

## Recent Pull Requests

_Auto-updated by a scheduled GitHub Action — see [workflow](./.github/workflows/update-readme.yml)._

<!-- ACTIVITY:START -->
- **[getlago/lago-api]** [feat(add_ons): add lifecycle webhooks](https://github.com/getlago/lago-api/pull/6308) &mdash; _open_
- **[getlago/lago-api]** [feat(coupons): add lifecycle webhooks](https://github.com/getlago/lago-api/pull/6306) &mdash; _open_
- **[etcd-io/etcd]** [client/v3: add ResumeMutex to concurrency package](https://github.com/etcd-io/etcd/pull/22384) &mdash; _open_
- **[etcd-io/etcd]** [etcdctl: add --from-key to watch command](https://github.com/etcd-io/etcd/pull/22383) &mdash; _open_
- **[apache/airflow]** [Add on_task_instance_up_for_retry listener hook](https://github.com/apache/airflow/pull/72424) &mdash; _open_
- **[apache/airflow]** [Add on_dag_pause_status_change listener hook](https://github.com/apache/airflow/pull/72378) &mdash; _open_

_Last updated 2026-09-08 10:28 UTC._
<!-- ACTIVITY:END -->

## Writing

**[The Curious Crunch](https://avanish-garg.hashnode.dev)** — an ongoing technical blog series reverse-engineering the system infrastructure behind Web3, AI, and DevOps.

## Education

Acropolis Institute of Technology & Research — B.Tech, Computer Science
