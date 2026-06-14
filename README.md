# Puneet Ludu's Resume

##### Latest Version: v11.0 
[![Resume PDF](https://img.shields.io/badge/Resume-PDF-blue.svg)](puneet_ludu_resume_latest.pdf)

## Resume in Markdown

**Puneet Ludu**\
**ML Engineer & Tech Lead**\
Production ML & LLM Reliability $\cdot$ 13+ years\
puneet [dot] ludu [at] gmail [dot] com $\cdot$ New York, NY $\cdot$ +1-(716) eight six seven four three four four
$\cdot$ [puneet.io](https://puneet.io)

 [github.com/puneetsl](https://github.com/puneetsl)\
 [linkedin.com/in/puneetsl](https://www.linkedin.com/in/puneetsl)\
 [kaggle.com/puneetsl](https://www.kaggle.com/puneetsl)\
 [Google
Scholar](https://scholar.google.com/citations?user=NrYKcaMAAAAJ&hl=en)

------------------------------------------------------------------------

to

**Zillow (Zestimate)**, Machine Learning Engineer (Tech Lead), *Sep 2021
-- Present*, Remote\

  **[Listing IQ: Interactive CMA
Platform](https://grow.zillow.com/listingIQ-comparative-market-analysis)**
*(Django, DocumentDB, PyTorch)* \[Real-time Valuations + Embeddings\]

Led **proof-of-concept and core architecture** for platform now live as
Listing IQ CMA: AI-powered tool enabling agents to customize property
comparisons with map-based filtering, editable valuations, and
amenity-level explanations. Designed APIs integrating real-time
Zestimate valuations, property embeddings, and comparative analysis.
Mentored junior engineer through production launch.\
**Impact:** *POC $\rightarrow$ shipped product powering agent pricing
decisions; foundation for new agent revenue products*

  **Zestimate Customer Care Agent + Reliability Infrastructure**
*(React, LangChain, FastAPI)* \[RAG Grounding + Output Validation +
Deflection KPI\]

Designed and shipped the **first LLM assistant deployed to Zillow
customer support**: personalized Zestimate explanations grounded in real
valuation data. Built **RAG pipeline that constrains the agent** to
answer from actual Zestimate features and values rather than free-form
generation; layered **output validation with schema and range checks**
to catch out-of-distribution responses before they reach customers.
Deployed with **deflection rate** tracked as the primary production
KPI.\
**Impact:** *First LLM tool deployed to Zillow customer care;
production-hardened against hallucination via grounding and output
validation*

  **Active Listing Comps Engine** *(Apache Spark, Metaflow, H3
Geospatial)* \[Similarity Scoring + Batch/REST APIs\]

Architected and built similar listings comparison engine from ground up:
batch pipeline and real-time API using **H3 geospatial indexing** and
customizable ranking algorithms. Processes **3M+ listings**, powers
[Zillow Showcase](https://grow.zillow.com/showcase) dashboards (**8M
monthly views**) helping agents demonstrate listing performance vs
non-Showcase homes. Led migration to append-only listing data source;
built lifecycle management and deduplication layer to track active,
sold, and removed listings across markets. **Production in 5 weeks.**
Later led algorithm improvements.\
**Impact:** *5 weeks to production; 95% complaint reduction, coverage
90%$\rightarrow$`<!-- -->`{=html}98.5%; metrics cited in sales,
marketing, and investor communications*

  **Infrastructure & Engineering Leadership** *(Terraform, AWS,
Metaflow, Docker)*

Built Valuation API from POC to production: FastAPI service handling
**$\sim$`<!-- -->`{=html}6K requests/day with zero P2 alerts** since
launch. Led Zestimate 6.6 deprecation (Redis$\rightarrow$hybrid cache
feature store for real-time valuations, legacy system shutdown), saving
**\$350K annually**. Drove several Zestimate model point releases to
completion; created MR tracking system, led ETL optimizations. Completed
CI/CD pipeline modernization across all team services with **zero
production incidents**.\
**Impact:** *\$500K+ combined annual savings, 61% alert reduction
(641$\rightarrow$`<!-- -->`{=html}249 YoY)*

  **Next-Gen Zestimate: Multimodal + NAM + Explainability** *(PyTorch,
CLIP, Databricks)* \[DualLossAutoEncoder + NAM + Per-feature
Attribution\]

Leading Image Embeddings project: experimenting with DualLossAutoEncoder
to predict property condition from **CLIP embeddings (3.3M listings)**
for Zestimate integration. Prototyping a **NAM-based (Neural Additive
Models) Zestimate variant** for intrinsic interpretability, alongside a
per-feature attribution architecture that exposes dollar-level
contributions to downstream AI agents. Led core Zestimate neural network
ETL pipeline migration to Databricks; **identified and resolved 8x
latency and 10x cost regression** before production deployment.\
**Impact:** *Building multimodal and explainability infrastructure for
next-generation valuation products*

  **Mentorship & Technical Leadership**

Managed summer intern (2023): designed project plan, weekly check-ins,
received **"strongly favorable"** feedback. Mentored **4+ engineers**
across many projects, deployments, and onboardings. Created **RFC
templates, Stacked MR best practices** etc. adopted by the team. Conduct
technical interviews, lead code reviews, and coordinate cross-team
design discussions.\

**Match Group (OkCupid)**, Machine Learning Engineer, *May 2020 -- Sep
2021*, New York City\

  **Discount Optimization** *(Python, Keras, TensorFlow, Weights and
Biases)*
\[[Wide&Deep](https://blog.research.google/2016/06/wide-deep-learning-better-together-with.html)\]

Owned **end-to-end ML pipeline** for subscription discount optimization:
feature engineering, model training, A/B testing, deployment, and
production monitoring. Discovered high prediction variance across model
runs; designed **ensemble uncertainty estimation using 100-model
bagging** to quantify and stabilize outputs for production deployment.\
**Impact:** *6% overall revenue increase through A/B tested pricing
models*

**FactSet**, ML Engineer $\rightarrow$ Senior ML Engineer, *Apr 2015 --
May 2020*, New York City\

  **ML-Powered Financial Data Extraction** *(Python, TensorFlow, Keras,
Sagemaker)* \[CNN, ELMo, BiLSTM\]

Led multiple ML initiatives: (1) **Speaker identification** system for
earnings calls using spectrograms and CNNs, (2) Private company fact
extraction from **1.6M websites** using ELMo/BiLSTM. Rewrote MLangID
language identification service. Led machine translation infrastructure
(Polish SMT achieving **BLEU 69.10**).\
**Impact:** *20% reduction in human-hours for earnings call processing,
automated extraction from millions of documents*
\[[](https://drive.google.com/file/d/1nF485POZoE2YsYuQHdvUHO1GbwkQUDfL/view)\]

  **Financial Document Search & Ranking Systems** *(Apache Spark, Java,
Python)* \[Distributed Trie, N-gram LM, Vector Space\]

Led **team of 3 engineers** on Document Screening: built autosuggestion
and concept similarity systems. Created FingerPrinter deduplication
service (**10$\times$ response improvement:
1000ms$\rightarrow$`<!-- -->`{=html}100ms**). Architected Formula Lookup
using distributed trie and n-gram language models on Spark.\
**Impact:** *Improved formula ranking from 5.6 to 2.3, 66% faster
document processing, powered StreetAccount trending news*

  **Technical Leadership**

Established engineering best practices: Jenkins CI, comprehensive test
suites, documentation standards. Mentored new hires and junior
engineers. FingerPrinter became the model Java project within the ML
group.\

**[Tata Research Development and Design
Centre](https://en.wikipedia.org/wiki/Tata_Research_Development_and_Design_Centre)**,
ML Research Engineer, *Jul 2011 -- Jul 2013*, India\

  **Event Detection in Time Series** *(Java, Python, RapidMiner)*
\[SVM - RBF\] [](http://arxiv.org/pdf/1408.3733v1.pdf)

Wrote an algorithm based on Shape Context for finding frequently
occurring patterns and events, with as good results as SAX, DTW etc.
with **7%** better results in the particular domain of car sensors.

  **[Data Harmonization Framework
(DHF)](https://ieeexplore.ieee.org/abstract/document/6597127)** *(Java,
Apache Pig)*

Implemented an ETL framework that exploits the power of map-reduce and
big-databases to fuse incongruous enterprise data from disparate sources
in near real time.

to

  ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  **Languages**       Python $\cdot$ Java $\cdot$ C/C++ $\cdot$ Bash $\cdot$ SQL
  **LLM & GenAI**     LangChain $\cdot$ RAG $\cdot$ LLM Guardrails $\cdot$ Embeddings $\cdot$ Vector DBs (Pinecone) $\cdot$ CLIP
  **Classical ML**    PyTorch $\cdot$ TensorFlow $\cdot$ A/B Testing $\cdot$ Uncertainty Estimation $\cdot$ Model Monitoring
  **Data & Infra**    PySpark $\cdot$ Databricks $\cdot$ MLflow $\cdot$ Metaflow $\cdot$ FastAPI $\cdot$ Django $\cdot$ Docker $\cdot$ Kubernetes $\cdot$ Terraform
  **Cloud & CI/CD**   AWS (S3, EC2, SageMaker) $\cdot$ GitLab CI $\cdot$ Weights & Biases
  **Leadership**      System Design $\cdot$ Technical Interviews $\cdot$ Mentoring $\cdot$ RFC Authorship $\cdot$ Cross-team Coordination
  ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------

to

**[Inferring Latent Attributes of an Indian Twitter user using
Celebrities and Class
Influencers](http://dl.acm.org/citation.cfm?id=2806657)**
[](https://www.youtube.com/watch?v=9BtWs3Rn2Ng) ACM Hypertext 2015

**[Inferring gender of a Twitter user using celebrities it
follows](http://arxiv.org/abs/1405.6667)** CORR 2014

**[Architecture for Automated Tagging and Clustering of Song Files
According to Mood](http://arxiv.org/abs/1206.2484)** IJCSI, 2010

to

**Master of Science** in Computer Science, State University of New York,
Buffalo, NY

**B. Tech.** in Computer Science and Engineering, JIIT, India

to

  ---------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ** [Organizer @ MUFin](https://sites.google.com/view/w-mufin/organizers)**                                       Program committee member, paper reviewer at top ML conferences: Workshop on Modeling Uncertainty in the Financial Sector *(AAAI 2023, ECML-PKDD 2022)*
  ** [Lotion](https://github.com/puneetsl/lotion)**                                                                Unofficial Notion.so Desktop app for Linux *(2K+ GitHub stars / 60K+ Clones & Downloads)*
  ** [Romadeva](https://github.com/puneetsl/Romadeva)**                                                            Tool to convert Roman script to Indic(Devanagari) script *(Used by [Translators Without Borders](https://translatorswithoutborders.org))*
  ** [Quena](https://www.facebook.com/photo.php?fbid=10153613108040010&set=a.10153613186550010&type=3&theater)**   Question and Answering system -- Indexed 1.6 Million Wikipedia documents, designed a question parser and a ranking algorithm based on popularity. *(Apache Solr, NER, POS tagger)*
  ---------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Download Options

- [Download Latest PDF](puneet_ludu_resume_latest.pdf)
- [View on GitHub](https://github.com/puneetsl/resume/blob/main/puneet_ludu_resume_latest.pdf)

## Previous Versions

All previous versions are available in the [versions](versions/) directory.

## Compilation Instructions

For instructions on how to compile this resume, see [RUNSTEPS.md](RUNSTEPS.md).
