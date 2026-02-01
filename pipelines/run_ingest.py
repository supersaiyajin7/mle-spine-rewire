from pipelines.ingest import ingest_document

if __name__ == "__main__":
    content = "This is a sample document about machine learning."
    # metadata = {
    #     "author": "test_user",
    #     "category": "ml"
    # }
    metadata = {}

    doc = ingest_document(
        source="manual_test",
        content=content,
        metadata=metadata
    )

    print("Ingested document:", doc.document_id if doc else "FAILED")
