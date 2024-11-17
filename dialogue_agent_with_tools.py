from typing import List, Optional

class DialogueAgentWithTools:
    def __init__(self, name: str, system_message: str, model: str = "gpt-3.5-turbo", tools: Optional[List] = None):
        self.name = name
        self.system_message = system_message
        self.model = model
        self.tools = tools or []
        self.message_history = []
        self.xagent_enabled = True
        
    def _format_xagent_message(self, message: str) -> str:
        """Format message for XAgent processing"""
        return f"XAgent({self.name}): {message}"
    
    async def send(self, message: str) -> str:
        """Enhanced send method with XAgent support"""
        if self.xagent_enabled:
            formatted_message = self._format_xagent_message(message)
            response = self._process_with_xagent(formatted_message)
        else:
            response = message
            
        self.message_history.append({"role": "user", "content": message})
        self.message_history.append({"role": "assistant", "content": response})
        return response
        
    def _process_with_xagent(self, message: str) -> str:
        """Local XAgent processing simulation"""
        processed_message = f"Processed by XAgent: {message}"
        return processed_message