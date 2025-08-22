import os

from dotenv import load_dotenv


load_dotenv()

SMITHERY_API_KEY = os.getenv('SMITHERY_API_KEY')
MCP_SERVERS_CONFIG = {
    'duck-duck-go-search': {
        'url': f'https://server.smithery.ai/@nickclyde/duckduckgo-mcp-server/mcp?api_key={SMITHERY_API_KEY}&profile=fun-grasshopper-kwJEdG',
        'transport': 'streamable_http',
    },
}
