# Production Architecture

This document describes the recommended pattern for deploying the Horizon Shield as an inline, low-latency asynchronous security proxy protecting your Core Large Language Models (e.g., local Phi-3, external APIs).

```text
                        [ Inbound User Prompt ]
                                   │
                                   ▼
                   ┌───────────────────────────────┐
                   │   API Gateway (FastAPI / TLS) │
                   └───────────────┬───────────────┘
                                   │
                                   ▼
                   ┌───────────────────────────────┐
                   │    PII Cloaking Device Layer  │
                   └───────────────┬───────────────┘
                                   │
                                   ▼
                   ┌───────────────────────────────┐
                   │    Horizon Shield Checkers    │
                   │ (Mass, Trajectory, Anomaly)  │
                   └───────────────┬───────────────┘
                                   │
                  ┌────────────────┴────────────────┐
        [Threat Detected]                  [Threat Clean]
                  │                                 │
                  ▼                                 ▼
   ┌─────────────────────────────┐   ┌─────────────────────────────┐
   │ Deception Protocol          │   │ Local LLM Processing        │
   │ (Fake Honey-tokens Issued)   │   │ (Phi-3 Engine / Inference)  │
   └──────────────┬──────────────┘   └──────────────┬──────────────┘
                  │                                 │
                  └────────────────┬────────────────┘
                                   │
                                   ▼
                   ┌───────────────────────────────┐
                   │     PII Decloaking Layer      │
                   └───────────────┬───────────────┘
                                   │
                                   ▼
                       [ Outbound Secure Output ]
```

### Core Components

* **Edge Reverse Proxy**: Handles high-concurrency requests, TLS termination, and basic rate limiting using FastAPI.
* **Synchronous Interceptors**: The PII Cloaking Engine runs immediately on the string stream before semantic checking to prevent leakage to backend logging infrastructure.
* **Shield Trajectory Module**: Prompts are dynamically scored against local astrophysical heuristics.
* **Conditional Routing Isolation**:
  * **Clean Traffic**: Forwarded directly to the local Phi-3 inference runner.
  * **Adversarial Traffic**: Redirected instantly to the Deception Module, short-circuiting expensive model compute times and wasting attacker resources.
