# Architecture Decision Record (ADR): GraphRAG for Complex Operational Data

## Context and Problem Statement
Standard Vector databases (Vector RAG) utilize semantic similarity, which is highly effective for basic document retrieval but fails at complex relational mapping. 

**Business Use Case:** Managing operational and financial data across a multi-unit real estate portfolio (e.g., Stepping Stone LLC). 
If an executive asks the AI: *"What is the total maintenance ROI impact of the Tupelo model property in the Franklin 37064 zip code over the last fiscal year?"*, standard Vector RAG fails. It cannot explicitly connect the tenant's maintenance request, the specific "Tupelo" floor plan entity, the Franklin property tax records, and the LLC's annual financial report.

## The GraphRAG Solution
To solve this, we implement a Knowledge Graph (GraphRAG) architecture. 

### Implementation Strategy
Instead of merely chunking text into vector embeddings, the ingestion pipeline utilizes Python to extract specific entities and create relational edges:
*   `Entity A:` Stepping Stone LLC
*   `Entity B:` Franklin 37064 Property
*   `Entity C:` Tupelo Floor Plan
*   `Entity D:` HVAC Maintenance Ledger

### Outcome
GraphRAG traverses the semantic network, understanding that the maintenance ledger belongs to the Tupelo unit, which is an asset of the LLC. This enables the LLM to generate precise, financially accurate answers for complex business operations, shifting the AI from a simple "search engine" to an operational intelligence tool.
