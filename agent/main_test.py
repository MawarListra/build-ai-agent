import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

print("=== Testing Script ===")
print(f"API Key loaded: {'Yes' if openai_api_key else 'No'}")

# Simulate the loading and processing
print("Loading document...")
print("Creating embeddings...")
print("Setting up QA chain...")

# Test the input part
print("\n=== Ready for Questions ===")
try:
    query = input("Masukkan pertanyaanmu: ")
    print(f"\nAnda bertanya: {query}")
    print("\nJawaban:")
    print("Maaf, sistem sedang dalam mode testing. Fitur QA belum bisa digunakan karena ada masalah dengan OpenAI API quota.")
except KeyboardInterrupt:
    print("\nProgram dihentikan oleh user.")
except Exception as e:
    print(f"Error: {e}")
