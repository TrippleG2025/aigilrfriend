from ..config import MOCK_EXTERNAL_CALLS

def chat_completion(character_key: str, user_text: str) -> str:
    if MOCK_EXTERNAL_CALLS:
        return f"[{character_key}] Mock: {user_text}"
    # Real OpenAI call will be added for staging/prod
    raise NotImplementedError("Live OpenAI not enabled in Codex environment")
