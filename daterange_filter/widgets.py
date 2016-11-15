from django import forms


class AdminDateWidget(forms.DateInput):
    @property
    def media(self):
        # js = ["calendar.js", "admin/DateTimeShortcuts.js"]
        return forms.Media(js=["admin/js/calendar.js", "date_widget/js/DateTimeShortcuts.js"])

    def __init__(self, attrs=None, format=None):
        final_attrs = {
            'class': 'vDateField',
            'size': '10',
            # 'onchange': window.location.search = '?' + (value ? ('&' + name + '=' + encodeURI(value)) : '')
        }
        if attrs is not None:
            final_attrs.update(attrs)
        super(AdminDateWidget, self).__init__(attrs=final_attrs, format=format)
