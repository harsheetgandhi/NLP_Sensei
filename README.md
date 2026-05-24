# 90-Day NLP Mastery Plan

## 🔹 Phase 1: Core NLP Fundamentals (Days 1–28) [cite: 11]

### Week 1 (Days 1–7): Word Embeddings [cite: 11]
* **Day 1-2 (Theory):** Study Distributional Semantics, Word2Vec (Skip-gram, CBOW), and GloVe from Lena's blog[cite: 11]. Understand Intrinsic vs. Extrinsic evaluation[cite: 12].
* **Day 3-4 (Code):** Pull week01_embeddings from the YSDA repo[cite: 12]. Complete the seminar on training and playing with word/sentence embeddings[cite: 13].
* **Day 5-6 (Test):** Build the homework task: An embedding-based Machine Translation system[cite: 14]. Test your model's accuracy[cite: 14].
* **Day 7 (Summarize):** Push your code to your GitHub repo[cite: 15]. Write a summary of how Word2Vec maps semantic relationships[cite: 16].

### Week 2 (Days 8–14): Language Modeling (LM) [cite: 17]
* **Day 8-9 (Theory):** Read about Left-to-Right frameworks, N-gram LMs, and Neural LMs (RNNs, CNNs)[cite: 17]. Understand Perplexity[cite: 18].
* **Day 10-11 (Code):** Pull week02_lm[cite: 18]. Build an N-gram language model from scratch following the seminar notebook[cite: 18].
* **Day 12-13 (Test):** Complete the homework on Neural LMs and implement smoothing for count-based models[cite: 19].
* **Day 14 (Summarize):** Push to GitHub[cite: 20]. Summarize the transition from counting N-grams to predicting with Neural Networks[cite: 20].

### Week 3 (Days 15–21): Seq2Seq & Attention (The turning point) [cite: 21]
* **Day 15-16 (Theory):** Study the Encoder-Decoder framework, Attention mechanisms, Subword Segmentation (BPE), and Beam Search[cite: 22].
* **Day 17-18 (Code):** Pull week03_attention[cite: 23]. Implement a basic sequence-to-sequence model in PyTorch[cite: 23].
* **Day 19-20 (Test):** Tackle the core homework: Build a Machine Translation system with Attention[cite: 24].
* **Day 21 (Summarize):** Push your code[cite: 25]. Write a visually-rich GitHub summary explaining how Attention solves the sequence bottleneck problem[cite: 25].

### Week 4 (Days 22–28): Transfer Learning & Transformers [cite: 26]
* **Day 22-23 (Theory):** Learn the Transformer architecture (Self-Attention, Multi-head attention)[cite: 27]. Read about CoVe, ELMo, GPT, and BERT paradigms[cite: 28].
* **Day 24-25 (Code):** Pull week04_transfer[cite: 28]. Load pre-trained models using the Hugging Face transformers library[cite: 29].
* **Day 26-27 (Test):** Complete the homework: Fine-tune a pre-trained BERT model for text classification[cite: 30].
* **Day 28 (Summarize):** Push to GitHub[cite: 31]. Document the "Pre-train and Fine-tune" paradigm[cite: 31].

---

## 🔹 Phase 2: The LLM Revolution (Days 29–56) [cite: 32]

### Week 5 (Days 29–35): Large Language Models (LLMs) [cite: 32]
* **Day 29-30 (Theory):** Study Scaling Laws, Emergent Abilities, and the landscape of Open-Source LLMs (Llama, Mistral, etc.)[cite: 32].
* **Day 31-33 (Code & Test):** Pull week05_llm[cite: 33]. Get hands-on with open-source LLMs using local inference or Colab[cite: 33].
* **Day 34-35 (Summarize):** Document your experiments with different model sizes and capabilities on your GitHub[cite: 34].

### Week 6 (Days 36–42): Prompting & In-Context Learning (ICL) [cite: 35]
* **Day 36-37 (Theory):** Learn prompt engineering techniques, Chain-of-Thought (CoT) reasoning, and the mechanics of ICL[cite: 35].
* **Day 38-40 (Code & Test):** Pull week06_prompting[cite: 36]. Complete the homework by doing manual prompt engineering and implementing CoT reasoning for complex tasks[cite: 36].
* **Day 41-42 (Summarize):** Create a Prompting guide in your GitHub repo detailing which techniques yield the best results[cite: 37].

