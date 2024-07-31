from typing import Optional
from pydantic import BaseModel, Field, AwareDatetime, TypeAdapter
DT = AwareDatetime
TA= TypeAdapter(DT)

class adns(BaseModel):
    client: int
    domain: str
    response : bool
    date_time : Optional[str] | None = Field(default=None, title="Datetime")
    dns_server : str
    reason: Optional[str] | None = Field(default=None, title="Reason of the lookup result")
    a_records : Optional[list] | None = Field(default=None, title="A records for domain")
    
class mxdns(BaseModel):
    client: int
    domain: str
    response : bool
    date_time : Optional[str] | None = Field(default=None, title="Datetime")
    dns_server : str
    reason: Optional[str] | None = Field(default=None, title="Reason of the lookup result")
    mx_records : Optional[dict] | None = Field(default=None, title="MX record for domain")
    
class nsdns(BaseModel):
    client: int
    domain: str
    response : bool
    date_time : Optional[str] | None = Field(default=None, title="Datetime")
    dns_server : str
    reason: Optional[str] | None = Field(default=None, title="Reason of the lookup result")
    ns_records : Optional[list] | None = Field(default=None, title="NS records for domain")
    
class soadns(BaseModel):
    client: int
    domain: str
    response : bool
    date_time : Optional[str] | None = Field(default=None, title="Datetime")
    dns_server : str
    reason: Optional[str] | None = Field(default=None, title="Reason of the lookup result")
    soa_records : Optional[dict] | None = Field(default=None, title="SOA record for domain")
    
class txtdns(BaseModel):
    client: int
    domain: str
    response : bool
    date_time : Optional[str] | None = Field(default=None, title="Datetime")
    dns_server : str
    reason: Optional[str] | None = Field(default=None, title="Reason of the lookup result")
    txt_records : Optional[list] | None = Field(default=None, title="TXT record for domain")