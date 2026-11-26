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
| [roboflow/supervision](https://github.com/roboflow/supervision/pulls?q=is%3Apr+author%3Aavanish-garg) | 8 | 0 | Mask-hole dataset export, CompactMask.resize parity, CSV export of array data |
| [temporalio/ai-integrations](https://github.com/temporalio/ai-integrations/pulls?q=is%3Apr+author%3Aavanish-garg) | 8 | 0 | OpenAI Agents plugin: tool metadata, tool argument errors, RunState resume; Gemini permanent-error handling |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio/pulls?q=is%3Apr+author%3Aavanish-garg) | 3 | 0 | Anthropic prompt caching and OpenAI Agents strict mode (Python), cache-breakpoint fix (TypeScript) |
| [lancedb/lancedb](https://github.com/lancedb/lancedb/pulls?q=is%3Apr+author%3Aavanish-garg) | 3 | 0 | Embedding retry/backoff on permanent errors, optimize() keeping tagged versions |
| [temporalio/sdk-python](https://github.com/temporalio/sdk-python/pulls?q=is%3Apr+author%3Aavanish-garg) | 3 | 0 | Workflow update validator checks, Annotated parameter hints |
| [docling-project/docling](https://github.com/docling-project/docling/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 2 | Office backends: DOCX/ODF footnotes, PPTX formatting and hyperlinks |
| [mlflow/mlflow](https://github.com/mlflow/mlflow/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 2 | Experiment and run restore, prompt search ordering, GCS/Azure presigned URLs |
| [truera/trulens](https://github.com/truera/trulens/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 1 | Bedrock and LangChain provider fixes, Cursor token usage |
| [collabora/WhisperLive](https://github.com/collabora/WhisperLive/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 0 | OpenVINO backend: prompts, hotwords, diarization |
| [getlago/lago-api](https://github.com/getlago/lago-api/pulls?q=is%3Apr+author%3Aavanish-garg) | 2 | 0 | Coupon and add-on lifecycle webhooks |
| [apache/airflow](https://github.com/apache/airflow/pulls?q=is%3Apr+author%3Aavanish-garg) | 1 | 1 | Listener hooks for task retries and DAG pause state |
| [celery/celery](https://github.com/celery/celery/pulls?q=is%3Apr+author%3Aavanish-garg) | 1 | 1 | Chord errbacks given as a single signature |
| [qdrant/qdrant](https://github.com/qdrant/qdrant/pulls?q=is%3Apr+author%3Aavanish-garg) | 1 | 1 | gRPC metrics whitelist, public gRPC Quotas service |
| [weaviate/weaviate](https://github.com/weaviate/weaviate/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 4 | Backup API, tenant filtering, reranker config |
| [etcd-io/etcd](https://github.com/etcd-io/etcd/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | etcdctl watch --from-key, concurrency.ResumeMutex |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo/pulls?q=is%3Apr+author%3Aavanish-garg) | 0 | 2 | exec: provider argument quoting, unquoted YAML dates in config and test files |
<!-- REPOS:END -->

## Recent Pull Requests

_Auto-updated by a scheduled GitHub Action — see [workflow](./.github/workflows/update-readme.yml)._

<!-- ACTIVITY:START -->
- **[qdrant/qdrant]** [fix: sync GRPC_ENDPOINT_WHITELIST with its REST metrics sibling](https://github.com/qdrant/qdrant/pull/10968) &mdash; _merged_
- **[celery/celery]** [index tasks by the worker and type known at event time](https://github.com/celery/celery/pull/10988) &mdash; _merged_
- **[roboflow/supervision]** [fix(detection): anchor empty masks at box center for `CENTER_OF_MASS`](https://github.com/roboflow/supervision/pull/2976) &mdash; _merged_
- **[roboflow/supervision]** [fix(key_points): validate data length in `KeyPoints.__setitem__`](https://github.com/roboflow/supervision/pull/2974) &mdash; _merged_
- **[roboflow/supervision]** [fix(detection): stop NMM from merging detections that do not overlap at threshold 0](https://github.com/roboflow/supervision/pull/2972) &mdash; _merged_
- **[roboflow/supervision]** [fix(dataset): keep the train item that float rounding drops in split](https://github.com/roboflow/supervision/pull/2969) &mdash; _merged_

_Last updated 2026-11-26 16:15 UTC._
<!-- ACTIVITY:END -->

## Writing

**[The Curious Crunch](https://avanish-garg.hashnode.dev)** — an ongoing technical blog series reverse-engineering the system infrastructure behind Web3, AI, and DevOps.

## Education

Acropolis Institute of Technology & Research — B.Tech, Computer Science
