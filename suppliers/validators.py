from rest_framework.serializers import ValidationError


class TypeAndSupplierValidator:
    """Validator for fields type and supplier"""
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        type = value.get(self.field1)
        supplier = value.get(self.field2)
        if type == 'FA' and supplier:
            raise ValidationError("A factory cannot have a supplier")
        if type in ['RN', 'IE'] and not supplier:
            raise ValidationError("Retail network or IP must have supplier")


class TypeAndDebtValidator:
    """Validator for fields type and debt"""
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        type = value.get(self.field1)
        debt = value.get(self.field2)
        if type == 'FA' and debt:
            raise ValidationError("A factory cannot have a debt")


class SupplierValidator:
    """Validator for field supplier"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        supplier = value.get(self.field)
        if supplier and supplier.level == 2:
            raise ValidationError("You cannot choose this supplier, because we have only 3 levels (0,1,2) but this supplier already have second level")
