
import wikipedia

class IndustryResearchAgent:
    def __init__(self, company_name):
        self.company_name = company_name
    
    def research_industry(self):
        try:
            summary = wikipedia.summary(self.company_name, sentences=5)
            return summary
        except Exception as e:
            return f"Could not fetch industry info: {e}"
