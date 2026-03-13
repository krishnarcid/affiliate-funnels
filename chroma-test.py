#!/usr/bin/env python3
"""
Chroma Test - Vector Database for Sacredbod
Stores prospect data, content embeddings, semantic search
"""
import chromadb
from chromadb.config import Settings

def main():
    print("=" * 70)
    print("CHROMA VECTOR DATABASE - Sacredbod")
    print("=" * 70)
    print()
    
    # Initialize Chroma
    print("Initializing Chroma...")
    client = chromadb.PersistentClient(path="./chroma_db")
    print("Status: Connected")
    print()
    
    # Create collection for prospects
    print("Creating 'prospects' collection...")
    prospects_collection = client.get_or_create_collection(
        name="prospects",
        metadata={"description": "SDR hunted prospects"}
    )
    print("Collection created: prospects")
    print()
    
    # Add test prospect
    print("Adding test prospect...")
    prospects_collection.add(
        documents=["Marketing Mojo - Digital marketing agency with weak landing page copy, unclear CTA, long-winded sentences"],
        metadatas=[{
            "company": "Marketing Mojo",
            "source": "LinkedIn",
            "status": "DISCOVERED",
            "pain_point": "Weak landing page copy",
            "timestamp": "2026-03-13"
        }],
        ids=["marketing-mojo-001"]
    )
    print("Added: Marketing Mojo")
    print()
    
    # Create collection for content
    print("Creating 'content' collection...")
    content_collection = client.get_or_create_collection(
        name="content",
        metadata={"description": "Generated marketing content"}
    )
    print("Collection created: content")
    print()
    
    # Add test content
    print("Adding test content...")
    content_collection.add(
        documents=["Running a marketing agency used to mean managing 10+ different tools..."],
        metadatas=[{
            "type": "LinkedIn blog",
            "project": "GoHighLevel",
            "tone": "professional",
            "timestamp": "2026-03-13"
        }],
        ids=["content-001"]
    )
    print("Added: Sample content")
    print()
    
    # Query test
    print("Testing semantic search...")
    results = prospects_collection.query(
        query_texts=["landing page problems"],
        n_results=1
    )
    print(f"Query results: {len(results['documents'][0])} matches")
    print(f"  - {results['documents'][0][0][:50]}...")
    print()
    
    # Stats
    print("Database Stats:")
    print(f"  - Prospects collection: {prospects_collection.count()} documents")
    print(f"  - Content collection: {content_collection.count()} documents")
    print()
    
    print("=" * 70)
    print("CHROMA STATUS: OPERATIONAL")
    print("=" * 70)
    print()
    print("Use cases:")
    print("  1. Semantic search for similar prospects")
    print("  2. Content similarity matching")
    print("  3. Pain point clustering")
    print("  4. Prospect scoring")
    print()
    print("Next: Populate with 7 hunted prospects")
    print("=" * 70)

if __name__ == "__main__":
    main()
