from rest_framework import serializers
from suppliers.models import Supplier
from suppliers.validators import TypeAndSupplierValidator, SupplierAndDebtValidator, SupplierValidator


class SupplierSerializer(serializers.ModelSerializer):
    """Serializer for supplier's views"""
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('level', )
        validators = [TypeAndSupplierValidator(field1='type', field2='supplier'),
                      SupplierAndDebtValidator(field1='supplier', field2='debt'),
                      SupplierValidator(field='supplier')]

    def update(self, instance, validated_data):
        """Redefining the update function to exclude the ability to edit the debt field"""
        if 'debt' in validated_data:
            validated_data.pop('debt')
        return super().update(instance, validated_data)