### Week 7 (Days 43–49): Fine-tuning (PEFT & RLHF) [cite: 38]
* **Day 43-44 (Theory):** Understand Parameter-Efficient Fine-Tuning (LoRA, Adapters) and Reinforcement Learning from Human Feedback (RLHF)[cite: 38].
* **Day 45-47 (Code & Test):** Pull week07_finetuning[cite: 39]. Train a LoRA adapter on an open-source LLM to adapt it to a new domain without updating all weights[cite: 39].
* **Day 48-49 (Summarize):** Push your PEFT scripts to GitHub[cite: 40]. Summarize the math behind Low-Rank Adaptation[cite: 40].

### Week 8 (Days 50–56): Model Efficiency [cite: 41]
* **Day 50-51 (Theory):** Study Quantization (running big models on small GPUs), Knowledge Distillation, Pruning, and Speculative Decoding[cite: 41].
* **Day 52-54 (Code & Test):** Pull week08_efficiency[cite: 42]. Test quantized models (e.g., 4-bit/8-bit models) and complete the efficiency homework[cite: 42].
* **Day 55-56 (Summarize):** Document the latency/memory vs. accuracy trade-offs of quantization in your repo[cite: 43].

---

## 🔹 Phase 3: Advanced Systems & Production (Days 57–90) [cite: 44]

### Week 9 (Days 57–63): Retrieval-Augmented Generation (RAG) [cite: 44]
* **Day 57-58 (Theory):** Learn about Dense Retrieval, Vector Databases, and RAG architectures to ground LLMs in external data[cite: 44].
* **Day 59-61 (Code & Test):** Pull week09_retrieval[cite: 45]. Build a RAG pipeline from scratch to answer questions over a specific document corpus[cite: 45].
* **Day 62-63 (Summarize):** Push your RAG application to GitHub and document its architecture[cite: 46].

### Week 10 (Days 64–70): AI Agents [cite: 47]
* **Day 64-65 (Theory):** Study Agent Architectures, Tool Use (function calling), and Memory modules[cite: 47].
* **Day 66-68 (Code & Test):** Pull week10_agents[cite: 48]. Build an LLM agent that can execute code, search the web, or use calculators[cite: 48].
* **Day 69-70 (Summarize):** Document how you parse LLM outputs to trigger deterministic functions[cite: 49].

### Week 11 (Days 71–75): Interpretability [cite: 50]
* **Day 71-72 (Theory):** Read about Probing and Mechanistic Interpretability[cite: 50]. Learn how to look inside the "black box"[cite: 51].
* **Day 73-74 (Code & Test):** Pull week11_interpretability[cite: 51]. Run the probing seminar to identify linguistic structures inside attention heads[cite: 52].
* **Day 75 (Summarize):** Write a blog-style README on how Attention heads specialize in different tasks[cite: 53].

### Week 12 (Days 76–80): Multimodal LLMs [cite: 54]
* **Day 76-77 (Theory):** Understand how vision and text are fused (e.g., CLIP, LLaVA)[cite: 54].
* **Day 78-79 (Code):** Pull week12_multimodal[cite: 55]. Experiment with open-source Vision-Language models[cite: 55].
* **Day 80 (Summarize):** Push multimodal generation/captioning code to your repo[cite: 56].

### Week 13 (Days 81–85): Building LLM Systems [cite: 57]
* **Day 81-82 (Theory):** Learn the engineering side of LLMs: Batching, Caching, API integration, and orchestration[cite: 57].
* **Day 83-84 (Code):** Pull week13_llm_systems[cite: 58]. Optimize an inference pipeline[cite: 58].
* **Day 85 (Summarize):** Document system-level best practices for LLM deployment[cite: 59].

### Week 14 (Days 86–90): Agents in Production & Final Review [cite: 60]
* **Day 86-87 (Theory):** Pull week14_agents_production[cite: 60]. Learn about monitoring, evaluating, and scaling AI agents[cite: 61].
* **Day 88-89 (Project Code):** Wrap all your learning into a final mini-project: Build an end-to-end RAG Agent that uses a LoRA fine-tuned model and external tools, wrapped in a simple UI (like Streamlit)[cite: 62].
* **Day 90 (The Master Repo):** Polish your GitHub repository[cite: 63]. Ensure all 14 weeks are cleanly organized with well-documented READMEs, requirements.txt files, and execution instructions[cite: 64].
