from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()

def main():
    workflow = Workflow()
    print("Agente de Pesquisa")

    while True:
        query = input("\n Consulta: ").strip()
        if query.lower() in {"Fui!", "Sair"}:
            break

        if query:
            result = workflow.run(query)
            print(f"\n Resultados para: {query}")
            print("=" * 60)

            for i, company in enumerate(result.companies, 1):
                print(f"\n{i}. 🏢 {company.name}")
                print(f"   🌐 Website: {company.website}")
                print(f"   💰 Valores: {company.pricing_model}")
                print(f"   📖 Open Source: {company.is_open_source}")

                if company.tech_stack:
                    print(f"   🛠️  Tecnologia: {', '.join(company.tech_stack[:5])}")

                if company.language_support:
                    print(
                        f"   💻 Suporte: {', '.join(company.language_support[:5])}"
                    )

                if company.api_available is not None:
                    api_status = (
                        "✅ Disponível" if company.api_available else "❌ Não disponível"
                    )
                    print(f"   🔌 API: {api_status}")

                if company.integration_capabilities:
                    print(
                        f"   🔗 Integrações: {', '.join(company.integration_capabilities[:4])}"
                    )

                if company.description and company.description != "Falhou":
                    print(f"   📝 Descrição: {company.description}")

                print()

            if result.analysis:
                print("Recomendações: ")
                print("-" * 40)
                print(result.analysis)


if __name__ == "__main__":
    main()
