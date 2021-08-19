from django import forms


SUBJECT_CHOICES = [('READING', 'Reading'), ('MATH', 'Math'), ('WRITING', 'Writing'),
                   ('SCIENCE', 'Science'), ('SOCIALSTUDIES', 'Social Studies')]
GRADE_CHOICES = [('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')]


class FileForm(forms.Form):
    subject = forms.CharField(label='Subject', widget=forms.Select(choices=SUBJECT_CHOICES))
    grade = forms.CharField(label='Grade', widget=forms.Select(choices=GRADE_CHOICES))
    file = forms.FileField()
    confirmation = forms.BooleanField(
        label="By checking this box, I confirm that the information file uploaded to the DSPP contains NO "
              "identifiable student information or any such information that would be considered a violation of the "
              "Family Educational Rights and Privacy Act (FERPA).",
        required=True)
