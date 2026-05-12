from .base_agent import BaseAgent
from .audit import AUDIT_LOGS

class AdminAgent(BaseAgent):
    """
    The agent responsible for assisting administrators with managing the system.
    """

    def get_persona(self) -> str:
        """
        Returns the persona of the agent.
        """
        return "Admin"

    def get_tools(self) -> list:
        """
        Returns the list of tools available to the agent.
        """
        self.tools = ["query_audit_logs", "manage_roles", "troubleshoot_flow"]
        return self.tools

    def query_audit_logs(self, limit: int = 5) -> list:
        """
        Retrieves the latest audit logs.
        """
        return AUDIT_LOGS[:limit]

    def process_request(self, query: str) -> str:
        """
        Processes a user query and returns a response.
        """
        query_lower = query.lower()
        if "audit" in query_lower or "logs" in query_lower:
            logs = self.query_audit_logs()
            response = "Latest audit logs:\n"
            for log in logs:
                response += f"- [{log['timestamp']}] {log['user']}: {log['action']} - {log['details']}\n"
            return response

        if "troubleshoot" in query_lower:
            return "To troubleshoot a flow, please provide the Flow Run ID. I can then check the execution logs in Dataverse for you."

        return f"The Admin Agent is processing your query: '{query}'. I can help you manage roles and audit system activity. Try 'show me the audit logs'."
