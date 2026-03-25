from openai import OpenAI

client = OpenAI(api_key=" sk-... ")

resp = client.responses.create(
    model="gpt-5",
    tools=[
        {
            "type": "mcp",
            "server_label": "Dropbox",
            "connector_id": "connector_dropbox",
            "authorization": "<oauth access token>",
            "require_approval": "never",
        },
    ],
    input="write me 2 lines about india.",
)

print(resp.output_text)