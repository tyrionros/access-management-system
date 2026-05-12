from .base_agent import BaseAgent
from .history import REQUEST_HISTORY

class ApproverAgent(BaseAgent):
    """
    The agent responsible for assisting managers with approving access requests.
    """

    def get_persona(self) -> str:
        """
        Returns the persona of the agent.
        """
        return "Approver"

    def get_tools(self) -> list:
        """
        Returns the list of tools available to the agent.
        """
        self.tools = ["summarize_request", "view_history", "approve_request", "reject_request"]
        return self.tools

    def view_history(self, user_name: str) -> list:
        """
        Retrieves the request history for a specific user.
        """
        return [r for r in REQUEST_HISTORY if r["user"].lower() == user_name.lower()]

    def summarize_request(self, request_id: str) -> str:
        """
        Simulates summarizing a specific request.
        """
        # For simulation, we'll just return a hardcoded summary
        return f"Summary for Request {request_id}: User John Doe is requesting 'Salesperson' access to 'D365 Sales'. This is consistent with their current role in the Sales department."

    def process_request(self, query: str) -> str:
        """
        Processes a user query and returns a response.
        """
        query_lower = query.lower()
        if "history" in query_lower:
            # Extract user name (simple heuristic)
            parts = query_lower.split("for")
            user_name = parts[-1].strip() if len(parts) > 1 else "Priya"
            history = self.view_history(user_name)
            
            if not history:
                return f"No history found for user '{user_name}'."
            
            response = f"Access history for {user_name}:\n"
            for h in history:
                response += f"- {h['date']}: {h['role']} ({h['application']}) - {h['status']}\n"
            return response

        if "summarize" in query_lower:
            return self.summarize_request("REQ-123")

        return f"The Approver Agent is processing your query: '{query}'. I can help you by summarizing requests and providing user history. Try 'view history for Priya'."
