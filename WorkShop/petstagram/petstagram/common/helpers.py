class BootstrapFormMixin:
    fields = {}

    def _init_boostrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class DisabledFieldsFormMixin:
    disabled_fields = ()
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if name not in self.disabled_fields:
                continue
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'
