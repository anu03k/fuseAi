import requests

thoughts = [
    "I always fail at everything",  # all-or-nothing
    "Nothing ever goes right",  # overgeneralization
    "I only focus on my mistakes",  # mental filter
    "It's my fault my team lost",  # personalization
    "I had a balanced day with ups and downs",  # no distortion
]

for thought in thoughts:
    response = requests.post(
        "http://localhost:8000/check-distortion", params={"thought": thought}
    )
    print(f"Thought: {thought}")
    try:
        print("Response:", response.json())
    except Exception as e:
        print("Failed to parse JSON:", e)
    print("\n")
