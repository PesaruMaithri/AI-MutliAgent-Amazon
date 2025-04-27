
class UseCaseGenerationAgent:
    def __init__(self, industry_info):
        self.industry_info = industry_info
    
    def generate_use_cases(self):
        if "retail" in self.industry_info.lower() or "e-commerce" in self.industry_info.lower():
            return [
                "Customer Behavior Prediction",
                "Inventory Demand Forecasting",
                "Delivery Time Prediction",
                "AI Chatbots for Customer Support",
                "Document Summarization for AWS Docs"
            ]
        else:
            return ["General AI Process Automation", "Customer Support Chatbots"]
