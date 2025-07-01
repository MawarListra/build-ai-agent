import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

load_dotenv()

def simple_search(documents, query):
    """Simple text search without embeddings"""
    query_lower = query.lower()
    results = []
    
    for doc in documents:
        content = doc.page_content.lower()
        if any(word in content for word in query_lower.split()):
            # Get relevant paragraph
            sentences = content.split('.')
            relevant = []
            for sentence in sentences:
                if any(word in sentence for word in query_lower.split()):
                    relevant.append(sentence.strip())
            
            if relevant:
                results.extend(relevant[:2])  # Take first 2 relevant sentences
    
    return results

try:
    print("Loading PDF document...")
    loader = PyPDFLoader("document/contoh_kebijakan.pdf")
    documents = loader.load()
    print(f"✅ Document loaded successfully! Found {len(documents)} pages.")
    
    # Split text for better search
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)
    print(f"✅ Text split into {len(docs)} chunks for better search.")
    
    print("\n" + "="*50)
    print("🤖 Simple Document Search Ready!")
    print("📄 Document: contoh_kebijakan.pdf")
    print("ℹ️  Mode: Local text search (no AI)")
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
                
            print("\n🔍 Mencari dalam dokumen...")
            results = simple_search(docs, query)
            
            if results:
                print(f"\n📋 Ditemukan {len(results)} hasil yang relevan:")
                for i, result in enumerate(results, 1):
                    cleaned = re.sub(r'\s+', ' ', result).strip()
                    if cleaned:
                        print(f"\n{i}. {cleaned}")
            else:
                print("\n❌ Tidak ditemukan hasil yang relevan.")
                print("💡 Coba gunakan kata kunci yang berbeda.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan. Sampai jumpa!")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")

except Exception as e:
    if "File path" in str(e):
        print(f"\n❌ ERROR: File tidak ditemukan")
        print(f"📁 File yang dicari: document/contoh_kebijakan.pdf")
        print("🔧 Solusi: Pastikan file PDF ada di folder yang benar")
    else:
        print(f"\n❌ ERROR: {e}")
        print("🔧 Pastikan semua dependencies terinstall dengan benar")
