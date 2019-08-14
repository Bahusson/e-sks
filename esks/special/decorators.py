from django.http import redirect
from rekruter.models import Profile

# Test sprawdzający czy klient ma akcję kwaterunkową w profilu.
def quarter_test(f, subject):
    def test_user_for_subject(request, subject, *args, **kwargs):
        if not Profile.objects.filter(user=request.Profile, subject=subject).exists():
            return redirect('initial')
        else:
            return f(request, *args, **kwargs)
    return test_user_for_subject
