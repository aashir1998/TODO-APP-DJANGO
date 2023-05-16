from django.views.generic import ListView, FormView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm


class IndexView(ListView, FormView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasks"
    form_class = TaskForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    success_url = "/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = self.get_object()
        return context

    def get_success_url(self):
        return self.success_url
