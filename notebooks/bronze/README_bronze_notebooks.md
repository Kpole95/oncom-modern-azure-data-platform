# Bronze Notebooks - Standardized Markdown

These notebooks follow a consistent Bronze ingestion pattern:

1. Run shared libraries.
2. Define entity-specific variables.
3. Read data from the Raw Delta path.
4. Verify the DataFrame schema.
5. Write the DataFrame into the Bronze schema.
6. Run validation checks when they already exist in the original notebook.