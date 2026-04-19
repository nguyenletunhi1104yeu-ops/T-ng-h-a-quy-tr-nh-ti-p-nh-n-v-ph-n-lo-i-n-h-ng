# rule_engine.py
def assign_vehicle(label, weight_kg, distance_km):
    if label == 'Nhẹ':
        if weight_kg < 15 and distance_km < 10:
            return 'Xe máy'
        else:
            return 'Xe Tải Van'
    elif label == 'Nặng':
        if weight_kg <= 1500:
            return 'Xe tải 1.5 tấn'
        elif weight_kg <= 5000:
            return 'Xe tải 5 tấn'
        else:
            return 'Xe Đầu kéo / Container'
    return 'Chưa xác định'
