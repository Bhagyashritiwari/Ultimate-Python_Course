from transformers import AutoModelForCausalLM, AutoTokenizer

# Load BLOOM Model
model_name = "bigscience/bloom"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# SQL Injection Vulnerable Code
sql_injection_code = """
import sqlite3

def get_user_details(username):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result

username = "admin' OR '1'='1"
print(get_user_details(username))
"""

# Insecure API Call Vulnerable Code
insecure_api_code = """
import requests

def fetch_data():
    # Insecure API call without SSL verification
    response = requests.get("http://example.com/api/data", verify=False)
    return response.json()

print(fetch_data())
"""

# Run the model
inputs = tokenizer(sql_injection_code + "\n" + insecure_api_code, return_tensors="pt")
outputs = model.generate(**inputs, max_length=512)

print("BLOOM Analysis:\n", tokenizer.decode(outputs[0]))
