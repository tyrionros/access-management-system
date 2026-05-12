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
    from .requestor_agent import RequestorAgent
    from .approver_agent import ApproverAgent
    from .admin_agent import AdminAgent

    # Initialize orchestrator and register agents
    orchestrator = AgentOrchestrator()
    orchestrator.register_agent(RequestorAgent())
    orchestrator.register_agent(ApproverAgent())
    orchestrator.register_agent(AdminAgent())

    # Route requests
    print("--- Requestor Agent ---")
    print(orchestrator.route_request("Requestor", "find roles for sales"))

    print("\n--- Approver Agent ---")
    print(orchestrator.route_request("Approver", "view history for Priya"))

    print("\n--- Admin Agent ---")
    print(orchestrator.route_request("Admin", "show me the audit logs"))
