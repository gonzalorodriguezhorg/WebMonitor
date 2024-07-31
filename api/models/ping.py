from typing import Optional
from pydantic import BaseModel, Field, AwareDatetime, TypeAdapter
DT = AwareDatetime
TA= TypeAdapter(DT)

class Ping(BaseModel):
    client: int
    hostname: str
    response : bool
    date_time : Optional[str] | None = Field(default=None, title="Datetime")
    #date_time : Optional[datetime] | None = Field(default=None, title="Datetime")
    #Si un campo es opcional, es decir que puede ser pasado a la API o no, se debe de especificar un dato por default
    reason: Optional[str] | None = Field(default=None, title="Reason of the ping result")
    rtt_max_avg: Optional[float] | None = Field (default=None, title="Round Trip Time Max Avg")
    rtt_min_ms: Optional[float] | None = Field (default=None, title="Min Round Trip Time in ms")
    rtt_max: Optional[float] | None = Field (default=None, title="Max Round Trip Time")
    rtt_min: Optional[float] | None = Field (default=None, title="Min Round Trip Time")
    rtt_max_ms: Optional[float] | None = Field (default=None, title="Max Round Trip Time in  ms")
    packets_sent: Optional[int] | None = Field (default=None, title="Packets sent")
    packets_received: Optional[int] | None = Field (default=None, title="Packets received")
    
