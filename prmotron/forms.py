import npyscreen
import config


class PRForm(npyscreen.FormMultiPage):
    def create(self):
        self.test_widget = self.add(npyscreen.TitleText,
                                    name='TEST',
                                    value=self.parentApp.pullrequest.full_name)

class ConfigForm(npyscreen.ActionFormMinimal):
    options = [
        {
            'key': 'username',
            'display': 'GitHub User'
        },
        {
            'key': 'token',
            'display': 'GitHub Token'
        },
        {
            'key': 'api_path',
            'display': 'API Root'
        }
    ]

    def on_cancel(self):
        self.parentApp.setNextForm('MAIN')

    def on_ok(self):
        new_options = {}
        for option in self.options:
            control = option['control']
            new_options[option['key']] = control.value
        config.Config().save_config(new_options)
        import ipdb; ipdb.set_trace()
        self.parentApp.setNextForm('MAIN')

    def create(self):
        for option in self.options:
            widget = npyscreen.TitleText

            if self.parentApp.config.has_key(option['key']):
                default_value = self.parentApp.config[option['key']]
            else:
                default_value = ''
            option['control'] = self.add(widget,
                                         name=option['display'],
                                         value=default_value)
