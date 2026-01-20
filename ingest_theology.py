#!/usr/bin/env python3
"""
Bulk ingestion script for theology papers.

This script populates ChromaDB with theology research papers from OpenAlex.
Run this to set up your RAG system's knowledge base.
"""
import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.ingest import ingest_openalex_query
from src.vectorstore import add_documents

# Theology topics to ingest
THEOLOGY_QUERIES = [
    "systematic theology",
    "biblical theology",
    "theological anthropology",
    "doctrine of God",
    "Christology",
    "pneumatology",
    "soteriology",
    "ecclesiology",
    "eschatology",
    "theological hermeneutics",
    "doctrine of sin",
    "doctrine of salvation",
    "doctrine of Trinity",
    "covenant theology",
    "theological ethics",
]

def main():
    """Ingest theology papers into ChromaDB."""
    print("=" * 60)
    print("GRAYSON Theology Database Ingestion")
    print("=" * 60)
    print(f"\nIngesting {len(THEOLOGY_QUERIES)} theology topics...")
    print(f"This will take several minutes.\n")

    total_ingested = 0

    for i, query in enumerate(THEOLOGY_QUERIES, 1):
        print(f"[{i}/{len(THEOLOGY_QUERIES)}] Fetching: {query}")
        try:
            # Fetch papers from OpenAlex
            records = ingest_openalex_query(query, max_results=20)

            if records:
                # Add to ChromaDB
                add_documents(records)
                total_ingested += len(records)
                print(f"  [OK] Added {len(records)} papers")
            else:
                print(f"  [WARN] No papers found")

            # Be nice to the API
            time.sleep(1)

        except Exception as e:
            print(f"  [ERROR] {e}")
            continue

    print("\n" + "=" * 60)
    print(f"Ingestion complete! Total papers: {total_ingested}")
    print("=" * 60)
    print("\nYour ChromaDB is now populated with theology research.")
    print("You can start querying your RAG system!")

if __name__ == "__main__":
    main()
