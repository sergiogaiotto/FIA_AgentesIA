---
mode: ask
---
{
  "ai_agent_development": {
    "description": "Prompts para desenvolvimento de agentes de IA",
    "prompts": {
      "langchain_workflow": "Ao criar workflows com LangGraph, sempre use StateGraph com tipos bem definidos no Pydantic. Implemente nodes separados para cada etapa (extract, research, analyze) e adicione tratamento de erros robusto.",
      
      "mcp_integration": "Para integração MCP, use ClientSession e stdio_client do mcp. Configure server_params com variáveis de ambiente apropriadas. Implemente async/await corretamente para todas as operações.",
      
      "firecrawl_usage": "Com Firecrawl, sempre use ScrapeOptions com formats=['markdown'] para melhor extração. Limite search results a 3-5 para performance. Implemente fallbacks quando scraping falhar.",
      
      "pydantic_models": "Modelos Pydantic devem ter tipos opcionais para campos que podem não estar disponíveis. Use List[str] para arrays, Optional[bool] para flags, e sempre forneça valores default apropriados.",
      
      "error_handling": "Implemente try/catch em todas as operações de API externa. Para Firecrawl, capture ConnectionError e RateLimitError. Para OpenAI, trate APIError e RateLimitError adequadamente."
    }
  },
  
  "data_analysis": {
    "description": "Prompts para análise e processamento de dados",
    "prompts": {
      "content_extraction": "Ao extrair informações de conteúdo web, foque em dados estruturados: preços, tecnologias, APIs, integrações. Use regex para extrair padrões específicos como URLs, emails, versões.",
      
      "pricing_analysis": "Para análise de preços, categorize em: 'Gratuito', 'Freemium', 'Pago', 'Empresarial', 'Assinatura'. Procure por indicadores como 'free tier', 'subscription', 'enterprise', '$', 'pricing'.",
      
      "tech_stack_detection": "Identifique tecnologias mencionadas: frameworks (React, Django), linguagens (Python, JavaScript), databases (PostgreSQL, MongoDB), cloud (AWS, Azure), APIs (REST, GraphQL).",
      
      "competitive_analysis": "Compare produtos em dimensões: preço, open source vs proprietário, API availability, language support, integration capabilities, developer experience."
    }
  },
  
  "api_integration": {
    "description": "Prompts para integração com APIs",
    "prompts": {
      "openai_usage": "Use ChatOpenAI com temperature=0 para consistência. Para structured output, use with_structured_output(). Implemente retry logic e exponential backoff para rate limits.",
      
      "environment_vars": "Sempre use python-dotenv para carregar variáveis. Valide se as chaves de API estão presentes antes de inicializar clientes. Use .env.example para documentar variáveis necessárias.",
      
      "async_patterns": "Para operações assíncronas, use asyncio.run() no main. Implemente context managers (async with) para recursos que precisam cleanup. Use asyncio.gather() para operações paralelas.",
      
      "rate_limiting": "Implemente rate limiting para APIs externas. Use asyncio.sleep() entre requests. Para Firecrawl, respeite limits de concurrent requests."
    }
  }
}