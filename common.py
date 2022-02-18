import csv

from django.contrib.admin import ModelAdmin
from django.http import HttpResponse

class ExportMixin():

    def download_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response


    download_csv.short_description = "Download CSV"


class DefaultAdmin(ModelAdmin, ExportMixin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.list_filter = self.list_display
        self.search_fields = self.list_display
        # self.list_editable = [field.name for field in model._meta.fields if field.name != 'id']
        self.actions = ['download_csv']
        self.list_select_related = True
        super().__init__(model, admin_site)



