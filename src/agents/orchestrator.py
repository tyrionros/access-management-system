from typing import Dict, Type
from .base_agent import BaseAgent

class AgentOrchestrator:
    """
    Manages and orchestrates different specialized agents.
    """

    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        """
        Registers a new agent with the orchestrator.
        """
        persona = agent.get_persona()
        if persona in self.agents:
            raise ValueError(f"Agent with persona '{persona}' is already registered.")
        self.agents[persona] = agent
        print(f"Agent '{persona}' registered.")

    def get_agent(self, persona: str) -> BaseAgent:
        """
        Retrieves a registered agent by its persona.
        """
        agent = self.agents.get(persona)
        if not agent:
            raise ValueError(f"No agent found for persona '{persona}'.")
        return agent

    def route_request(self, persona: str, query: str) -> str:
        """
        Routes a request to the appropriate agent based on the persona.
        """
        agent = self.get_agent(persona)
        return agent.process_request(query)

# Example usage (can be removed later)
if __name__ == '__main__':
    # This is a placeholder for how the orchestrator might be used.
    # In a real scenario, agents would be loaded dynamically.
    
    # Dummy agent implementations for demonstration
    class RequestorAgent(BaseAgent):
        def get_persona(self) -> str:
            return "Requestor"
        def get_tools(self) -> list:
            return ["search_roles", "request_access"]
        def process_request(self, query: str) -> str:
            return f"Requestor Agent processing: {query}"

    class ApproverAgent(BaseAgent):
        def get_persona(self) -> str:
            return "Approver"
        def get_tools(self) -> list:
            return ["summarize_request", "view_history"]
        def process_request(self, query: str) -> str:
            return f"Approver Agent processing: {query}"

    # Initialize orchestrator and register agents
    orchestrator = AgentOrchestrator()
    orchestrator.register_agent(RequestorAgent())
    orchestrator.register_agent(ApproverAgent())

    # Route requests
    requestor_response = orchestrator.route_request("Requestor", "I need access to the sales app.")
    print(requestor_response)

    approver_response = orchestrator.route_request("Approver", "Summarize this request for me.")
    print(approver_response)
