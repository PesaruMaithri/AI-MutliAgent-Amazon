
from agents.industry_research_agent import IndustryResearchAgent
from agents.usecase_generation_agent import UseCaseGenerationAgent
from agents.resource_collection_agent import ResourceCollectionAgent

def main(company_name):
    research_agent = IndustryResearchAgent(company_name)
    industry_info = research_agent.research_industry()
    print(f"Industry Info: {industry_info}\n")

    usecase_agent = UseCaseGenerationAgent(industry_info)
    use_cases = usecase_agent.generate_use_cases()
    print(f"Generated Use Cases: {use_cases}\n")

    resource_agent = ResourceCollectionAgent(use_cases)
    resources = resource_agent.collect_resources()
    print(f"Collected Resources: {resources}\n")

    return use_cases, resources

if __name__ == "__main__":
    main("Amazon")
