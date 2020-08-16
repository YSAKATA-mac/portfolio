from django import forms


class numForm(forms.Form):
    sun = forms.DecimalField(label='日曜の買値', initial=0, required=True)
    ma = forms.DecimalField(label='月曜午前', initial=0, required=True)
    mp = forms.DecimalField(label='月曜午後', initial=0, required=True)
    tua = forms.DecimalField(label='火曜午前', initial=0, required=True)
    tup = forms.DecimalField(label='火曜午後', initial=0, required=True)
    wa = forms.DecimalField(label='水曜午前', initial=0, required=True)
    wp = forms.DecimalField(label='水曜午後', initial=0, required=True)
    tha = forms.DecimalField(label='木曜午前', initial=0, required=True)
    thp = forms.DecimalField(label='木曜午後', initial=0, required=True)
    fa = forms.DecimalField(label='金曜午前', initial=0, required=True)
    fp = forms.DecimalField(label='金曜午後', initial=0, required=True)
    sa = forms.DecimalField(label='土曜午前', initial=0, required=True)
    sp = forms.DecimalField(label='土曜午後', initial=0, required=True)
