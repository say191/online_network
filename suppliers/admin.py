from django.contrib import admin
from django.utils.html import format_html
from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'level', 'country', 'city', 'debt', 'created_at', 'supplier_link')
    list_filter = ('city', 'country')
    search_fields = ('name', )
    actions = ['clean_debt']

    def clean_debt(self, request, queryset):
        """Function for cleaning the debt"""
        queryset.update(debt=0)
    clean_debt.short_description = "Clean the debt"

    def supplier_link(self, obj):
        """Function for displaying supplier link"""
        supplier = obj.supplier
        if supplier:
            return format_html('<a href="/admin/suppliers/supplier/{}/change/">{}</a>', supplier.pk, supplier.title)
        else:
            return None

    supplier_link.allow_tags = True
    supplier_link.short_description = 'supplier'
