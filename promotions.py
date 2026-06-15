class PromotionEngine:
    def __init__(self):
        self.promotions = []

    def add_promotion(self, name, discount_pct, min_quantity=1):
        self.promotions.append({
            "name": name,
            "discount_pct": discount_pct,
            "min_quantity": min_quantity
        })

    def get_best_promotion(self, cart):
        # BUG: expired promotions not filtered
        applicable = [p for p in self.promotions if cart.get_item_count() >= p["min_quantity"]]
        if not applicable:
            return None
        return max(applicable, key=lambda p: p["discount_pct"])
