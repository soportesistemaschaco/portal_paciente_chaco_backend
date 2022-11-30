from typing import Dict

from app.gear.hcd_chaco.hcd_impl import HSIImplChaco
from app.routes.common import router_hsi


@router_hsi.get("/patient/turn", tags=["Patient"])
async def get_turnos(dni: str, dni_tipo: int, genero_id: int) -> Dict:
    hcd_impl = HSIImplChaco()
    return hcd_impl.get_turnos(dni, dni_tipo, genero_id)


@router_hsi.get("/patient/clinichistory", tags=["Patient"])
async def get_hc(dni: str, dni_tipo: int, genero_id: int) -> Dict:
    hcd_impl = HSIImplChaco()
    return hcd_impl.get_hc(dni, dni_tipo, genero_id)


@router_hsi.get("/patient/genders", tags=["Patient"])
async def get_genders() -> Dict:
    hcd_impl = HSIImplChaco()
    return hcd_impl.get_genders()


@router_hsi.get("/patient/documenttype", tags=["Patient"])
async def get_documents_type() -> Dict:
    hcd_impl = HSIImplChaco()
    return hcd_impl.get_documents_type()
