def build_prompt(context_block: str, user_query: str) -> str:
    return f"""
You are CALA, a friendly and thoughtful life assistant that uses rich context to provide tailored suggestions.

--- CONTEXT ---
{context_block}

--- USER QUERY ---
{user_query}

--- RESPONSE ---
"""
