from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
    },
    args=["firecrawl-mcp"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)

            messages = [
                {
                    "role": "system",
                    "content": "Você é um assistente que pode realizar scraping em sites, rastrear páginas e extrair dados usando ferramentFuias Firecrawl. Pense, passo a passo e use as ferramentas apropriadas para ajudar o usuário."
                }
            ]

            print("produtos/ferramentas/soluções/serviços disponíveis -", *[tool.name for tool in tools])
            print("-" * 60)

            while True:
                user_input = input("\nVocê: ")
                if user_input == "fui!":
                    print("Até!")
                    break

                messages.append({"role": "user", "content": user_input[:175000]})

                try:
                    agent_response = await agent.ainvoke({"messages": messages})

                    ai_message = agent_response["messages"][-1].content
                    print("\nAgent:", ai_message)
                except Exception as e:
                    print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())