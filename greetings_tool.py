from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class GreetingsInput(BaseModel):
    greetings: str = Field(..., description="Greeting message to be sent")


class GreetingsTool(BaseTool):
    """
    Greetings Tool
    """
    name: str = "Greetings Tool"
    args_schema: Type[BaseModel] = GreetingsInput
    description: str = "Sends a Greeting Message"


    def _execute(self, greetings: dict = None):
        from_name = self.get_tool_config('FROM')
    
        if not isinstance(greetings, dict):
            return f"Hello There!!\n{from_name}"

        greetings_message = greetings.get("greetings", "")
        composed_message = f"{greetings_message}\n{from_name}"
        return composed_message

    # def _execute(self, greetings: dict = None):
    #     from_name = self.get_tool_config('FROM')
    #     if type(greetings) != dict:
    #         return "Hello" + "\n" + from_name
    #     else:
    #         greetings_str = greetings["greetings"] + "\n" + from_name
    #         return greetings_str
                