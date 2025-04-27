
class ResourceCollectionAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases
    
    def collect_resources(self):
        dataset_links = {
            "Customer Behavior Prediction": "https://www.kaggle.com/datasets/carrie1/ecommerce-data",
            "Inventory Demand Forecasting": "https://www.kaggle.com/datasets/snanthan89/walmart-sales-forecasting",
            "Delivery Time Prediction": "https://www.kaggle.com/datasets/prachi13/customer-analytics",
            "AI Chatbots for Customer Support": "https://www.kaggle.com/datasets/saikrishna03/customer-support-on-twitter",
            "Document Summarization for AWS Docs": "https://huggingface.co/datasets/ccdv/arxiv-summarization"
        }
        resources = []
        for case in self.use_cases:
            if case in dataset_links:
                resources.append(dataset_links[case])
        return resources
