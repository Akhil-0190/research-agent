import json
cleaned = '{"success": true}'

def safe_json_parse(response):
    try:
        json_array_start = response.find('{')
        if json_array_start == -1:
            raise ValueError("No JSON array found.")
        cleaned = response[json_array_start:]
        json_array_end = cleaned.rfind('}')
        if json_array_end != -1:
            cleaned = cleaned[:json_array_end + 1]
        return json.loads(cleaned)
    except Exception as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        print(f"[RAW OUTPUT]\n{response}")
        return None
    
print(safe_json_parse(cleaned))