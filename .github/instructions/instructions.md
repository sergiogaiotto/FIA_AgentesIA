---
applyTo: '**'
---
# Instruções para Desenvolvimento de Agentes de IA

## Contexto do Projeto
Você está trabalhando em projetos de Agentes de IA que utilizam:
- **LangChain/LangGraph** para workflows inteligentes
- **Firecrawl** para web scraping e extração de dados
- **OpenAI GPT-4** para processamento de linguagem natural
- **Pydantic** para validação e estruturação de dados
- **MCP (Model Context Protocol)** para integração de ferramentas

## Diretrizes Gerais

### 🎯 Foco em Qualidade
- Sempre priorize código limpo, legível e bem documentado
- Use type hints em todas as funções e classes
- Implemente tratamento de erros robusto
- Escreva testes unitários quando necessário

### 🔧 Padrões Técnicos

#### Estrutura de Projeto
```
projeto/
├── .env                 # Variáveis de ambiente
├── main.py             # Ponto de entrada
├── requirements.txt    # Dependências
└── src/
    ├── __init__.py
    ├── workflow.py     # Lógica principal
    ├── models.py       # Modelos Pydantic
    ├── prompts.py      # Templates de prompts
    └── services/       # Integrações externas
```

#### Modelos Pydantic
- Use tipos Optional para campos que podem estar ausentes
- Forneça valores default apropriados
- Documente campos complexos com Field(description="...")
- Valide dados de entrada com validators personalizados

#### Workflows LangGraph
- Separe cada etapa em nodes distintos
- Use StateGraph com modelos Pydantic como state
- Implemente edge conditions quando necessário
- Adicione logging para debug do fluxo

#### Integração APIs
- Sempre use variáveis de ambiente para chaves de API
- Implemente retry logic com exponential backoff
- Use async/await consistentemente
- Valide responses antes de processar

### 🛠️ Ferramentas Específicas

#### Firecrawl
- Use ScrapeOptions com formats=['markdown'] para melhor extração
- Limite search results (3-5) para performance
- Implemente timeout adequado para scraping
- Cache results quando possível

#### OpenAI
- Use temperature=0 para consistência em análises
- Para structured output, sempre use with_structured_output()
- Implemente token counting para controle de custos
- Use system messages para definir comportamento

#### MCP
- Configure server_params com env vars corretas
- Use ClientSession com context managers
- Implemente initialize() antes de usar tools
- Trate disconnections gracefully

### 📝 Convenções de Código

#### Nomenclatura
- Classes: `PascalCase` (ex: `CompanyAnalysis`)
- Funções/variáveis: `snake_case` (ex: `extract_tools`)
- Constantes: `UPPER_CASE` (ex: `MAX_RETRIES`)
- Arquivos: `snake_case.py`

#### Imports
```python
# Standard library
import os
import asyncio

# Third-party
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

# Local imports
from .models import ResearchState
from .services.firecrawl import FirecrawlService
```

#### Error Handling
```python
try:
    result = await api_call()
    return result
except SpecificError as e:
    logger.error(f"Specific error: {e}")
    return fallback_value
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

### 🔍 Debugging e Logging
- Use logging em vez de print() para debug
- Implemente progress indicators para operações longas
- Log requests/responses de APIs (sem expor keys)
- Use structured logging para análise posterior

### 🚀 Performance
- Use asyncio.gather() para operações paralelas
- Implemente caching para dados que não mudam
- Limite concurrent requests para APIs externas
- Use pagination quando disponível

### 🔒 Segurança
- Nunca commite chaves de API
- Use .env para todas as configurações sensíveis
- Valide e sanitize inputs de usuário
- Implemente rate limiting adequado

### 📊 Análise de Dados
- Estruture dados em modelos Pydantic consistentes
- Use type hints para clareza
- Implemente validação de dados robusta
- Forneça fallbacks para dados ausentes

## Exemplos de Uso

### Criando um Workflow
```python
from langgraph.graph import StateGraph
from .models import ResearchState

def create_workflow():
    graph = StateGraph(ResearchState)
    graph.add_node("extract", extract_step)
    graph.add_node("research", research_step)
    graph.add_edge("extract", "research")
    return graph.compile()
```

### Análise com LLM
```python
async def analyze_content(content: str) -> CompanyAnalysis:
    structured_llm = self.llm.with_structured_output(CompanyAnalysis)
    
    messages = [
        SystemMessage(content=ANALYSIS_PROMPT),
        HumanMessage(content=f"Analyze: {content}")
    ]
    
    return await structured_llm.ainvoke(messages)
```

### Scraping com Firecrawl
```python
def scrape_with_fallback(url: str) -> Optional[str]:
    try:
        result = self.firecrawl.scrape_url(
            url,
            formats=["markdown"],
            timeout=30
        )
        return result.markdown
    except Exception as e:
        logger.warning(f"Scraping failed for {url}: {e}")
        return None
```

## Checklist de Qualidade
- [ ] Type hints em todas as funções
- [ ] Tratamento de erros implementado
- [ ] Variáveis de ambiente documentadas
- [ ] Logs informativos adicionados
- [ ] Modelos Pydantic validados
- [ ] Async/await usado consistentemente
- [ ] Performance otimizada
- [ ] Testes básicos criados