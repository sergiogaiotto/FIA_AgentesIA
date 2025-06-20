{
  "development_modes": [
    {
      "name": "agent_development",
      "display_name": "🤖 Desenvolvimento de Agentes",
      "description": "Modo otimizado para criação de agentes de IA inteligentes",
      "settings": {
        "focus": "ai_agent_workflows",
        "code_style": "async_first",
        "error_handling": "comprehensive",
        "documentation": "detailed"
      },
      "features": {
        "auto_import": [
          "from langchain_openai import ChatOpenAI",
          "from langgraph.graph import StateGraph, END",
          "from pydantic import BaseModel, Field",
          "import asyncio",
          "from typing import List, Optional, Dict, Any"
        ],
        "templates": {
          "workflow_node": "async def ${node_name}_step(state: ${StateClass}) -> Dict[str, Any]:",
          "pydantic_model": "class ${ModelName}(BaseModel):\n    ${field_name}: ${field_type}",
          "api_call": "try:\n    result = await ${api_call}\n    return result\nexcept Exception as e:\n    logger.error(f'Error: {e}')\n    return fallback"
        },
        "prompt_engineering": true,
        "structured_output": true
      }
    },
    
    {
      "name": "web_scraping",
      "display_name": "🕷️ Web Scraping & Extração",
      "description": "Modo especializado para scraping e extração de dados web",
      "settings": {
        "focus": "data_extraction",
        "rate_limiting": "enabled",
        "error_recovery": "robust",
        "caching": "recommended"
      },
      "features": {
        "auto_import": [
          "from firecrawl import FirecrawlApp, ScrapeOptions",
          "import requests",
          "from bs4 import BeautifulSoup",
          "import time",
          "from urllib.parse import urljoin, urlparse"
        ],
        "templates": {
          "firecrawl_scrape": "result = self.app.scrape_url(\n    url,\n    formats=['markdown'],\n    scrape_options=ScrapeOptions(timeout=30)\n)",
          "rate_limit": "await asyncio.sleep(${delay})",
          "url_validation": "if not urlparse(url).scheme:\n    url = f'https://{url}'"
        },
        "best_practices": [
          "Sempre implementar rate limiting",
          "Usar User-Agent apropriado",
          "Respeitar robots.txt",
          "Implementar retry logic",
          "Validar URLs antes do scraping"
        ]
      }
    },
    
    {
      "name": "data_analysis", 
      "display_name": "📊 Análise de Dados",
      "description": "Modo para análise e processamento de dados extraídos",
      "settings": {
        "focus": "data_processing",
        "validation": "strict",
        "performance": "optimized",
        "visualization": "enabled"
      },
      "features": {
        "auto_import": [
          "import pandas as pd",
          "import numpy as np",
          "from typing import List, Dict, Optional",
          "import json",
          "import re"
        ],
        "templates": {
          "data_cleaning": "def clean_${data_type}(data: List[Dict]) -> List[Dict]:\n    cleaned = []\n    for item in data:\n        if ${validation_condition}:\n            cleaned.append(${transform_item})\n    return cleaned",
          "price_extraction": "price_match = re.search(r'\\$([0-9,]+(?:\\.[0-9]{2})?)', text)\nif price_match:\n    price = float(price_match.group(1).replace(',', ''))",
          "company_analysis": "analysis = {\n    'name': ${company_name},\n    'pricing_model': ${pricing_model},\n    'tech_stack': ${tech_stack},\n    'api_available': ${api_available}\n}"
        },
        "validation_patterns": {
          "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
          "url": "^https?://[^\\s/$.?#].[^\\s]*$",
          "price": "\\$?([0-9,]+(?:\\.[0-9]{2})?)",
          "version": "v?([0-9]+(?:\\.[0-9]+)*)"
        }
      }
    },
    
    {
      "name": "api_integration",
      "display_name": "🔌 Integração de APIs",
      "description": "Modo para trabalhar com APIs externas e integrações",
      "settings": {
        "focus": "api_reliability",
        "authentication": "secure",
        "rate_limiting": "automatic",
        "monitoring": "enabled"
      },
      "features": {
        "auto_import": [
          "import httpx",
          "import os",
          "from dotenv import load_dotenv",
          "import asyncio",
          "from tenacity import retry, stop_after_attempt, wait_exponential"
        ],
        "templates": {
          "api_client": "class ${APIName}Client:\n    def __init__(self, api_key: str):\n        self.api_key = api_key\n        self.base_url = '${base_url}'\n        self.session = httpx.AsyncClient()",
          "retry_decorator": "@retry(\n    stop=stop_after_attempt(3),\n    wait=wait_exponential(multiplier=1, min=4, max=10)\n)",
          "env_validation": "api_key = os.getenv('${API_KEY_NAME}')\nif not api_key:\n    raise ValueError('${API_KEY_NAME} environment variable is required')"
        },
        "security_practices": [
          "Nunca hardcode API keys no código",
          "Use .env para variáveis sensíveis",
          "Implemente timeout adequado",
          "Valide responses antes de processar",
          "Log requests sem expor credenciais"
        ]
      }
    },
    
    {
      "name": "testing_debug",
      "display_name": "🐛 Testing & Debug",
      "description": "Modo para testes e debugging de agentes",
      "settings": {
        "focus": "testing_reliability",
        "coverage": "comprehensive",
        "mocking": "enabled",
        "logging": "verbose"
      },
      "features": {
        "auto_import": [
          "import pytest",
          "from unittest.mock import Mock, patch, AsyncMock",
          "import logging",
          "from pytest import fixture"
        ],
        "templates": {
          "async_test": "@pytest.mark.asyncio\nasync def test_${function_name}():\n    # Given\n    ${setup}\n    \n    # When\n    result = await ${function_call}\n    \n    # Then\n    assert ${assertion}",
          "mock_api": "@patch('${module}.${api_client}')\ndef test_${function}(mock_api):\n    mock_api.return_value = ${mock_response}\n    result = ${function_call}\n    assert result == ${expected}",
          "logger_setup": "import logging\nlogging.basicConfig(\n    level=logging.INFO,\n    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'\n)"
        },
        "test_scenarios": [
          "API timeout e rate limiting",
          "Dados malformados no scraping", 
          "Falhas de rede intermitentes",
          "Respostas inesperadas da LLM",
          "Validação de modelos Pydantic"
        ]
      }
    },
    
    {
      "name": "production_deploy",
      "display_name": "🚀 Produção & Deploy",
      "description": "Modo para preparação e deploy em produção",
      "settings": {
        "focus": "production_readiness",
        "performance": "optimized",
        "monitoring": "comprehensive",
        "security": "hardened"
      },
      "features": {
        "auto_import": [
          "import uvicorn",
          "from fastapi import FastAPI, HTTPException",
          "import prometheus_client",
          "from contextlib import asynccontextmanager"
        ],
        "templates": {
          "health_check": "@app.get('/health')\nasync def health_check():\n    return {\n        'status': 'healthy',\n        'timestamp': datetime.utcnow().isoformat()\n    }",
          "error_middleware": "async def error_handler(request, exc):\n    logger.error(f'Error processing {request.url}: {exc}')\n    return JSONResponse(\n        status_code=500,\n        content={'error': 'Internal server error'}\n    )",
          "metrics": "REQUEST_COUNT = prometheus_client.Counter(\n    'requests_total',\n    'Total requests',\n    ['method', 'endpoint']\n)"
        },
        "production_checklist": [
          "Configurar logging estruturado",
          "Implementar health checks",
          "Adicionar métricas de performance",
          "Configurar rate limiting",
          "Implementar graceful shutdown",
          "Adicionar middleware de segurança",
          "Configurar monitoramento de erros"
        ]
      }
    }
  ],
  
  "context_modes": {
    "research_assistant": {
      "description": "Assistente para pesquisa de produtos e ferramentas",
      "behavior": "Foque em encontrar, extrair e analisar informações sobre produtos, preços, tecnologias e alternativas. Priorize dados estruturados e comparações objetivas.",
      "output_format": "structured_analysis"
    },
    
    "code_reviewer": {
      "description": "Revisor de código para agentes de IA",
      "behavior": "Analise código Python focando em async/await, tratamento de erros, performance de APIs, e patterns de LangChain/LangGraph.",
      "output_format": "detailed_feedback"
    },
    
    "architecture_advisor": {
      "description": "Consultor de arquitetura para sistemas de IA",
      "behavior": "Forneça conselhos sobre estrutura de projetos, escolha de ferramentas, patterns de workflow, e integração de componentes.",
      "output_format": "architectural_guidance"
    }
  }
}