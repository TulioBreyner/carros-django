from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    '''
    Funções que começam com clean_ são executadas quando is_valid() é chamado na view
    '''
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor mínimo deve ser R$ 10.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1886:
            self.add_error('factory_year', 'Antes de 1886 não existiam carros')
        return factory_year