def calculate_eui(energy_use, floor_area):
    """Calculate Energy Use Intensity (EUI) in kWh/m²
    energy_use: in kWh
    floor_area: in m²
    """
    eui = energy_use / floor_area
    return eui
