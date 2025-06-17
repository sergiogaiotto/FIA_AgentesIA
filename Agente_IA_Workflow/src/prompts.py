
class DeveloperToolsPrompts:
    # Tool extraction prompts
    TOOL_EXTRACTION_SYSTEM = """Você é um pesquisador de preços, promoções, ofertas e valores. Extraia nomes específicos de ferramentas, bibliotecas, plataformas ou serviços de artigos.
Concentre-se em produtos/ferramentas/soluções/serviços reais que consumidores demnonstrem interesse e podem usar."""

    @staticmethod
    def tool_extraction_user(query: str, content: str) -> str:
        return f"""Query: {query}
                Conteúdo do Artigo: {content}

                Extraia uma lista de nomes de produtos/ferramentas/soluções/serviços específicos mencionados neste conteúdo que sejam relevantes para "{query}".

                Rules:
                - Incluir apenas nomes de produtos reais, sem termos genéricos
                - Foco em ferramentas/soluções/serviços que os consumidores podem comprar, obter, assinar, usar e consumir diretamente
                - Incluir opções comerciais e de código aberto
                - Limitar às 5 resultados mais relevantes
                - Retornar apenas os nomes dos produtos/ferramentas/soluções/serviços, um por linha, sem descrições
                Formato de exemplo:
                Amazon
                MercadoLivre
                Picpay
                Nubank
                Microsoft
                IBM
                Carrefour
                Ifood
                OpenAI
                Groq
                """

    # Company/Tool analysis prompts
    TOOL_ANALYSIS_SYSTEM = """Você está analisando preços, promoções, ofertas e valores de produtos/ferramentas/soluções/serviços com base na categoria informada pelo usuário.
Concentre-se em extrair informações relevantes para consumidores de produtos/ferramentas/soluções/serviços.
Preste atenção especial nas condições, descontos, modelo comercial, pré-requisitos, tecnologia, APIs, SDKs e modos de utilização para compra, obtenção, assinatura, uso e consumo."""

    @staticmethod
    def tool_analysis_user(company_name: str, content: str) -> str:
        return f"""Empresa/Ferramenta: {company_name}
                Conteúdo do Website: {content[:2500]}

                Analise este conteúdo da perspectiva de um consumidor e forneça:
                - pricing_model: "Gratuito", "Freemium", "Pago", "Empresarial", "Assinatura" ou "Desconhecido"
                - is_open_source: verdadeiro se for de código aberto, falso se for proprietário, nulo se não estiver claro
                - tech_stack: tecnologia adotada para produtos/ferramentas/soluções/serviços oferecido
                - description: breve descrição de uma frase com foco no que esta produtos/ferramentas/soluções/serviços entrega para o consumidor
                - api_available: verdadeiro se API REST, GraphQL, SDK ou acesso programático forem mencionados
                - language_support: Lista de linguagens de programação explicitamente suportadas (ex.: Python, JavaScript, Go, etc.)
                - integration_capabilities: Lista de ferramentas/plataformas com as quais se integra (ex.: GitHub, VS Code, Docker, AWS, etc.)
                Foco em recursos relevantes para o consumidor, como produtos/ferramentas/soluções/serviços, bem como modos de uso, integrações com APIs, SDKs, suporte a idiomas, integrações e modos de utlização para compra, obtenção, assinatura, uso e consumo."""

    RECOMMENDATIONS_SYSTEM = """Você é um pesquisador sênior que fornece recomendações técnicas rápidas e concisas.
    Mantenha as respostas breves e práticas - no máximo 3 a 4 frases no total.."""

    @staticmethod
    def recommendations_user(query: str, company_data: str) -> str:
        return f"""Consumer Query: {query}
                Ferramentas/Tecnologias Analisadas: {company_data}

                Forneça uma breve recomendação (máximo de 3 a 4 frases) abrangendo:
                - Qual ferramenta é a melhor e por quê
                - Principais considerações sobre custo/preço
                - Principal vantagem técnica
                - A melhor oferta, preços e condições

                Não são necessárias longas explicações."""
