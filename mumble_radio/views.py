from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json
from Mumdio import wsgi
from mumble_radio.forms import UpdateListForm

class UpdateListView(FormView):
    template_name = 'queue.html'
    form_class = UpdateListForm
    success_url = reverse_lazy('home-queue')

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)

def queue_data_ajax(request):
    data = {
        'queue': wsgi.quu_list
    }

    return HttpResponse(json.dumps(data), content_type='application/json')
