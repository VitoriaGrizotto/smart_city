from django import forms

class CSVUploadForm(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV")

class CSVUploadTemp(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Temperatura")

class CSVUploadUmidade(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Umidade")

class CSVUploadContador(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Contador")

class CSVUploadLuminosidade(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Luminosidade")
