from typing import Dict

from app.gear.sumar_chaco.sumar_impl import SumarImplChaco
from app.routes.common import router_sumar


@router_sumar.get("/me", tags=["SUMAR"])
async def get_me() -> Dict:
    sumar_impl = SumarImplChaco()
    return sumar_impl.get_me()


@router_sumar.get("/prestaciones", tags=["SUMAR"])
async def get_prestaciones(dni: str) -> Dict:
    sumar_impl = SumarImplChaco()
    return sumar_impl.get_prestaciones(dni)


@router_sumar.get("efectores", tags=["SUMAR"])
async def get_efectores() -> Dict:
    sumar_impl = SumarImplChaco()
    return sumar_impl.get_efectores()
