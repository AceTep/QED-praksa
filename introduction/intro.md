## Agentic Flow
proces kojim agent rjesava komlekse zadatke kroz niz koraka koji su slicni covjeku.

1. Razumijevanje cilja ili ulaza (npr. pitanje korisnika)
2. Planiranje koraka potrebnih da se dođe do rješenja
3. Pozivanje alata (npr. tražilica, baze podataka, API-jevi, itd.)
4. Pamćenje stanja (što je već naučio ili dobio kao rezultat)
5. Petlje i grananje (ako nešto ne valja, ponovi ili ide drugim putem)
- **LangGraph** - python framework koji se koristi da se lagano napravi i pokrene agentic flow

Prednosti:
- Pamti stanje između koraka
- Pruža kontrolu toka (ako A, idi na B, inače na C...)
- Podržava paralelno izvođenje više agenata
- Dobro se integrira s LangChainom, OpenAI, itd
- Može se vizualizirati, pratiti, i skalirati

## LLM Models (LangChain)
- **Ollama** - Ollama je alat za lokalno pokretanje LLM modela (npr. LLaMA, Mistral, Gemma...) na tvojem računalu.

    - Podržava kvantizirane modele (brži, manji)


- **OpenAI**

| Model           | Namjena                            | Arhitektura                  | Napomena                                 |
|-----------------|-------------------------------------|------------------------------|------------------------------------------|
| `gpt-4.1-mini`  | Generiranje teksta                 | LLaMA-4 Scout (kvantiziran)  | Brži, manji model                         |
| `gpt-4.1-nano`  | Tool calling (pozivanje alata)     | Mixtral                      | Za agenta koji poziva funkcije           |
| `gpt-4.1`       | LLM-as-a-Judge (evaluacija)        | Viši kapacitet               | Koristi se za usporedbu odgovora         |
| `gpt-4o-mini`   | Brzo generiranje + tool use        | Višemodalni (tekst+slika)    | Dio GPT-4o obitelji (novi)               |

### RAG 
To je tehnika u području velikih jezičnih modela (LLM) koja kombinira:

- Retrieval — dohvaćanje relevantnih informacija iz baze podataka, dokumenata ili vanjskih izvora (npr. vektorska baza s embeddingima)

- Generation — generiranje odgovora ili teksta pomoću LLM-a koristeći te dohvaćene informacije kao dodatni kontekst



## Logging

Kada koristiš LLM tokove, agente i više koraka u LangChainu, praćenje ponašanja modela i tokova je ključno za:
- debugiranje
- mjerenje performansi
- praćenje korisničke interakcije
- analizu promptova i odgovora

### Logging alati u LangChain ekosustavu

| Alat        | Opis                                           | Integracija s LangChainom | Ključne značajke                                              |
|-------------|------------------------------------------------|----------------------------|---------------------------------------------------------------|
| **LangSmith** | Alat od tvoraca LangChaina za **debug i praćenje** | Izvorna / native           | - Vizualizacija toka<br>- Praćenje promptova<br>- Usporedba verzija |
| **LangFuse**  | Open-source alternativa za **praćenje i metrike**  | API / SDK                  | - Tracing<br>- Latency metrike<br>- A/B testiranje i evaluacija    |



## Code
- **GitHub** (versioning of code)
- **Jupyter Notebook** (Google Colab, Local Jupyter)

## Data Preparation
Priprema podataka je ključni korak kod rada s LLM-ovima i agentima. To uključuje:

- Učitavanje i čišćenje podataka
- Strukturiranje podataka (CSV, JSON, PDF...)
- Parsiranje dokumenata, tablica, tekstova
- Chunkanje za vektorizaciju i embeddinge

### Najčešće Python biblioteke za Data Preparation

| Biblioteka     | Namjena                                      | Primjeri korištenja                               |
|----------------|-----------------------------------------------|---------------------------------------------------|
| **pandas**     | Rad s tabličnim podacima (CSV, Excel, JSON)   | Učitavanje i čišćenje CSV-a                       |
| **numpy**      | Numeričke operacije i rad s matricama         | Statistike, transformacije podataka               |
| **re**         | Regularni izrazi za obradu teksta             | Ekstrakcija entiteta, čišćenje                    |
| **langchain**  | Učitavanje dokumenata, chunkanje, parseri     | `DocumentLoader`, `TextSplitter`, `Docstore`     |
| **PyMuPDF (fitz)** | Čitanje PDF dokumenata                    | Parsiranje teksta i strukture iz PDF-ova          |
| **unstructured** | Izvlačenje teksta iz raznih formata         | Word, HTML, PDF, itd.                             |
| **tiktoken**   | Tokenizacija i brojanje tokena (OpenAI modeli)| Chunkanje prema broju tokena                      |
| **BeautifulSoup** | Parsiranje HTML/XML dokumenata             | Scraping i obrada web-stranica                    |
| **json / orjson** | Rad s JSON podacima                        | Učitavanje i parsiranje JSON zapisa               |

## Chunking
Chunking je proces dijeljenja velikih dokumenata ili tekstova u manje dijelove ("chunkove") koje LLM može lakše obraditi (zbog ograničenja tokena i boljeg konteksta).

- **LangChain**
    - *(If time permits, consider building a custom solution)*

## Embeddings
Embedding predstavlja tekst kao niz brojeva (vektor) koji model može razumjeti i uspoređivati. Ključno je za:

- semantičko pretraživanje
- sličnost dokumenata
- retrival-based upite (RAG)
- klasifikaciju, klasteriranje

### Embedding modeli: Ollama vs OpenAI

| Pružatelj   | Model                     | Dimenzija | Lokacija izvršavanja | Bilješke                                   |
|-------------|---------------------------|-----------|-----------------------|--------------------------------------------|
| **Ollama**  | npr. `nomic-embed-text`    | 768       | Lokalno (offline)     | Brz, privatnost, bez troškova po pozivu    |
| **OpenAI**  | `text-embedding-3-small`   | 1536      | Cloud (API)           | Precizan, skupa kvaliteta, ali uz trošak   |
|             | `text-embedding-3-large`   | 3072      | Cloud (API)           | Viša preciznost i veći kontekst            |


## Vector Database
Vektorske baze podataka omogućuju spremanje i brzo pretraživanje embedding vektora, što je ključno za:

- Semantičko pretraživanje
- Retrieval-Augmented Generation (RAG)
- Sličnost dokumenata ili slika
- Klasifikaciju i detekciju anomalija

---
### Osnovne informacije: Milvus

| Svojstvo             | Vrijednost                                 |
|----------------------|---------------------------------------------|
| Tehnologija          | Vektorska baza (C++, Go backend)            |
| Tip pretraživanja    | Approximate Nearest Neighbors (ANN)         |
| Podržani indeksi     | IVF, HNSW, Flat, ANNOY                      |
| Način rada           | Lokalno (Docker) ili putem Milvus Cloud     |
| Integracija          | LangChain, LlamaIndex, Haystack, itd.       |
| Upravljački alat     | Milvus Insight, pymilvus (Python SDK)       |
