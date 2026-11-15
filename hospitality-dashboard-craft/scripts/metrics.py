"""Reference arithmetic for fixture testing; policies are illustrative, not universal industry contracts."""
def safe_div(numerator, denominator):
    return None if denominator is None or denominator <= 0 else numerator / denominator

def metrics(physical, ooo, sold, recognized_revenue):
    eligible = physical - ooo
    if eligible < 0 or sold < 0 or sold > eligible:
        raise ValueError("Invalid inventory basis or sold rooms")
    occ = safe_div(sold, eligible)
    adr = safe_div(recognized_revenue, sold)
    revpar = safe_div(recognized_revenue, eligible)
    return {"sellableRooms":eligible,"occupancyRate":None if occ is None else occ*100,"adr":adr,"revpar":revpar}

def net_after_acquisition(recognized_revenue, costs):
    result = recognized_revenue - sum(costs.values())
    return {"totalAcquisitionCosts":sum(costs.values()),"roomRevenueAfterAcquisition":result,"retainedPercent":None if recognized_revenue <= 0 else result/recognized_revenue*100}

def revpar_effects(adr0,occ0,adr1,occ1):
    # Occupancy inputs are fractions 0..1. Symmetric exact decomposition.
    return {"adrEffect":(adr1-adr0)*(occ0+occ1)/2,"occupancyEffect":(occ1-occ0)*(adr0+adr1)/2,"change":adr1*occ1-adr0*occ0}

def pace(current, baseline):
    val=safe_div(current-baseline,baseline)
    return None if val is None else val*100
