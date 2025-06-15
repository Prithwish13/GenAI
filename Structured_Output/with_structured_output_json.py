from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""I placed the order on March 28th and received the laptop the very next day—excellent delivery speed!

Now, about the laptop specs: it's a M4 MacBook Air with 16GB of RAM, 512GB SSD, and a 13-inch Midnight display. The performance is top-notch; it doesn’t feel like an Air at all. Apple has really nailed it with the M-series silicon chips.

The 13-inch screen is perfect for me—light and portable. You won’t feel like the screen is too small. I also own a Lenovo Legion with a 15.6-inch display, and I find the MacBook's display to be very impressive. Despite what some online comments say, I don’t notice any issues with the 60Hz refresh rate.

My main use case is coding—both web and app development. The MacBook performs flawlessly. Build times are very short, and Android Studio runs smoothly.

One thing to note: since it doesn’t have a fan, it can get warm when multiple apps are open. But overall, I highly recommend it without hesitation. I’ll provide an update after using it for a month""")

print(result)