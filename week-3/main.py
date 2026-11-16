
import os
from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient
from mongo_logger import MongoLogger


def main():

    load_dotenv(override=True)

    print("\n===== WEEK 3: LLM MONITORING SYSTEM =====")
    print("1. Gemini")
    print("2. Ollama")

    choice = input("\nChoose your AI provider (1 or 2): ")

    logger = None

    try:
        logger = MongoLogger()

        if choice == "1":

            api_key = os.getenv("GEMINI_API_KEY")

            if not api_key:
                raise ValueError("GEMINI_API_KEY is missing from .env")

            provider = GeminiProvider(api_key)

        elif choice == "2":

            provider = OllamaProvider()

        else:
            print("Invalid choice. Please select 1 or 2.")
            return

        client = LLMClient(provider, logger)

        prompt = input("\nEnter your question: ")

        print("\nGenerating response...\n")

        answer = client.generate(prompt)

        print("AI Response:")
        print(answer)

    except Exception as error:

        print("\nSomething went wrong:")
        print(error)

    finally:

        if logger:
            logger.close()


if __name__ == "__main__":
    main()
