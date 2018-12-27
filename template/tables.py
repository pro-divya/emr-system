import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from template.models import TemplateInstruction


class TemplateTable(tables.Table):
    template_title = tables.Column(verbose_name='Title', accessor="template_title")
    btn_action = tables.Column(empty_values=(), verbose_name='')

    class Meta:
        attrs = {
            'class': 'table table-striped table-bordered table-hover',
            'id': 'templatesTable'
        }
        model = TemplateInstruction
        fields = ('template_title', 'description', 'btn_action')
        template_name = 'django_tables2/semantic.html'

    def render_btn_action(self, record):
        return format_html(
            "<a href='" + reverse('template:change_template', args=[record.pk]) +\
            "' id='changeBtn-" + str(record.pk) + "' class='btn btn-primary'>Change</a>\
            <a href='" + reverse('template:remove_template', args=[record.pk]) +\
            "' id='removeBtn-" + str(record.pk) + "' class='btn btn-danger'>Remove</a>"
        )
