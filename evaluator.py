from evaluation_metrics import FaithfulnessEvaluator, RelevancyEvaluator, ContextualAccuracyEvaluator, CompletenessEvaluator, LatencyEvaluator


class LLMEvaluator:
    def __init__(self, model):
        self.model = model
        self.results = {}

        # Initialize metric evaluators
        self.faithfulness_evaluator = FaithfulnessEvaluator()
        self.relevancy_evaluator = RelevancyEvaluator()
        self.contextual_accuracy_evaluator = ContextualAccuracyEvaluator()
        self.completeness_evaluator = CompletenessEvaluator()
        self.latency_evaluator = LatencyEvaluator()

    def evaluate_faithfulness(self, claims, reference_nodes):
        faithfulness, hallucination = self.faithfulness_evaluator.calculate_faithfulness(claims, reference_nodes)
        self.results['faithfulness'] = faithfulness
        self.results['hallucination'] = hallucination
        return faithfulness, hallucination

    def evaluate_relevancy(self, output_sentences, input_query):
        relevancy = self.relevancy_evaluator.calculate_relevancy(output_sentences, input_query)
        self.results['relevancy'] = relevancy
        return relevancy

    def evaluate_contextual_accuracy(self, retrieved_nodes, user_query):
        accuracy = self.contextual_accuracy_evaluator.calculate_contextual_accuracy(retrieved_nodes, user_query)
        self.results['contextual_accuracy'] = accuracy
        return accuracy

    def evaluate_completeness(self, user_intentions, chatbot_responses):
        completeness = self.completeness_evaluator.calculate_completeness(user_intentions, chatbot_responses)
        self.results['completeness'] = completeness
        return completeness

    def evaluate_latency(self, user_query):
        response = self.latency_evaluator.generate_response(self.model, user_query)
        latency = self.latency_evaluator.calculate_latency()
        self.results['latency'] = latency
        return latency

    # Method to recall all evaluation metrics
    def get_evaluation_results(self):
        return self.results
