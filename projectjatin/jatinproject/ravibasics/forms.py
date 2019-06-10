from django import forms
# from skimage.measure import label


class UploadFiles(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    file = forms.FileField()
 