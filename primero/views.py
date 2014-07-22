from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render

def hello(request):
    v1 = " you sexy thing!"
    return HttpResponse("Hello" + str(v1))

def jsAlert(request):
    #Devuelve un script con un MsgBox
    mensaje = "Funciona!"

    al = '<script type="text/javascript"> window.alert("%s"); </script>' %(mensaje)
    return HttpResponse(al + "Alerta!")
    
def currentDateTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    #Regresa la fecha mas un offset especificado en la url

    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def displayThankForm(request, current_secction, person_name, company, ordered_warranty):
    if str(ordered_warranty) == "T":
        ordered_warranty = True
    else:
        ordered_warranty = False
    contextVariables = {'person_name':str(person_name), 'company':str(company), 'ordered_warranty':ordered_warranty,
                 'ship_date':datetime.datetime.now()+datetime.timedelta(hours=48),
                 'current_section':str(current_secction)}

    """Forma larga de hacer el render
    from django.template import Template, Context
    from django.template.loader import get_template
    t = get_template('displayThankForm.html ')
    c = Context(contextVariables)
    resp = t.render(c)
    return HttpResponse(resp)"""
    #Forma corta de hacer el render:
    return render(request, 'displayThankForm.html', contextVariables)


def currentDateTimeTemplate(request):
    now = datetime.datetime.now()

    contextVariables = {'current_date':now}
    return render(request, 'dateTime.html', contextVariables)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))













