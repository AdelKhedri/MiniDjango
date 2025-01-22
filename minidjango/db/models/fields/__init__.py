from ....utils.colors import Colors


class Field:
    def __init__(self, verbose_name = None, blank = False, default=None):
        self.verbose_name = verbose_name
        self.blank = blank
        self.default = default
        self._value = None
    
    def contribute_to_class(self, name):
        self.name = name

    def get_field_sql(self):
        name = self.name
        column_type = getattr(self, 'column_type')
        if column_type == 'VARCHAR':
            return f'"{name}" {column_type}({self.max_length})'
        else:
            return f'"{name}" {column_type}'

    def _check_default(self):
        default = getattr(self, 'default', None)
        column_type = self.column_type
        if default and isinstance(default, int) and column_type != 'INTEGER':
            raise ValueError('{}{}{}'.format(Colors.RED, 'default in IntegerField must be a number', Colors.RESET))
        if default and isinstance(default, str) and column_type != 'VARCHAR':
            raise ValueError('{}{}{}'.format(Colors.RED, 'default in CharField must be a string', Colors.RESET))

    def __get__(self, instance, owner):
        return getattr(self, '_value', self.default)

    def __set__(self, instance, value):
        if value:
            if self.column_type == 'VARCHAR' and len(value) > self.max_length:
                raise ValueError(f'value is greader than of {self.max_length}')
        self._value = value

    def __repr__(self):
        return self._value
    
    def __str__(self):
        return self._value


class CharField(Field):
    column_type = 'VARCHAR'

    def __init__(self, max_length, verbose_name=None, blank=False, default=None):
        super().__init__(verbose_name, blank, default)
        super()._check_default()
        self.max_length = max_length
        self.check()

    def check(self):
        required_attr = 'max_length'
        max_length = getattr(self, required_attr, None)
        has_error = False

        if max_length is None:
            has_error = True
            error_type = ValueError
            message = 'is not defained.'
        elif not isinstance(max_length, int):
            has_error = True
            error_type = ValueError
            message = 'must be integer'

        if has_error:
            raise error_type('{}{}{}{}{}'.format(Colors.BLUE, required_attr, Colors.RED, message, Colors.RESET))


class IntegerField(Field):
    column_type = 'INTEGER'

    def __init__(self, null=False, verbose_name=None, blank=False, default=None):
        super().__init__(verbose_name, blank, default)
        self.null = null
