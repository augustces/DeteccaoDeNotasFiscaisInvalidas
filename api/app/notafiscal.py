from pydantic import BaseModel

class NotaFiscal(BaseModel):
    id_supplier: int
    iss_retention: bool
    iss_tax_rate: float
    csll_tax_rate: float
    ir_tax_rate: float
    cofins_tax_rate: float
    pis_tax_rate: float
    opting_for_simples_nacional: bool
