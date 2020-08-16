from django.shortcuts import render
from .form import numForm


def prediction(request):
    if request.method == 'POST':
        form = numForm(request.POST)
        if form.is_valid():
            n0 = int(form.cleaned_data['sun'])
            n1 = int(form.cleaned_data['ma'])
            n2 = int(form.cleaned_data['mp'])
            n3 = int(form.cleaned_data['tua'])
            n4 = int(form.cleaned_data['tup'])
            n5 = int(form.cleaned_data['wa'])
            n6 = int(form.cleaned_data['wp'])
            n7 = int(form.cleaned_data['tha'])
            n8 = int(form.cleaned_data['thp'])
            n9 = int(form.cleaned_data['fa'])
            n10 = int(form.cleaned_data['fp'])
            n11 = int(form.cleaned_data['sa'])
            n12 = int(form.cleaned_data['sp'])
            if 0.4 < n1 / n0 < 0.59:
                ans = '四期型です'
            elif 0.8 < n1 / n0 < 0.849:
                ans = '四期型です'
            elif 0.6 < n1 / n0 < 0.79:
                if n1 - n2 == 0:
                    ans = '波型確定です'
                elif n2 > n3:
                    ans = '波型確定です'
                elif n2 < n3:
                    if n3 / n0 <= 0.9:
                        ans = '波型確定です'
                    else:
                        if n4 / n0 <= 0.9:
                            ans = 'K 波型確定です'
                        else:
                            if n5 / n0 < 2:
                                ans = '四期型確定です'
                            else:
                                ans = '三期型確定です'
            elif 0.85 < n1 / n0 < 0.89:
                if n2 - n1 >= 1:
                    if n3 / n0 <= 2:
                        ans = '四期型確定です'
                    else:
                        ans = '三期型確定です'
                else:
                    if 0.9 <= n3 / n0 <= 1.4:
                        ans = '四期型確定です'
                    elif 1.4 < n3 / n0:
                        ans = '三期型確定です'
                    else:
                        if n3 < n4:
                            if 0.9 < n4 / n0 < 1.4:
                                ans = '四期型確定です'
                            else:
                                ans = '三期型確定です'
                        else:
                            if n4 < n5:
                                if 0. < n5 / n0 < 1.4:
                                    ans = '四期型確定です'
                                else:
                                    ans = '三期型確定です'
                            else:
                                if n5 < n6:
                                    if 0.9 <= n6 / n0 < 1.4:
                                        ans = '四期型確定です'
                                    else:
                                        ans = '三期型確定です'
                                else:
                                    if n6 < n7:
                                        if 0.9 < n7 / n0 < 1.4:
                                            ans = '四期型確定です'
                                        else:
                                            ans = '三期型確定です'
                                    else:
                                        if n7 < n8:
                                            if 0.9 < n8 / n0 < 1.4:
                                                ans = '四期型確定です'
                                            else:
                                                ans = '三期型確定です'
                                        else:
                                            ans = 'ジリ貧型確定です'
            elif 0.9 < n1 / n0 < 1.4:
                if 0.4 < n2 / n0 < 0.8:
                    ans = '波型確定です'
                else:
                    if 0.4 < n3 / n0 < 1.39:
                        ans = '波型確定です'
                    else:
                        ans = '四期型確定です'
            else:
                ans = 'データが足りません'
        else:
            ans = 'データが足りません'
    else:
        form = numForm()
        ans = ""
    return render(request, 'prediction/prediction.html', {'form': form, 'ans': ans})
