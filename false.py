from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

# Load the flow definition from flow.yaml
flow = Flow(source="flow.yaml")

# Input dictionary for context-based joke generation
input_dict = {
    "context": "After a long day at work, everything goes hilariously wrong"
}

# Test the flow with the given input
response = client.flow.test(flow, input_dict)

# Extract and print only the joke from the response
if isinstance(response, dict) and "result" in response:
    print(response["result"].split("Here's a witty joke based on the given context:\n\n")[-1])
else:
    print("Failed to generate a joke. Please check your input or configuration.")
