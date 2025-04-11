from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Specimen
from .forms import SpecimenForm


class SpecimenListView(ListView):
    model = Specimen
    template_name = 'website/home.html'
    context_object_name = 'specimens'
    ordering = ['-date_added']


class SpecimenCreateView(CreateView):
    model = Specimen
    form_class = SpecimenForm
    template_name = 'website/calculate.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Calculate the actual size
        specimen = form.save(commit=False)
        specimen.actual_size = specimen.size / specimen.mag_factor
        specimen.save()

        messages.success(self.request,
                         f'Specimen "{specimen.name}" has been added with actual size {specimen.actual_size:.6f} units')
        return super().form_valid(form)


class SpecimenDetailView(DetailView):
    model = Specimen
    template_name = 'website/detail.html'