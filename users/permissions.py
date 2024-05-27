from rest_framework.permissions import BasePermission


class IsOwnerForUser(BasePermission):
    """Permission for user's actions"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsCreatorForProduct(BasePermission):
    """Permission for product's creator"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsCreatorForSupplier(BasePermission):
    """Permission for supplier's creator"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
