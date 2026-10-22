# Avanish Garg

**Applied AI Engineer** · IST (UTC+5:30) · Open to remote roles

[LinkedIn](https://www.linkedin.com/in/avanish-garg-90562b255/) · [Email](mailto:gargavanish@gmail.com) · [X](https://x.com/GARGAVANISH)

---

## Summary

AI Engineer with 2+ years building and deploying production AI/ML systems — LLM fine-tuning, RAG,
agentic pipelines, and model evaluation. Track record optimizing model quality, latency, and
inference cost at scale, backed by open-source contributions to major AI/ML repositories. Focused
on turning research techniques into reliable, reusable AI infrastructure.

## Core Skills

- **AI/ML:** LLMs, Transformers, RAG, Fine-Tuning, LoRA, Quantization, Embeddings, NLP, Computer Vision, VLMs, Prompt Engineering, AI Agents
- **Languages:** Python, TypeScript, Go
- **Cloud & DevOps:** AWS, Kubernetes, Docker, Terraform, GitHub Actions, Linux
- **Frameworks & Tools:** PostgreSQL, SQLAlchemy, Redis, Git
- **Web3/Blockchain:** Solidity, Foundry, Hardhat, EIP-712, UUPS Upgradeable Proxies, Gnosis Safe, The Graph, Cross-Chain Messaging (CCTP), Gas Optimization

## Experience

**Applied AI Engineer, Syvora** — July 2025 – Present
- Developed document-processing workflows combining OCR, VLM inference, validation, and structured extraction, reducing manual processing time by 80%.
- Built AI services integrating LLMs, RAG, PostgreSQL, Redis, and REST APIs, handling 100K+ requests/day across production workflows.
- Implemented model routing, caching, batching, and provider fallbacks, reducing AI infrastructure costs by 61% while maintaining 95%+ task success.
- Deployed AI workloads on Kubernetes, implementing GPU scheduling, autoscaling, health checks, rolling deployments, and model version management.

**Protocol Engineer, NDA** — Jun 2024 – May 2025
- Implemented defense-in-depth for LLM applications using prompt-injection detection, retrieval isolation, tool authorization, output validation, and policy checks.
- Architected Polymarket-style prediction exchange contracts with deterministic order matching, invariant-safe execution, and settlement state machines sustaining 10k+ daily on-chain trades in production.
- Authored 300+ Foundry fuzz and invariant tests covering adversarial execution paths including duplicate messages and partial settlement, achieving 97% branch coverage on core protocol contracts.
- Built cross-chain USDC settlement infrastructure processing 500k+ messages with domain-separated replay protection and invariant-safe execution, sustaining zero failed settlements across all integrated chains.

## Open Source Contributions

Pull requests across the AI/ML and infrastructure projects below (merged and currently open; counts update automatically).

<!-- REPOS:START -->
| Repository | Merged | Open | Focus |
| --- | ---: | ---: | --- |
| [temporalio/ai-integrations](https://github.com/temporalio/ai-integrations/pulls?q=is%3Apr+author%3Aavanish-garg) | 3 | 1 | OpenAI Agents plugin: tool metadata, tool argument errors, RunState resume |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio/pulls?q=is%3Apr+author%3Aavanish-garg) | 3 | 0 | Anthropic prompt caching and OpenAI Agents strict mode (Python), cache-breakpoint fix (TypeScript) |
| [roboflow/supervision](https://github.com/roboflow/supervision/pulls?q=is%3Apr+author%3Aavanish-garg) | 3 | 0 | Mask-hole dataset export, CompactMask.resize parity, CSV export of array data |
| [docling-project/docling](https://github.com/docling-project/docling/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 2 | Office backends: DOCX/ODF footnotes, PPTX formatting and hyperlinks |
| [mlflow/mlflow](https://github.com/mlflow/mlflow/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 2 | Experiment and run restore, prompt search ordering, GCS/Azure presigned URLs |
| [truera/trulens](https://github.com/truera/trulens/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 1 | Bedrock and LangChain provider fixes, Cursor token usage |
| [getlago/lago-api](https://github.com/getlago/lago-api/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 0 | Coupon and add-on lifecycle webhooks |
| [collabora/WhisperLive](https://github.com/collabora/WhisperLive/pulls?q=is%3Apr+author%3Aavanish-garg) | 1 | 1 | OpenVINO backend: prompts, hotwords, diarization |
| [weaviate/weaviate](https://github.com/weaviate/weaviate/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 4 | Backup API, tenant filtering, reranker config |
| [apache/airflow](https://github.com/apache/airflow/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | Listener hooks for task retries and DAG pause state |
| [etcd-io/etcd](https://github.com/etcd-io/etcd/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | etcdctl watch --from-key, concurrency.ResumeMutex |
| [lancedb/lancedb](https://github.com/lancedb/lancedb/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | Embedding retry/backoff on permanent errors, optimize() keeping tagged versions |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | exec: provider argument quoting, unquoted YAML dates in config and test files |
| [qdrant/qdrant](https://github.com/qdrant/qdrant/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | gRPC metrics whitelist, public gRPC Quotas service |
<!-- REPOS:END -->

## Recent Pull Requests

_Auto-updated by a scheduled GitHub Action — see [workflow](./.github/workflows/update-readme.yml)._

<!-- ACTIVITY:START -->
- **[temporalio/ai-integrations]** [Return invalid tool arguments to the model instead of failing the workflow](https://github.com/temporalio/ai-integrations/pull/92) &mdash; _merged_
- **[getlago/lago-api]** [feat(coupons): Add lifecycle webhooks](https://github.com/getlago/lago-api/pull/6306) &mdash; _merged_
- **[getlago/lago-api]** [feat(add_ons): Add lifecycle webhooks](https://github.com/getlago/lago-api/pull/6308) &mdash; _merged_
- **[temporalio/ai-integrations]** [Fail fast on permanent HTTP errors from Gemini Interactions, Agents and Files calls](https://github.com/temporalio/ai-integrations/pull/135) &mdash; _open_
- **[promptfoo/promptfoo]** [fix(util): keep unquoted YAML dates when loading config and test files](https://github.com/promptfoo/promptfoo/pull/11776) &mdash; _open_
- **[promptfoo/promptfoo]** [fix(providers): parse quoted exec arguments like a shell](https://github.com/promptfoo/promptfoo/pull/11774) &mdash; _open_

_Last updated 2026-10-22 11:01 UTC._
<!-- ACTIVITY:END -->

## Writing

**[The Curious Crunch](https://avanish-garg.hashnode.dev)** — an ongoing technical blog series reverse-engineering the system infrastructure behind Web3, AI, and DevOps.

## Education

Acropolis Institute of Technology & Research — B.Tech, Computer Science
