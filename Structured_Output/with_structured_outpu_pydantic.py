from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import  Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# class Review(TypedDict):
#     key_themes: Annotated[list[str], "Key themes or topics discussed in the review"]
#     summary: Annotated[str, "A brief summary of the review"]
#     pros: Annotated[Optional[list[str]], "Positive aspects or features of the product mentioned in the review"]
#     cons: Annotated[Optional[list[str]], "Negative aspects or features of the product mentioned in the review"]
#     sentiment: Annotated[Literal["pos", "neg"], "The overall sentiment of the review, e.g., positive, negative, neutral"]

class Review(BaseModel):
    key_themes: list[str] = Field(description="Key themes or topics discussed in the review")
    summary: str = Field(description="A brief summary of the review")
    pros: Optional[list[str]] = Field(None, description="Positive aspects or features of the product mentioned in the review")
    cons: Optional[list[str]] = Field(None, description="Negative aspects or features of the product mentioned in the review")
    sentiment: Literal["pos", "neg"] = Field(description="The overall sentiment of the review, e.g., positive, negative, neutral")

structured_model  = model.with_structured_output(Review)

result = structured_model.invoke("""I placed the order on March 28th and received the laptop the very next day—excellent delivery speed!

Now, about the laptop specs: it's a M4 MacBook Air with 16GB of RAM, 512GB SSD, and a 13-inch Midnight display. The performance is top-notch; it doesn’t feel like an Air at all. Apple has really nailed it with the M-series silicon chips.

The 13-inch screen is perfect for me—light and portable. You won’t feel like the screen is too small. I also own a Lenovo Legion with a 15.6-inch display, and I find the MacBook's display to be very impressive. Despite what some online comments say, I don’t notice any issues with the 60Hz refresh rate.

My main use case is coding—both web and app development. The MacBook performs flawlessly. Build times are very short, and Android Studio runs smoothly.

One thing to note: since it doesn’t have a fan, it can get warm when multiple apps are open. But overall, I highly recommend it without hesitation. I’ll provide an update after using it for a month""")

print(result)