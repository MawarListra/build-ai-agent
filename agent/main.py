import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

try:
    print("Loading PDF document...")
    # Load document - fixed path
    loader = PyPDFLoader("document/contoh_kebijakan.pdf")
    pages = loader.load_and_split()
    print(f"✅ Document loaded successfully! Found {len(pages)} pages.")

    print("Creating embeddings and vector store...")
    # Embedding & vector store
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_documents(pages, embedding)
    print("✅ Vector store created successfully!")

    print("Setting up QA chain...")
    # Setup LLM and QA chain
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    print("✅ QA chain ready!")

    # Interactive Q&A loop
    print("\n" + "="*50)
    print("🤖 AI Document Assistant Ready!")
    print("📄 Document: contoh_kebijakan.pdf")
    print("💡 Tip: Type 'quit' or 'exit' to stop")
    print("="*50)
    
    while True:
        try:
            query = input("\n❓ Masukkan pertanyaanmu: ")
            
            if query.lower() in ['quit', 'exit', 'keluar']:
                print("👋 Terima kasih! Sampai jumpa!")
                break
                
            if not query.strip():
                print("⚠️ Pertanyaan tidak boleh kosong!")
                continue
                
            print("\n🔍 Mencari jawaban...")
            response = qa_chain.run(query)
            print(f"\n💬 Jawaban:\n{response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan. Sampai jumpa!")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error saat memproses pertanyaan: {e}")
            print("💡 Silakan coba pertanyaan lain.")

except Exception as e:
    error_type = type(e).__name__
    
    if "RateLimitError" in error_type or "insufficient_quota" in str(e):
        print("\n❌ ERROR: OpenAI API Quota Exceeded")
        print("📋 Penyebab: Limit penggunaan API OpenAI sudah terlampaui")
        print("🔧 Solusi:")
        print("   1. Cek billing settings di https://platform.openai.com/account/billing")
        print("   2. Tambahkan credit atau upgrade plan")
        print("   3. Tunggu reset quota bulanan")
        
    elif "invalid_api_key" in str(e) or "api_key" in str(e):
        print("\n❌ ERROR: API Key tidak valid")
        print("🔧 Solusi: Periksa kembali API key di file .env")
        
    elif "File path" in str(e):
        print(f"\n❌ ERROR: File tidak ditemukan")
        print(f"📁 File yang dicari: document/contoh_kebijakan.pdf")
        print("🔧 Solusi: Pastikan file PDF ada di folder yang benar")
        
    else:
        print(f"\n❌ ERROR: {error_type}")
        print(f"📝 Detail: {e}")
        
    print(f"\n💡 Untuk testing, coba jalankan: python3 agent/main_test.py")
