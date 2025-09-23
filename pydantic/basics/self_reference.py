from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None
    
Comment.model_rebuild() # This is must if we are creating self referencing models

comment = Comment (
    id= 1,
    content= "First Comment",
    replies = [
        Comment(id=2, content="reply 1"),
        Comment(id=2, content="reply 1", replies=[
            Comment(id=3, content="reply 10")
            ]),
    ]
)

print(comment)
