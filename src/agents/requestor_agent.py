from .base_agent import BaseAgent
from .catalog import ROLES_CATALOG

class RequestorAgent(BaseAgent):
    """
    The agent responsible for assisting end-users with access requests.
    """

    def get_persona(self) -> str:
        """
        Returns the persona of the agent.
        """
        return "Requestor"

    def get_tools(self) -> list:
        """
        Returns the list of tools available to the agent.
        """
        self.tools = ["search_roles", "request_access"]
        return self.tools

    def search_roles(self, query: str) -> list:
        """
        Searches for roles in the catalog based on a query string.
        """
        query = query.lower()
        results = [
            role for role in ROLES_CATALOG
            if query in role["role"].lower() or query in role["application"].lower() or query in role["description"].lower()
        ]
        return results

    def process_request(self, query: str) -> str:
        """
        Processes a user query and returns a response.
        """
        query_lower = query.lower()
        # Simple simulation of intent detection and tool usage
        if any(word in query_lower for word in ["search", "find", "what roles", "list"]):
            # Extract keywords by removing command verbs and common stop words
            stop_words = ["search", "find", "for", "what", "roles", "available", "list", "show", "me"]
            words = query_lower.split()
            keywords = [w for w in words if w not in stop_words]
            search_query = " ".join(keywords) if keywords else query_lower

            results = self.search_roles(search_query)
            
            # If no results with stripped keywords, try with the original query (excluding "search/find")
            if not results and search_query != query_lower:
                search_query = query_lower.replace("search", "").replace("find", "").strip()
                results = self.search_roles(search_query)

            if not results:
                return f"I couldn't find any roles matching '{search_query}'. Can you try another keyword?"
            
            response = f"I found {len(results)} matching roles:\n"
            for r in results[:5]:  # Limit to 5 for brevity
                response += f"- {r['role']} (App: {r['application']}): {r['description']}\n"
            
            if len(results) > 5:
                response += "...and more."
            return response

        return f"The Requestor Agent is processing your query: '{query}'. I can help you find and request access to applications. For example, try 'find roles for sales'."
