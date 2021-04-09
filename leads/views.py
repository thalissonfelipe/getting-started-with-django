from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from .forms import LeadModelForm, CustomUserCreationForm
from .models import Lead
from agents.mixins import OrganizorAndLoginRequiredMixin


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organization
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organization
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganizorAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject='A lead has been created',
            message='Go to the site to see the new lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(OrganizorAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(OrganizorAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')


# def landing_page(request):
#     return render(request, 'landing.html')


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads
#     }
#     return render(request, 'leads/lead_list.html', context=context)


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'leads/lead_detail.html', context=context)


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         'form': form
#     }
#     return render(request, 'leads/lead_create.html', context=context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         'lead': lead,
#         'form': form
#     }
#     return render(request, 'leads/lead_update.html', context=context)


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads')
