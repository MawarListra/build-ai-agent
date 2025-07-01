# 🤖 AI Document Assistant

Sistem AI untuk melakukan tanya jawab dengan dokumen PDF menggunakan LangChain dan OpenAI API.

## 📋 Deskripsi

AI Document Assistant adalah aplikasi yang memungkinkan pengguna untuk:

- 📄 Memuat dan memproses dokumen PDF
- 🔍 Melakukan pencarian cerdas dalam dokumen
- 💬 Bertanya tentang isi dokumen dan mendapat jawaban yang relevan
- 🧠 Menggunakan AI untuk memberikan jawaban yang kontekstual

## 🏗️ Arsitektur Agent

### Komponen Utama:

- **Prompt + Memory**
  - Prompt dinamis dengan konteks dari dokumen
  - Memory menggunakan pendekatan **Semantic Memory** (vector store FAISS)
- **Tool / Function**

  - Tool utama: pencarian dokumen menggunakan vector similarity
  - Tool opsional: fallback pencarian lokal (non-AI)

- **Model**
  - LLM: `gpt-3.5-turbo` dari OpenAI
  - Embedding: `text-embedding-ada-002`
  - Vector DB: FAISS (lokal)

---

## 🔁 Agent Loop (Observe → Decide → Act)

1. **Observe**: User menginput pertanyaan dalam bahasa natural
2. **Decide**: Sistem mencocokkan pertanyaan ke chunk dokumen terdekat (via vector search)
3. **Act**: Jawaban dihasilkan oleh LLM berdasarkan konteks dokumen

---

## 🚀 Fitur

- ✅ Memuat dokumen PDF internal
- ✅ Preprocessing dan chunking otomatis
- ✅ Pencarian berbasis vector
- ✅ Integrasi OpenAI untuk QnA
- ✅ Alternatif offline (local string matching)
- ✅ Error handling user-friendly

## 📁 Struktur Proyek

```
build-ai-agent/
├── agent/
│   ├── main.py          # Script utama dengan OpenAI API
│   ├── main_local.py    # Versi pencarian lokal
│   └── main_test.py     # Script untuk testing
├── document/
│   └── contoh_kebijakan.pdf  # Dokumen contoh
├── .env                 # Environment variables
├── requirements.txt     # Dependencies Python
└── README.md           # File dokumentasi ini
```

## 🛠️ Instalasi

### 1. Clone Repository

```bash
git clone <repository-url>
cd build-ai-agent
```

### 2. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # di macOS/Linux
# atau
venv\Scripts\activate     # di Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Buat file `.env` di root directory:

```env
OPENAI_API_KEY="your-openai-api-key-here"
```

## 🚦 Cara Penggunaan

### Opsi 1: Menggunakan OpenAI API (Rekomendasi)

```bash
python3 agent/main.py
```

**Persyaratan:**

- ✅ OpenAI API key yang valid
- ✅ Credit/quota yang cukup di akun OpenAI

### Opsi 2: Menggunakan Pencarian Lokal

```bash
python3 agent/main_local.py
```

**Keunggulan:**

- ✅ Tidak perlu API key
- ✅ Berjalan sepenuhnya offline
- ✅ Gratis dan cepat

### Opsi 3: Testing Mode

```bash
python3 agent/main_test.py
```

## 💡 Contoh Penggunaan

```bash
$ python3 agent/main_local.py

🤖 Simple Document Search Ready!
📄 Document: contoh_kebijakan.pdf
ℹ️  Mode: Local text search (no AI)
💡 Tip: Type 'quit' or 'exit' to stop

❓ Masukkan pertanyaanmu: Apa itu kebijakan cuti?

🔍 Mencari dalam dokumen...

📋 Ditemukan 2 hasil yang relevan:

1. kebijakan cuti tahunan - karyawan tetap berhak atas cuti tahunan sebanyak 12 hari kerja per tahun
2. cuti dapat diambil setelah melewati masa kerja minimal 1 tahun

❓ Masukkan pertanyaanmu: quit
👋 Terima kasih! Sampai jumpa!
```

## 🔧 Konfigurasi

### Environment Variables

| Variable         | Deskripsi           | Required           |
| ---------------- | ------------------- | ------------------ |
| `OPENAI_API_KEY` | API key dari OpenAI | Ya (untuk main.py) |

### Dependencies Utama

- `langchain` - Framework untuk aplikasi LLM
- `openai` - Client OpenAI API
- `faiss-cpu` - Vector database untuk similarity search
- `PyPDF2` - Library untuk memproses PDF
- `python-dotenv` - Memuat environment variables

## ⚠️ Troubleshooting

### Error: OpenAI API Quota Exceeded

```
❌ ERROR: OpenAI API Quota Exceeded
```

**Solusi:**

1. Cek billing settings di [OpenAI Platform](https://platform.openai.com/account/billing)
2. Tambahkan payment method dan credit
3. Gunakan alternatif `main_local.py`

### Error: File tidak ditemukan

```
❌ ERROR: File tidak ditemukan
```

**Solusi:**

1. Pastikan file `contoh_kebijakan.pdf` ada di folder `document/`
2. Periksa nama file dan path yang benar

### Error: Import modules

```
ModuleNotFoundError: No module named 'langchain'
```

**Solusi:**

```bash
pip install -r requirements.txt
```

## 👨‍💻 Author

**AI Enhancement Course Project**

- 📧 Email: [listramawar@gmail.com]
- 🌐 GitHub: [(https://github.com/MawarListra)]

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) - Framework LLM yang powerful
- [OpenAI](https://openai.com/) - API untuk embeddings dan language model
- [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search

---

⭐ **Jika project ini membantu, jangan lupa beri star!** ⭐
