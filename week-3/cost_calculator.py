
PRICING = {
    "gemini-3.5-flash-lite": {
        "input": 0.50,
        "output": 2.00
    }
}


def calculate_cost(provider, model, input_tokens, output_tokens):

    if provider == "OllamaProvider":
        return 0.0

    if model not in PRICING:
        return None

    input_cost = (input_tokens / 1_000_000) * PRICING[model]["input"]

    output_cost = (output_tokens / 1_000_000) * PRICING[model]["output"]

    total_cost = input_cost + output_cost

    return round(total_cost, 10)
