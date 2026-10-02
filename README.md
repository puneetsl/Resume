# Puneet Ludu — Resume

[![Latest](https://img.shields.io/badge/Latest-v11.4-3C2D41?style=flat-square)](puneet_ludu_resume_latest.pdf) [![Download PDF](https://img.shields.io/badge/Download-PDF-005FAF?style=flat-square&logo=adobeacrobatreader&logoColor=white)](puneet_ludu_resume_latest.pdf) [![All versions](https://img.shields.io/badge/All_versions-folder-lightgrey?style=flat-square)](versions/)

---

=3em

**Puneet Ludu**  
**ML Engineer & Tech Lead**  
Production ML · Applied AI + Agentic · 13+ years  
puneet [dot] ludu [at] gmail [dot] com · New York, NY · +1-(716) eight six seven four three four four · [puneet.io](https://puneet.io)

[github.com/puneetsl](https://github.com/puneetsl)  
[linkedin.com/in/puneetsl](https://www.linkedin.com/in/puneetsl)  
[kaggle.com/puneetsl](https://www.kaggle.com/puneetsl)  
[Google Scholar](https://scholar.google.com/citations?user=NrYKcaMAAAAJ&hl=en)  
No sponsorship required (LPR)

**Next-Gen Zestimate: Explainable Valuation** (PyTorch, Databricks)

Led architecture experiments and production evaluation for Zillow’s first explainable Zestimate model; improved accuracy through learned comp weighting and evaluated explanation stability nationally.

**Impact:** Per-feature dollar explanations built into the valuation model.

**Property Condition & Quality Image Embeddings** (PyTorch, Databricks, CLIP)

Led research and model refinement for CLIP-based property condition and quality scoring on 1.95M homes, achieving **${\sim}$70% five-class accuracy and ${\sim}$0.91 weighted AUC**.

**Impact:** Production scoring pipeline; scored 16.5M home–listing pairs.

**Zestimate Customer Care Agent** (LangChain, FastAPI)

Built one of Zillow’s first agentic AI tools for customer care, with RAG and real-time services exposing property history, features, and comps across ${\sim}$150M homes.

Encoded expert triage as agent tools; reduced hallucinations with custom judges, curated context, and bounded responses.

Answered ${\sim}$50–60% of evaluated questions; piloted with customer care representatives.

**[Listing IQ: Interactive CMA Platform](https://grow.zillow.com/listingIQ-comparative-market-analysis)** (Django, DocumentDB, H3 Geospatial)

Led two engineers and an intern from CMA prototype through handoff to ShowingTime; owned ML architecture, incorporated seller-agent feedback, and productionized real-time services.

Moved comp selection from batch to real time using geospatial retrieval and ranking. Property edits update comps and valuations immediately; full reports in under 15 seconds.

**Impact:** Shipped as Listing IQ CMA, bringing Zestimate valuation data into a commercial seller-agent product.

**Active Listing Comps Engine** (Databricks, PySpark, H3 Geospatial)

Architected the daily similarity-ranking pipeline for 3M+ active listings behind Showcase’s Listing Performance Dashboard.

Built listing deduplication and lifecycle tracking to maintain accurate comp sets.

Led a data source migration that expanded listing coverage from **90% to 98.5%**.

**Impact:95% reduction in listing-visibility complaints**.

**Infrastructure & Engineering Leadership** (FastAPI, AWS, Terraform, Databricks, PySpark)

Built a FastAPI reverse-proxy gateway decoupling downstream applications from model changes; designed for 20–40M req/day, with A/B testing support and a 99.5% SLA.

Led legacy valuation retirement and Redis-to-feature-store migration; discovered two undocumented downstream consumers, rolled back, and revised the rollout.

Led training ETL migration from Metaflow/Kubernetes to Databricks PySpark. Platform-specific optimization reversed an initial 8× latency and 10× cost regression, restoring production parity.

**Impact:$350K annual savings** from retiring the legacy valuation stack.

**Mentorship & Technical Leadership**

Managed an intern and mentored 4+ engineers; authored RFCs and architecture guidance adopted outside the team.

**Discount Optimization** (Python, Keras, TensorFlow, Weights & Biases)

Owned subscription discount optimization from privacy-constrained feature engineering through A/B testing and production.

Built a 100-model ensemble to reduce epistemic uncertainty and stabilize discount recommendations across retraining.

**Impact:6% revenue increase** vs. baseline in A/B testing.

**ML-Powered Financial Data Extraction** (Python, TensorFlow, Keras, SageMaker)

Led development of a speaker identification system for earnings calls using spectrogram-based CNNs.

Built private company fact extraction pipeline across 1.6M websites using ELMo/BiLSTM; rewrote the language identification service.

Led financial machine-translation infrastructure; achieved 69.1 BLEU for Polish.

**Impact:**% less annotation time in an initial production rollout. 

**Financial Document Search & Ranking Systems** (Apache Spark, Java, Python)

Led team of 3 engineers on Document Screening: built autosuggestion and concept similarity systems.

Built a document deduplication service, reducing response latency 10×.

Architected Formula Lookup using distributed trie and n-gram language models on Spark.

**Impact:** Formula ranking improved from 5.6 to 2.3; document processing was 66% faster. Systems supported StreetAccount trending news.

**Event Detection in Time Series** (Java, Python, RapidMiner) 

Wrote a Shape Context-based algorithm for detecting recurring patterns in time series; matched SAX/DTW accuracy on general benchmarks and outperformed by 7% in the car sensor domain.

**[Data Harmonization Framework (DHF)](https://ieeexplore.ieee.org/abstract/document/6597127)** (Java, Apache Pig)

Built a MapReduce ETL framework that combines enterprise data from multiple sources in near real time. Published at IEEE INDIN 2013.

|                           |                                                                                                            |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------|
| **Languages**             | **Python** · SQL · Java · C/C++ · Bash                                             |
| **Modeling & Evaluation** | **PyTorch** · TensorFlow · A/B Testing · Uncertainty Estimation                          |
| **LLM & GenAI**           | RAG · LangChain · LLM Guardrails · Embeddings · CLIP · Vector DBs (Pinecone) |
| **Data & ML Pipelines**   | **PySpark** · **Databricks** · MLflow · Metaflow · Weights & Biases                |
| **Backend & Deployment**  | **FastAPI** · Django · Docker · Kubernetes · Terraform                             |
| **Cloud & CI/CD**         | AWS (S3, EC2, SageMaker) · GitLab CI                                                                 |

**Master of Science** in Computer Science, State University of New York, Buffalo, NY  
**B. Tech.** in Computer Science and Engineering, JIIT, India

**[Inferring Latent Attributes of an Indian Twitter user using Celebrities and Class Influencers](http://dl.acm.org/citation.cfm?id=2806657)**  ACM Hypertext 2015  
**[Inferring gender of a Twitter user using celebrities it follows](http://arxiv.org/abs/1405.6667)** CORR 2014  
**[Architecture for Automated Tagging and Clustering of Song Files According to Mood](http://arxiv.org/abs/1206.2484)** IJCSI, 2010

|                                                                                                                |                                                                                                                                |
|:---------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| **[Organizer @ MUFin](https://sites.google.com/view/w-mufin/organizers)**                                     | Program committee and paper reviewer, Modeling Uncertainty in the Financial Sector *(AAAI 2023, ECML-PKDD 2022)*               |
| **[Lotion](https://github.com/puneetsl/lotion)**                                                              | Unofficial Notion.so Desktop app for Linux *(2K+ GitHub stars / 60K+ Clones & Downloads)*                                      |
| **[Romadeva](https://github.com/puneetsl/Romadeva)**                                                          | Roman-to-Devanagari transliteration *(Used by [Translators Without Borders](https://translatorswithoutborders.org))*           |
| **[Quena](https://www.facebook.com/photo.php?fbid=10153613108040010&set=a.10153613186550010&type=3&theater)** | Question-answering over 1.6M Wikipedia documents; query parsing and popularity-based ranking. *(Apache Solr, NER, POS tagger)* |

---

## Build

This resume is authored in LaTeX (`resume.tex`). Every push triggers [a GitHub Action](.github/workflows/compile-resume.yml) that:

1. Compiles the PDF with TeX Live 2026
2. Auto-bumps the version (`MAJOR.MINOR` rolls major every 10 minor)
3. Saves a versioned copy in [`versions/`](versions/)
4. Regenerates this README — deterministic Python cleanup of Pandoc artifacts + regex PII obfuscation, with optional [Gemini 2.5 Pro](https://ai.google.dev/) polish if `GEMINI_API_KEY` is set

For local compilation see [RUNSTEPS.md](RUNSTEPS.md).
