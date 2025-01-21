from django.views.generic import  CreateView, DetailView, ListView, UpdateView

from .models import Review

from .forms import ReviewForm

from django.contrib.auth.mixins import LoginRequiredMixin




class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm



class ReviewDetailView(DetailView):
    model = Review

class ReviewListView(ListView):
    model = Review


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm



# Create your views here.
