import pytest

from src.manager import Manager
from src.models import Parameters, ApartmentSettlement, TenantSettlement, Tenant
from src.models import Bill

def test_checking_tenants_payments():
    manager = Manager(Parameters())
    
    apartment_settlement = manager.get_settlement('apart-polanka', 2025, 1)
    assert isinstance(apartment_settlement, ApartmentSettlement)
    assert apartment_settlement.apartment == 'apart-polanka'
    assert apartment_settlement.month == 1
    assert apartment_settlement.year == 2025
    assert apartment_settlement.total_due_pln == 910.0
    
def test_checking_debtors():
    manager = Manager(Parameters())
    
    tenant_settlement = manager.get_debtors('apart-polanka', 2025, 1)
    assert isinstance(tenant_settlement, TenantSettlement)
    assert tenant_settlement.apartment_settlement == 'apart-polanka'
    assert tenant_settlement.month == 1
    assert tenant_settlement.year == 2025

def test_checking_deposit():
    manager = Manager(Parameters())
    deposit_settlement = manager.check_deposits()
    assert isinstance(deposit_settlement, Bill)
    assert deposit_settlement.amount_pln == 1000
    assert deposit_settlement.amount_pln == 3000
    assert isinstance(deposit_settlement, Tenant)
    assert deposit_settlement.rent_pln == 4000