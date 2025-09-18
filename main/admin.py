from django.contrib import admin
from .models import LeaveApplication

@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'leave_type', 'start_date', 'end_date', 'status', 'applied_on')
    list_filter = ('status', 'leave_type', 'applied_on')
    search_fields = ('student__username', 'reason')
    actions = ['approve_leaves', 'reject_leaves']

    def approve_leaves(self, request, queryset):
        queryset.update(status='APPROVED')
    approve_leaves.short_description = "Mark selected leaves as approved"

    def reject_leaves(self, request, queryset):
        queryset.update(status='REJECTED')
    reject_leaves.short_description = "Mark selected leaves as rejected"
